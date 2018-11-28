#include<iostream>
using namespace std;

char str[130];
bool map[550][550];
bool visited[550][550];
int num[550];
int m,n;

void Change(char ch,int j,int start){
	switch(ch){
		case '0':map[j][start*4]=0;map[j][start*4+1]=0;map[j][start*4+2]=0;map[j][start*4+3]=0;break;	
		case '1':map[j][start*4]=0;map[j][start*4+1]=0;map[j][start*4+2]=0;map[j][start*4+3]=1;break;	
		case '2':map[j][start*4]=0;map[j][start*4+1]=0;map[j][start*4+2]=1;map[j][start*4+3]=0;break;	
		case '3':map[j][start*4]=0;map[j][start*4+1]=0;map[j][start*4+2]=1;map[j][start*4+3]=1;break;	
		case '4':map[j][start*4]=0;map[j][start*4+1]=1;map[j][start*4+2]=0;map[j][start*4+3]=0;break;	
		case '5':map[j][start*4]=0;map[j][start*4+1]=1;map[j][start*4+2]=0;map[j][start*4+3]=1;break;	
		case '6':map[j][start*4]=0;map[j][start*4+1]=1;map[j][start*4+2]=1;map[j][start*4+3]=0;break;	
		case '7':map[j][start*4]=0;map[j][start*4+1]=1;map[j][start*4+2]=1;map[j][start*4+3]=1;break;	
		case '8':map[j][start*4]=1;map[j][start*4+1]=0;map[j][start*4+2]=0;map[j][start*4+3]=0;break;	
		case '9':map[j][start*4]=1;map[j][start*4+1]=0;map[j][start*4+2]=0;map[j][start*4+3]=1;break;	
		case 'A':map[j][start*4]=1;map[j][start*4+1]=0;map[j][start*4+2]=1;map[j][start*4+3]=0;break;	
		case 'B':map[j][start*4]=1;map[j][start*4+1]=0;map[j][start*4+2]=1;map[j][start*4+3]=1;break;	
		case 'C':map[j][start*4]=1;map[j][start*4+1]=1;map[j][start*4+2]=0;map[j][start*4+3]=0;break;	
		case 'D':map[j][start*4]=1;map[j][start*4+1]=1;map[j][start*4+2]=0;map[j][start*4+3]=1;break;	
		case 'E':map[j][start*4]=1;map[j][start*4+1]=1;map[j][start*4+2]=1;map[j][start*4+3]=0;break;	
		case 'F':map[j][start*4]=1;map[j][start*4+1]=1;map[j][start*4+2]=1;map[j][start*4+3]=1;break;
	}
}

void Try(int x,int y,int max){
	int tx,ty;
	for(int len=1;len<=max;len++){
			for(int j=0;j<len;j++){
				tx=x+len-1;
				ty=y+j;
				if((abs(x-tx)+abs(y-ty))%2==0){
					if(visited[tx][ty]||map[x][y]!=map[tx][ty])
						return;
				}
				else{
					if(visited[tx][ty]||map[x][y]==map[tx][ty])
						return;
				}
			}
			for(int j=0;j<len;j++){
				tx=x+j;
				ty=y+len-1;
				if((abs(x-tx)+abs(y-ty))%2==0){
					if(visited[tx][ty]||map[x][y]!=map[tx][ty])
						return;
				}
				else{
					if(visited[tx][ty]||map[x][y]==map[tx][ty])
						return;
				}
			}	
	}
	for(int k=x;k<x+max;k++)
		for(int l=y;l<y+max;l++)
			visited[k][l]=1;
	num[max]++;
}


int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++){
		memset(visited,0,sizeof(visited));
		memset(num,0,sizeof(num));
		scanf("%d%d",&m,&n);
		getchar();
		n/=4;
		for(int j=0;j<m;j++){
			gets(str);
			for(int k=0;k<n;k++)
				Change(str[k],j,k);		
		}
		n*=4;
		/*for(int i=0;i<m;i++){
			for(int j=0;j<n;j++){
				printf("%d",map[i][j]);	
			}	
			printf("\n");
		}*/
		for(int len=m<n?m:n;len>=1;len--)
			for(int i=0;i<=m-len;i++)
				for(int j=0;j<=n-len;j++)
					if(!visited[i][j])
						Try(i,j,len);
		int max=m<n?m:n,cnt=0;
		for(int i=1;i<=max;i++)
			if(num[i]) cnt++;
		printf("Case #%d: %d\n",c,cnt);
		for(int i=max;i>=1;i--)
			if(num[i]) printf("%d %d\n",i,num[i]);
	}
	//system("pause");
	return 0;	
}
