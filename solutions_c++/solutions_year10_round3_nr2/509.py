#include<algorithm>
#include<cstdlib>
#include<set>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;

int T,L,P,C,line;

void solve()
{
  int factor=C;
  int res=L*C,count=0;
  while(res<P) {
      factor*=factor;
      res=L*factor;
      count++;
  }
  printf("Case #%d: %d\n",line,count);

}

int main()
{
      freopen("E:\\³Ì±ó\\Round 1C 2010\\B\\B-small-attempt0.in","r",stdin);
      freopen("E:\\³Ì±ó\\Round 1C 2010\\B\\B-small-attempt0.out","w",stdout);
      scanf("%d",&T);
      for(line=1;line<=T;++line) {
              scanf("%d%d%D",&L,&P,&C);
              solve();
      }
     // system("PAUSE");
      return 0;
}

