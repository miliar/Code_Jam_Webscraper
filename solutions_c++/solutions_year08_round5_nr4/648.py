//#include<algorithm>
//#include<iostream>
//using namespace std;
//#define INF 0x3FFFFFFF
//
//
//int D[10005][2],Map[10005];
//int C[10005];
//int M,V;
//
//int main()
//{
//	//freopen("A-large.in", "r", stdin);
//	//freopen("A-large.out", "w", stdout);
//    int l,ncase; scanf("%d",&ncase);
//	for(l=1;l<=ncase;++l)
//	{
//		int i;
//		memset(D,-1,sizeof(D));
//		scanf("%d%d",&M,&V);
//		for(i=1;i<=(M-1)/2;i++)scanf("%d%d",&Map[i],&C[i]);
//
//		for(int i=(M-1)/2+1;i<=M;i++)
//		{
//			int t;
//			scanf("%d",&t);
//			D[i][t]=0;
//			D[i][1-t]=INF;
//		}
//		for(int i=(M-1)/2;i>=1;i--)
//		{
//			D[i][0]=D[i][1]=INF;
//			if(Map[i]==1)
//			{
//				D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][0]);
//				D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][1]);
//				D[i][0]=min(D[i][0],D[i*2][1]+D[i*2+1][0]);
//				D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][1]);
//			}
//			else 
//			{
//				D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][0]);
//				D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][1]);
//				D[i][1]=min(D[i][1],D[i*2][0]+D[i*2+1][1]);
//				D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][0]);
//			}
//			if(C[i])
//			{
//				if(Map[i]==0)
//				{
//					D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][0]+1);
//					D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][1]+1);
//					D[i][0]=min(D[i][0],D[i*2][1]+D[i*2+1][0]+1);
//					D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][1]+1);
//				}
//				else 
//				{
//					D[i][0]=min(D[i][0],D[i*2][0]+D[i*2+1][0]+1);
//					D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][1]+1);
//					D[i][1]=min(D[i][1],D[i*2][0]+D[i*2+1][1]+1);
//					D[i][1]=min(D[i][1],D[i*2][1]+D[i*2+1][0]+1);
//				}
//			}
//		}
//		if(D[1][V]<INF)printf("Case #%d: %d\n",l,D[1][V]);
//		else printf("Case #%d: IMPOSSIBLE\n",l);
//	}
//
//	return 0;
//}



#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;



bool Map[110][110];
int M,N,num[110][110];
int DFS(int i,int k)
{
	if(num[i][k]!=-1)return num[i][k];
	if(i==M&&k==N)return num[i][k]=1;

	int answer=0;
	if(i<M&&k<N-1&&!Map[i+1][k+2])
		answer=(answer+DFS(i+1,k+2))%10007;
	if(i<M-1&&k<N&&!Map[i+2][k+1])
		answer=(answer+DFS(i+2,k+1))%10007;

	num[i][k]=answer;
	return num[i][k];
}
int main()
{

	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt2.out","w",stdout);
	int ncase;scanf("%d",&ncase);
	int l,x,y,T;
	for(l=1;l<=ncase;l++)
	{
		scanf("%d%d%d",&M,&N,&T);
		
		memset(Map,0,sizeof(Map));
		while(T--)
		{
			scanf("%d%d",&x,&y);
			Map[x][y]=true;
		}
		memset(num,-1,sizeof(num));

		DFS(1,1);
		printf("Case #%d: %d\n",l,num[1][1]);
	}
	return 0;
}
