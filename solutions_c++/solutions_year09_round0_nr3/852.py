#include <cstdio>
#include <vector>
#include <string>
using namespace std;

string S;
string W;
int A[610][20];

int Rec(int i, int j)
  {
  if (j==W.size()) return 1;
  if (i==S.size()) return 0;

  if (A[i][j]!=-1) return A[i][j];

  int ret=Rec(i+1,j);
  if (S[i]==W[j]) ret=(ret+Rec(i+1,j+1))%10000;

  return A[i][j]=ret;
  }

int main()
  {
  W="welcome to code jam";

  int T;
  scanf("%d\n",&T);
  for(int t=0;t<T;++t)
    {
    char buf[1024];
    gets(buf);
    string s(buf);
    S=s;
    if (s.size()<W.size())
      {
      printf("Case #%d: 0000\n", t+1);
      continue;
      }

    for(int i=0;i<S.size();++i)
      for(int j=0;j<W.size();++j) A[i][j]=-1;
    int r=Rec(0,0);

    printf("Case #%d: %d%d%d%d\n", t+1, r/1000, (r%1000)/100, (r%100)/10, (r%10));
    }

  return 0;
  }