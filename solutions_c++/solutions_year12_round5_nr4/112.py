#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int K, N;
char S[1009];

int edges;
bool E[300][300];
vector<int> EE[300];
int iDeg[300];
int oDeg[300];
bool visit[300];

char encode (char c) {
  if (c == 'o') return '0';
  if (c == 'i') return '1';
  if (c == 'e') return '3';
  if (c == 'a') return '4';
  if (c == 's') return '5';
  if (c == 't') return '7';
  if (c == 'b') return '8';
  if (c == 'g') return '9';
  return '!';
}

void addEdge (char a, char b) {
  if (!E[a][b]) {
    E[a][b] = true;
    edges++;
    
    EE[a].push_back(b);
    EE[b].push_back(a);
    oDeg[a]++;
    iDeg[b]++;
  }
}

int DFS (int a) {
  visit[a] = true;
  int d = max(0, iDeg[a] - oDeg[a]);
  for (unsigned int i = 0; i < EE[a].size(); i++) {
    int b = EE[a][i];
    if (!visit[b])
      d += DFS(b);
  }
  return d;
}

int main()
{
  //for (char c = '0'; c <= 'z'; c++) printf("%c (%d)\n", c, c);
  
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    //input
    scanf("%d %s", &K, S);
    N = strlen(S);
    
    //init
    for (int i = 0; i < 300; i++) {
      iDeg[i] = 0;
      oDeg[i] = 0;
      EE[i] = vector<int>();
      for (int j = 0; j < 300; j++)
        E[i][j] = false;
      visit[i] = false;
    }
    
    //edges
    edges = 0;
    for (int i = 0; i < N - 1; i++) {
      char a = S[i];
      char b = S[i + 1];
      addEdge(a, b);
      if (encode(a) != '!')
        addEdge(encode(a), b);
      if (encode(b) != '!')
        addEdge(a, encode(b));
      if (encode(a) != '!' && encode(b) != '!')
        addEdge(encode(a), encode(b));
    }
    
    //count components and disprepancies
    int disprepancies = 0;
    for (int i = 0; i < 300; i++)
      if (iDeg[i] + oDeg[i] > 0 && !visit[i]) {
        int d = DFS(i);
        disprepancies += max(1, d);
      }
    //printf("edges = %d; components = %d; disprepancies = %d\n", edges, components, disprepancies);
    printf("Case #%d: %d\n", Ti, edges + disprepancies);
  }
  return 0;
}