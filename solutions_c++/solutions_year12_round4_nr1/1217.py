#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int position[10005],lenth[10005];
int maxn[100005];

bool solution(int n,int d)
{
    if(position[0]>lenth[0]) return 0;
    maxn[0]=position[0];
    if(maxn[0]>=d-position[0]) return 1;
    int i,j;
    int tmp,td;
    for(i=0; i<n; i++)
    {
        if(maxn[i]>=d-position[i])
            return 1;
        for(j=i+1; j<n; j++)
        {
            td=position[j]-position[i];
            if(maxn[i]<td)
                continue;
            int tmp=td<lenth[j]?td:lenth[j];
            maxn[j]=tmp>maxn[j]?tmp:maxn[j];
        }
    }
    return 0;
}

void solve()
{
	int cas,icas;
    int n,d,i,j;
    scanf("%d",&cas);
    for(icas=1; icas<=cas; ++icas)
    {
        scanf("%d",&n);
        for(i=0; i<n; i++)
        {
            scanf("%d%d",position+i,lenth+i);
            maxn[i]=-1;
        }

        scanf("%d",&d);
        bool ans=solution(n,d);
		printf("Case #%d: ",icas);
        if(ans) puts("YES");
        else puts("NO");
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    solve();
	//system("pause");
    return 0;
}
