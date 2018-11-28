

#include <iostream>
#include <cstdio>
#include <queue>
#include <list>
#include <cstring>
#include <cmath>
//#include <cchr>
#include <cstring>

using namespace std;

	long cc,tt;
	
	int chess[600][600];
	int akind[600][600][600]; //◊Û…œΩ«,size,x,y is a kind
	int bkind[600][600][600]; 
	int have[600][600];

	long ans[600];

	int ifok(int k,int x,int y){
		long i,j;
		for(i=0;i<k;i++)
			for(j=0;j<k;j++)
				if(have[x+i][y+j])
					return 0;
		return 1;
	}

	void makehave(int k,int x,int y){
		long i,j;
		for(i=0;i<k;i++)
			for(j=0;j<k;j++)
				have[x+i][y+j]=1;
	}
long anskind;
int main(){
	long m,n,i,j,k;
	scanf("%d",&tt);
	char c;
	int cs;
	for(cc=0;cc<tt;cc++){
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)
			for(j=0;j<n/4;j++){
				do{
				scanf("%c",&c);
				}while(!isdigit(c)&&(c<'A'||c>'G'));
				if(isdigit(c))
					cs=c-'0';
				else
					cs=c-'A'+10;
				for(k=0;k<4;k++)
					if((cs>>(3-k))&1)
						chess[i][j*4+k]=1;
					else
						chess[i][j*4+k]=0;
			}

		//≥ı ºªØakind,bkind
		for(i=0;i<m;i++)
			for(j=0;j<n;j++){
				akind[1][i][j]=(chess[i][j]+i+j)%2?0:1;
				bkind[1][i][j]=1-akind[1][i][j];
			}
		for(k=2;k<=min(m,n);k++)//Until we find the max one
			for(i=0;i<m-k+1;i++)
				for(j=0;j<n-k+1;j++){
					if(akind[k-1][i][j]&&akind[k-1][i+1][j]&&akind[k-1][i][j+1]&&akind[k-1][i+1][j+1])
						akind[k][i][j]=1;
					else
						akind[k][i][j]=0;

					if(bkind[k-1][i][j]&&bkind[k-1][i+1][j]&&bkind[k-1][i][j+1]&&bkind[k-1][i+1][j+1])
						bkind[k][i][j]=1;
					else
						bkind[k][i][j]=0;
				}
		/*for(i=0;i<m;i++,printf("\n"))
			for(j=0;j<n;j++)
				if(chess[i][j])
					printf("X");
				else 
					printf(" ");*/

		memset(ans,0,sizeof(ans));
		memset(have,0,sizeof(have));

		for(k=min(m,n);k>=1;k--)
			for(i=0;i<m-k+1;i++)
				for(j=0;j<n-k+1;j++)
					if((akind[k][i][j]||bkind[k][i][j])&&ifok(k,i,j)){
						makehave(k,i,j);
						ans[k]++;
					}
		
		anskind=0;
		for(k=min(m,n);k>=1;k--)
			if(ans[k]) anskind++;

		printf("Case #%d: %d\n",cc+1,anskind);
		for(k=min(m,n);k>=1;k--)
			if(ans[k])
				printf("%d %d\n",k,ans[k]);

	}
	return 0;
}

