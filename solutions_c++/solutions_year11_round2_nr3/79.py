#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>

using namespace std;

struct Edge {
  Edge(int x = 0, int y = 0) : x(0), y(0) {}
  int x;
  int y;
};

typedef vector<int> Poly;
vector<Poly> polygons;

bool inInterval(int i, int start, int end) {
  assert(start != end);
  if (start < end)
    return i >= start && i <= end;
  else
    return i >= start || i <= end;
}

void enumPoly(Poly& poly, vector<Edge>& edges) {
  int n = poly.size(), m = edges.size();
  if (m == 0)
    polygons.push_back(poly);
  else {
    vector<int> poly1, poly2;
    vector<Edge> edges1, edges2;
    int x = edges[0].x, y = edges[0].y;
    for (int i = 0; i < n; i++) {
      if (inInterval(poly[i], x, y))
        poly1.push_back(poly[i]);
      if (inInterval(poly[i], y, x))
        poly2.push_back(poly[i]);
    }
    for (int i = 1; i < m; i++) {
      if (inInterval(edges[i].x, x, y) && inInterval(edges[i].y, x, y))
        edges1.push_back(edges[i]);
      else if (inInterval(edges[i].x, y, x) && inInterval(edges[i].y, y, x))
        edges2.push_back(edges[i]);
      else
        cerr << "crossing edges!" << endl;
    }
    enumPoly(poly1, edges1);
    enumPoly(poly2, edges2);
  }
}

int main() {
  int nCases;
  int n, m;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%d%d", &n, &m);
    Poly poly(n);
    vector<Edge> edges(m);
    for (int i = 0; i < n; i++)
      poly[i] = i;
    for (int i = 0; i < m; i++) {
      scanf("%d", &edges[i].x);
      edges[i].x--;
    }
    for (int i = 0; i < m; i++) {
      scanf("%d", &edges[i].y);
      edges[i].y--;
    }
    polygons.clear();
    enumPoly(poly, edges);
    int nPoly = polygons.size();
    int maxColors = n;
    for (int i = 0; i < nPoly; i++) {
      maxColors = min(maxColors, (int) polygons[i].size());
    }
    vector<int> colors(n, 0), optColors;
    vector<int> usedColors(maxColors);
    vector<int> polyColors(maxColors);
    int nOptColors = 0;
    while (colors[n - 1] == 0) {
      int nUsedColors = 0;
      for (int i = 0; i < maxColors; i++) {
        usedColors[i] = false;
      }
      for (int i = 0; i < n; i++) {
        if (!usedColors[colors[i]]) {
          usedColors[colors[i]] = true;
          nUsedColors++;
        }
      }
      if (nUsedColors > nOptColors) {
        bool validColors = true;
        for (int i = 0; i < nPoly; i++) {
          int nPolyColors = 0;
          Poly& p = polygons[i];
          for (int j = 0; j < maxColors; j++) {
            polyColors[j] = false;
          }
          for (int j = 0; j < (int) p.size(); j++) {
            int c = colors[p[j]];
            if (!polyColors[c]) {
              polyColors[c] = true;
              nPolyColors++;
            }
          }
          if (nPolyColors < nUsedColors) {
            validColors = false;
            break;
          }
        }
        if (validColors) {
          nOptColors = nUsedColors;
          optColors = colors;
        }
      }
      for (int i = 0;; i++) {
        colors[i]++;
        if (colors[i] < maxColors) break;
        colors[i] = 0;
      }
    }
    printf("Case #%i: %i\n", iCase, nOptColors);
    for (int i = 0; i < n; i++) {
      if (i > 0) printf(" ");
      printf("%i", optColors[i] + 1);
    }
    printf("\n");
    /*for (size_t i = 0; i < polygons.size(); i++) {
      Poly& p = polygons[i];
      cout << "polygon " << i << " :";
      for (size_t j = 0; j < p.size(); j++) {
        cout << " " << p[j];
      }
      cout << endl;
    }*/
  }
  return 0;
}
