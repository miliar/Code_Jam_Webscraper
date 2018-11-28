using namespace std;
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string.h>
bool gr[50][50]={false};
int n,paths=0;
bool pathCount(int a,int b)
{       
	//cout<<paths<<endl;
	//cout<<a<<","<<b<<"  "<<paths<<endl;
	if(paths>=2)
		return true;
	if(a==b)
		paths++;
	for(int i=0;i<n;i++){
		if(gr[a][i]==true)
			pathCount(i,b);
	}
	if(paths>=2)
		return true;
	return false;
}
int main()
{         
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,m,temp;
	scanf("%d",&t);
	bool diamond;
	for(int k=0;k<t;k++){
		printf("Case #%d: ",k+1);
		diamond=false;
		paths=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%d",&m);
			for(int j=0;j<m;j++){
				scanf("%d",&temp);
				gr[i][temp-1]=true;	
			}
		}
		//for(int i=0;i<n;i++){for(int j=0;j<n;j++){cout<<gr[i][j]<<" ";}cout<<endl;}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(i!=j){
					paths=0;
					//printf("Checking %d %d\n",j,i);
					if(pathCount(j,i)){
						diamond=true;break;
					}
				}
			}
		}
		//cout<<pathCount(0,2)<<endl;
		if(diamond)printf("Yes\n");
		else printf("No\n");
		memset(gr,false,sizeof(gr));
	}
	return 0;
}
