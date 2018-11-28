#include<iostream>
using namespace std;
int tot,tt,r,x1,y1,x2,y2;
int map[1000][1000];
int ans,Maxx,Maxxo,Maxy,Maxyo,Minx,Minxo,Miny,Minyo;
int max(int a,int b){return (a>b?a:b);}
int min(int a,int b){return (a<b?a:b);}
void swap(int &a,int &b){int mm=a;a=b;b=mm;}
int main(){
	freopen("c.In","r",stdin);
	freopen("c.out","w",stdout);
	int i,x,y;
	scanf("%d",&tot);
	for(tt=0;tt<tot;tt++){
		scanf("%d",&r);
		Maxx=-1;Maxxo=-1;
		Maxy=-1;Maxyo=-1;
		Minx=1000;Minxo=1000;
		Miny=1000;Minyo=1000;
		memset(map,0,sizeof(0));
		for(i=0;i<r;i++){
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			if(x1>x2)swap(x1,x2);
			if(y1>y2)swap(y1,y2);
			for(x=x1;x<=x2;x++)
				for(y=y1;y<=y2;y++){
					map[x][y]=1;
					if(x>Maxx)Maxx=x;
					if(x<Minx)Minx=x;
					if(y>Maxy)Maxy=y;
					if(y<Miny)Miny=y;
				}
		}
		ans=0;
		while(Maxx!=-1){
			ans++;
			for(x=Maxx+1;x>=Minx;x--)
				for(y=Maxy+1;y>=Miny;y--){
					if(map[x][y]==0)if((map[x-1][y]==1)&&(map[x][y-1]==1))map[x][y]=1;
					if(map[x][y]==1)if((map[x-1][y]==0)&&(map[x][y-1]==0))map[x][y]=0;
					if(map[x][y]==1){
						Maxxo=max(Maxxo,x);
						Minxo=min(Minxo,x);
						Maxyo=max(Maxyo,y);
						Minyo=min(Minyo,y);
					}
			}
			Maxx=Maxxo;Maxxo=-1;
			Minx=Minxo;Minxo=1000;
			Maxy=Maxyo;Maxyo=-1;
			Miny=Minyo;Minyo=1000;
		}
		printf("Case #%d: %d\n",tt+1,ans);
	}
	return 0;
}