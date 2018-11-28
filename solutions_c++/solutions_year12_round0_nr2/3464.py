#include<cstdio>

using namespace std;

int main()
{
	int n;
	scanf("%d",&n);
	for(int r=1;r<=n;r++)
	{
		int N,S,p,ti,ans=0;
        scanf("%d %d %d",&N,&S,&p);
		for(int i=1;i<=N;i++)
		{
			scanf("%d",&ti);
			int avg=ti/3;
            if(p>=ti) continue;
            if(avg>=p){ ans++; continue; }
            int c=(ti-p)/2;
            if(p-c<2){ ans++; continue; }
            if((p-c==2)&&S>0){ ans++; S--; continue; }
		}
		printf("Case #%d: %d\n",r,ans);
	}
	return 0;
}
