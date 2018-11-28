#include<stdio.h>
#include<string.h>
#include<algorithm>
bool map[200][200],t[200][200];
int main(){
	int times;
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		printf("Case #%d: ",tm);
		int n,x1,y1,x2,y2;
		scanf("%d",&n);
		memset(map,0,sizeof(map));
		for(int i=0;i<n;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			x1--;x2--;y1--;y2--;
			for(int a=x1;a<=x2;a++)
				for(int b=y1;b<=y2;b++)
					map[a][b]=1;
		}
		for(int ct=0;;ct++){
			for(int i=0;i<200;i++)
				for(int j=0;j<200;j++){
					if(map[i][j] && (i==0 || map[i-1][j]==0) && (j==0 || map[i][j-1]==0))	{
						t[i][j]=0;
					}else if(map[i][j] ==0 && i && map[i-1][j] && j && map[i][j-1]){
						t[i][j]=1;
					}else{
						t[i][j]=map[i][j];
					}
				}
			bool all_die=1;
			for(int i=0;i<200;i++)
				for(int j=0;j<200;j++){
					if(map[i][j]=t[i][j])
						all_die=0;
				}
			if(all_die){
				printf("%d\n",ct+1);
				break;
			}
		}
	}
	return 0;
}
