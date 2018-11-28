#include <iostream>
#define IMP 10000000
using namespace std;

struct Tree
{
       int val, op;
} nodes[1000000];

int DP[1000000][2];

int N, M, V;
//1 - and, 0 - or
int dp(int k, int val)
{
    if (k > (M-1)/2) { if (nodes[k].val == val) return 0; else return IMP; }    
    
    if (DP[k][val] != -1) return DP[k][val];
    
    int &ret = DP[k][val];
    
    ret = IMP;
    
    if (val == 0)
    {
            if (nodes[k].op == 1 || nodes[k].val)
            {
                 int left = dp(2*k, 0);
                 int right = dp(2*k+1, 0);
                 
                 if (!(left == IMP && right == IMP))
                 {
                      if (left != IMP) ret = left;
                      if (right != IMP) ret = min(ret, right);
                      ret += (nodes[k].op!=1);
                 }
            }
            if (nodes[k].op == 0 || nodes[k].val)
            {
                 int left = dp(2*k, 0);
                 int right = dp(2*k + 1, 0);
                 
                 int curret = 0;
                 if (!(left == IMP || right == IMP))
                 {
                      curret = left + right;
                      ret = min(ret, curret + (nodes[k].op!=0));
                 }
            }
    }
    if (val == 1)
    {
            if (nodes[k].op == 0 || nodes[k].val)
            {
                 int left = dp(2*k, 1);
                 int right = dp(2*k+1, 1);
                 
                 if (!(left == IMP && right == IMP))
                 {
                      int curret = IMP;
                      if (left != IMP) curret = left;
                      if (right != IMP) curret = min(curret, right);
                      ret = min(ret, curret + (nodes[k].op!=0));
                 }
            }
            if (nodes[k].op == 1 || nodes[k].val)
            {
                 int left = dp(2*k, 1);
                 int right = dp(2*k + 1, 1);
                 
                 int curret = 0;
                 if (!(left == IMP || right == IMP))
                 {
                      curret = left + right;
                      ret = min(ret, curret + (nodes[k].op!=1));
                 }
            }
    }
    return ret;
}

void solve()
{
     memset(DP, -1, sizeof(DP));
     
     int cnt = 0;
     scanf("%d%d", &M, &V);
     
     for (int i = 1; i <= (M-1)/2; i++)
      scanf("%d%d", &nodes[i].op, &nodes[i].val);
     for (int i = (M-1)/2 + 1; i <= M; i++)
      scanf("%d", &nodes[i].val);
     
     if (dp(1, V) == IMP) printf("IMPOSSIBLE\n");
     else printf("%d\n", dp(1, V));
}
int main()
{
    int q; scanf("%d", &q);
    for (int i = 0; i < q; i++) 
    {
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}
