#include<algorithm>
#include<cstdlib>
#include<set>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;

const int maxn=1005;
int T,N,line;
int A[maxn],B[maxn];

bool check(int i,int j)
{
     int dx=A[i]-A[j];
     int dy=B[i]-B[j];
     if(dx*dy<0) return true;
     else return false;
}

void solve()
{
  int count=0;
  for(int i=0;i<N;++i) for(int j=i+1;j<N;++j) {
      if(check(i,j)) count++;
  }
  printf("Case #%d: %d\n",line,count);

}

int main()
{
      freopen("E:\\³Ì±ó\\Round 1C 2010\\A\\A-large.in","r",stdin);
      freopen("E:\\³Ì±ó\\Round 1C 2010\\A\\A-large.out","w",stdout);
      scanf("%d",&T);
      for(line=1;line<=T;++line) {
              scanf("%d",&N);
              for(int i=0;i<N;++i) {
                 scanf("%d%d",&A[i],&B[i]);
              }
              solve();
      }
      //system("PAUSE");
      return 0;
}

