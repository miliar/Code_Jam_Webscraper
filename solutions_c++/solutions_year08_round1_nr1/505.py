#include<iostream>
using namespace std;
#define MAX 900
int n,m,lef,righ;
int g[MAX][20],v[20];
int left_value[20],right_value[MAX],left_tag[20],right_tag[MAX];
int match[MAX],map[20][MAX];
int min(int a,int b){
	return a<b?a:b;
}
int max( int a,int b){
	return a>b?a:b;
}
int dfs(int p)
{
	left_tag[p]=1;
	for(int i=0;i<righ;i++)
		if(!right_tag[i] && left_value[p]+right_value[i]==map[p][i] )
		{
			right_tag[i]=1;
			if(match[i]==-1||dfs(match[i]))
			{
				match[i]=p;
				return 1;
			}
		}
		return 0;
}
int maxmatch()
{
	memset(left_value,0,sizeof(left_tag));
	memset(right_value,0,sizeof(right_tag));
	memset(match,-1,sizeof(match));
	int i,j,k,d,m;
	for(i=0;i<lef;i++){
		left_value[i]=0xfffffff;
		for(j=0;j<righ;j++)
			if(left_value[i]>map[i][j])
				left_value[i]=map[i][j];
	}
	for(i=0;i<lef;i++){
		while(1){
			memset(left_tag,0,sizeof(left_tag));
			memset(right_tag,0,sizeof(right_tag));
			if(dfs(i))break;
			d=0xfffffff;
			for(j=0;j<lef;j++){
				if(left_tag[j])
					for(k=0;k<righ;k++)
						if(!right_tag[k])d=min(d,map[j][k]-left_value[j]-right_value[k]);
			}
			for(j=0;j<lef;j++)
				if(left_tag[j])left_value[j]+=d;
			for(j=0;j<righ;j++)
				if(right_tag[j])right_value[j]-=d;
		}
	}
 
	for(m=i=0;i<righ;i++)
		//if(match[i]!=-1)m+=map[match[i]][i];
		m+=map[ match[i] ][i];
	return m;
}
 
int x[900],y[900];

	
 
 
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int t,i,j,k,n;
	scanf("%d",&t);
	int ca=0;
	while(t--){
		memset(map,0,sizeof(map));
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%d",&x[i]);
		for(i=0;i<n;i++)scanf("%d",&y[i]);

		for(i=0;i<n;i++){
			for(j=0;j<n;j++)
				map[i][j]=x[i]*y[j];
			
		}
		lef=righ=n;

		//for(i=0;i<n;i++){
		//	for(j=0;j<n;j++)
		//		cout<<map[i][j]<<" ";
		//	cout<<endl;
		//}

		printf("Case #%d: ",++ca);
		int minnum=maxmatch();
		printf("%d\n",minnum);
	}

	return 0;
}
