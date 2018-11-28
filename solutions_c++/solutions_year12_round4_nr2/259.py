#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int infinity = 1e9 + 9;

int N, W, L;
int R[1009];
//int I[1009];
int X[1009];
int Y[1009];

//candidates
vector<int> Cx;
vector<int> Cy;

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    //input
    scanf("%d %d %d", &N, &W, &L);
    for (int i = 0; i < N; i++)
      scanf("%d", &R[i]);
    
    //sort
    /*
    for (int i = 0; i < N; i++)
      for (int j = i + 1; j < N; j++)
        if (R[i] < R[j]) {
          int r = R[i]; R[i] = R[j]; R[j] = r;
          int t = I[i]; I[i] = I[j]; I[j] = t;
        }
    */
    
    //set of corners
    Cx = vector<int>();
    Cy = vector<int>();
    
    Cx.push_back(-10000);
    Cy.push_back(-10000);
    
    for (int i = 0; i < N; i++) {
      bool found = false;
      for (unsigned int p = 0; p < Cx.size(); p++) {
        //assign
        X[i] = Cx[p] + R[i];
        Y[i] = Cy[p] + R[i];
        X[i] = max(X[i], 0);
        X[i] = min(X[i], W);
        Y[i] = max(Y[i], 0);
        Y[i] = min(Y[i], L);
        //check
        bool ok = true;
        for (int j = 0; j < i; j++)
          if ((abs(X[j] - X[i]) < R[i] + R[j]) && (abs(Y[j] - Y[i]) < R[i] + R[j])) {
            ok = false;
            break;
          }
        if (!ok) continue;
        found = true;
        break;
      }
      Cx.push_back(X[i] + R[i]);
      Cy.push_back(Y[i] - R[i]);
      Cx.push_back(X[i] - R[i]);
      Cy.push_back(Y[i] + R[i]);
      
      if (!found)
        printf("Error.");
    }
    
    //output
    printf("Case #%d:", Ti);
    for (int i = 0; i < N; i++)
      printf(" %d %d", X[i], Y[i]);
    printf("\n");
  }
  return 0;
}