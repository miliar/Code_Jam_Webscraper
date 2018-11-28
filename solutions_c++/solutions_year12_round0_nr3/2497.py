#include <cstdio>
#include <vector>
#include <set>

using namespace std;

#define REP(i,n) for(__typeof(n) i=0;i!=(n);++i)

typedef pair<int,int> PI;

int main()
{
        int T;
        scanf("%d",&T);
        REP(i,T)
        {
                set<PI>S;
                int A,B,ans(0);
                scanf("%d%d",&A,&B);
                int tmp=A,ten(1),dig(0);
                while(tmp>0) tmp/=10,ten*=10,dig++;
                ten/=10;
                for (int j=A;j<=B;++j) 
                {
                        int num=j;
                        REP(k,dig) 
                        {
                                int last=num%10;
                                num/=10;
                                num+=last*ten;
                                if (num!=j && num>=A && num<=B && !S.count(PI(min(num,j),max(num,j)))) 
                                {
                                        //printf("%d %d\n",j,num);
                                        S.insert(PI(min(num,j),max(num,j)));
                                        ans++;
                                }
                        }
                }
                printf("Case #%d: %d\n",i+1,ans);
        }
        return 0;
}
