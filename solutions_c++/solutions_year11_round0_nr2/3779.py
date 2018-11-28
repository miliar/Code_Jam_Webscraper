//Fruit of Light
//FoL CC
//Mandarine
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

//s kym zmizne, s kym sa meni, na koho sa meni

int main() {
  int t;
  scanf ("%d", &t);
  for (int i = 0; i < t; i++) {
    vector <char> a(300);
    vector <char> b(300);
    vector <char> c(300);
    int n;
    scanf ("%d ", &n);
    while (n--) {
      char x, y, z;
      scanf ("%c %c %c", &x, &y, &z);
      b[x] = y;
      b[y] = x;
      c[x] = c[y] = z;
    }
    scanf ("%d ", &n);
    while (n--) {
      char x, y;
      scanf ("%c %c", &x, &y);
      a[x] = y;
      a[y] = x;
    }
    
//     for (int j = 65; j < 100; j++) printf ("%c %c %c %c\n", j, a[j], b[j], c[j]);
    scanf ("%d ", &n);
    vector <char> v;
    while (n--) {
      char x;
      scanf ("%c", &x);
      bool d = false;
      int s = v.size();
      if (a[x]) {
	for (int j = 0; j < s; j++) {
	  if (v[j] == a[x]) {
	    d = true;
	    break;
	  }
	}
      }
      if ((s) && (b[v[s-1]] == x)) v[s-1] = c[x];
      else if (d) v.resize(0);
      else v.push_back(x);
//       printf ("Case #%d: [", i+1);
//       for (int j = 0; j < v.size(); j++) {
// 	if (!j) printf ("%c", v[j]);
// 	else printf (", %c", v[j]);
//       }
//       printf ("]\n");

    }
    printf ("Case #%d: [", i+1);
    for (int j = 0; j < v.size(); j++) {
      if (!j) printf ("%c", v[j]);
      else printf (", %c", v[j]);
    }
    printf ("]\n");
  }
  return 0;
}