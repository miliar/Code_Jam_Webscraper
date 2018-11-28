#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
#define M 50
char sou[M+5][M+5];
int net[M+5][M+5];
int used[M+5][M+5];
int sum[M+5];
int n,m;
int getmin(int a,int b){
	return a>b?b:a;
}

int check(int a,int b,int c){
	int i,j;
	int key=net[a][b];
	for(i=0;i<c;i++){
		for(j=0;j<c;j++){
			int x=a+i;
			int y=b+j;

			if(x>=n||y>=m)
				return 0;
			if(used[x][y])
				return 0;

			if((i+j)%2==1){
				if(net[x][y]==key)
					return 0;
			}
			else if(net[x][y]!=key)
				return 0;
		}
	}
	return 1;
}

int color(int a,int b,int c){
	int i,j;
	for(i=0;i<c;i++){
		for(j=0;j<c;j++){
			used[a+i][b+j]=1;
		}
	}
	return 0;
}
int main(){

	freopen("C-small-attempt0.in","rb",stdin);
	freopen("C-small-attempt0.out","wb",stdout);
	int ca,c=0,i,j,k,u,v,p;
	scanf("%d",&ca);
	while(ca--){
		c++;
		scanf("%d%d",&n,&m);
		getchar();
		for(i=0;i<n;i++){
			scanf("%s",sou[i]);
		}

		memset(net,0,sizeof(net));
		memset(used,0,sizeof(used));
		memset(sum,0,sizeof(sum));
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				char ch=sou[i][j/4];
				int temp;
				if(ch>='0'&&ch<='9')
					temp=ch-'0';
				else temp=ch-'A'+10;
				net[i][j]=(temp>>(3-(j%4)))%2;
				//cout<<net[i][j]<<" ";
			}
			//cout<<endl;
		}

		p=getmin(n,m);
		for(i=p;i>=1;i--){
			for(j=0;j<n;j++){
				for(k=0;k<m;k++){
					if(check(j,k,i)){
						sum[i]++;
						color(j,k,i);
					}
				}
			}
		}

		int res=0;
		for(i=1;i<=p;i++){
			if(sum[i]!=0)
				res++;
		}
		printf("Case #%d: %d\n",c,res);
		for(i=p;i>=1;i--){
			if(sum[i]!=0){
				printf("%d %d\n",i,sum[i]);
			}
		}
	}
	return 0;
}