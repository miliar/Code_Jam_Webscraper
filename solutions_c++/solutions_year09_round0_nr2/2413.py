#include<iostream>
#include<algorithm>
#include<cstring>
#include<cctype>
using namespace std;

int a[]={-1,0,0,-1,0,1,1,0};
int T,H,W,min,x1,y1,x,y,kase;

int s[150][150],res[150][150],c;


char dfs(int i,int j){
	if(res[i][j])return res[i][j];	
	int k;
	min=32767;
	for(k=0;k<8;k+=2){
		x1=i+a[k];
		y1=j+a[k+1];
		if(x1<0 || x1>=H || y1<0 || y1>=W)continue;
		if(s[x1][y1]<s[i][j]){
			if(s[x1][y1]<min){
				min=s[x1][y1];
				x=x1;
				y=y1;
			}
		}
	}
	if(min==32767){
		return res[i][j]=c++;
	}
	else return res[i][j]=dfs(x,y);
}


int main(){
	int i,j,k,l,T;
	//freopen("1.txt","r",stdin);
	//freopen("b-small.out","w",stdout);
	cin>>T;
	while(T--){
		c='a';
		cin>>H>>W;
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				cin>>s[i][j];
			}
		}
		memset(res,0,sizeof(res));
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				if(!res[i][j])res[i][j]=dfs(i,j);
			}
		}
		printf("Case #%d:\n",++kase);
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				if(j)printf(" ");
				printf("%c",res[i][j]);
			}
		printf("\n");
		}
	}
	return 0;
}

