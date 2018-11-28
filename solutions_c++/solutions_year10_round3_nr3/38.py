#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define N 512
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define ROF(i,a,b) for(i=(a);i>=(b);i--)
#define min(a,b) (a<b) ? a : b

int n,m,T;
int arr[N+10][N+10];
int dy[N+10][N+10];
int count[N+10];

#define array(a,b) arr[i][j]
//#define array(a,b) ( (arr[a][ ( (b-1)/8) +1]>>(7 - ( b-1 )%8)) %2 )

int min3(int a,int b,int c)
{
	return (a<b && a<c) ? a:min(b,c);
}

void process(){
	int i,j,k,max,cnt=0,l;
	memset(count,0,sizeof(count));
	while(1) {
		max=-1;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++) {
				if(arr[i][j]==-1) { dy[i][j]=0; continue; }
				else if(arr[i-1][j-1]==-1 || arr[i-1][j]==-1 || arr[i][j-1]==-1) {
					dy[i][j]=1;
					continue;
				}
				if(arr[i-1][j-1]==arr[i][j] && arr[i-1][j]!=arr[i][j] && arr[i][j-1]!=arr[i][j])
					dy[i][j]=min3(dy[i-1][j],dy[i-1][j-1],dy[i][j-1])+1;
				else dy[i][j]=1;
				
				if(max<dy[i][j]) max=dy[i][j];
			}
		if(max==-1) break;
		
		if(count[max]==0) cnt++;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++) 
				if(max==dy[i][j]) {
					for(k=i-max+1;k<=i;k++) {
						for(l=j-max+1;l<=j;l++)
							if(arr[k][l]==-1) break;
						if(l<=j) break;
					}
					if(k<=i) continue;
					for(k=i-max+1;k<=i;k++) 
						for(l=j-max+1;l<=j;l++)
							arr[k][l]=-1;

					count[max]++;
				}
	}
	printf("Case #%d: %d\n",T,cnt);
	for(i=n;i>=1;i--)
		if(count[i]) printf("%d %d\n",i,count[i]);
}

char htoi(char ass){
	char ret_;
	if ('0' <= ass && ass <= '9'){
		ret_ =  ass - '0';
	}
	if (ass >= 'A'){
		ret_ =  ass - 'A' + 10;
	}

	
	return ret_;
	exit(0);
}

void input(){
	scanf("%d %d\n",&n,&m);
	int i,j,k,c;
	char up,down;
	FOR(i,1,n){
		c=0;
		FOR(j,1,m/4){
			scanf("%c",&up);
			up = htoi(up);
			ROF(k,3,0){
				arr[i][++c] = (up>>k)%2;
			}
		}
		scanf("\n");
	}
}

int main(){
	int t;
	scanf("%d",&t);
	FOR(T,1,t){
		input();
		process();
	}
	return 0;
}
