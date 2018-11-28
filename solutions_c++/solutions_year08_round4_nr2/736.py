#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
int main()
{
	int N,ca;
	freopen("B-small-attempt1.in","r",stdin);
freopen("B-small-attempt1.out","w",stdout);
	scanf("%d",&N);
	for(ca=1;ca<=N;ca++)
	{
		int x[3],y[3];
		int n,m,a,i;
		int sign=0;
		scanf("%d%d%d",&n,&m,&a);
		for(x[0]=0;x[0]<=n;x[0]++)
			for(y[0]=0;y[0]<=m;y[0]++)
				for(x[1]=x[0];x[1]<=n;x[1]++)
					for(y[1]=y[0];y[1]<=m;y[1]++)
						for(x[2]=x[1];x[2]<=n;x[2]++)
						{
						//	for(y[2]=0;y[2]<=m;y[2]++)
							//if(x[0]==x[1]&&y[0]==y[1]||x[0]==x[2]&&y[0]==y[2]||x[1]==x[2]&&y[1]==y[2])continue;
						//	else
						//	st=0,ed=n;
						//	//while(st<=ed)
						//	{
						//		x[2]=(st+ed)/2;

								int s=(x[2]-x[0])*(y[1]-y[0])-a;
								if(s==0)
								{
									sign=1;y[2]=0;goto si;
								}

								if((x[1]-x[0])!=0&&s%(x[1]-x[0])==0&&s/(x[1]-x[0])+y[0]<=m&&s/(x[1]-x[0])+y[0]>=0)
								{
									y[2]=s/(x[1]-x[0])+y[0];
									sign=1;
									goto si;
								}
								//if(abs((x[2]-x[0])*(y[1]-y[0])-(x[1]-x[0])*(y[2]-y[0]))==a)
								//	{sign=1;goto si;}
						//	cout<<sign<<endl;if(x[2]==2)cout<<"sdf"<<endl;
						//	}
						}
			//	cout<<sign<<endl;

si:
			printf("Case #%d:",ca);
			if(sign==0)
			{
				printf(" IMPOSSIBLE\n");
				continue;
			}
				for(i=0;i<3;i++)
				printf(" %d %d",x[i],y[i]);
				printf("\n");

		
	}
	return 0;
}