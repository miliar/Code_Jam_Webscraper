#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
int map[1000][1000];
int minx,miny,maxx,maxy;
inline int get(int x,int y){
	if(x<=0 || y<=0)
		return 0;
	return map[x][y];
}
int go(){
	bool has_one=true;
	int t;
	for(t=0;has_one;++t){
		has_one=false;
		for(int i=maxx+1;i>=minx;--i)
			for(int j=maxy+1;j>=miny;--j){
				if(get(i-1,j)+get(i,j-1)+map[i][j]>=2){
					map[i][j]=1;
					has_one=true;
					maxx=max(maxx,i);
					maxy=max(maxy,j);
				}else{
					map[i][j]=0;
				}
			}
	}
	return t;
}
int main(){
	int t;
	cin>>t;
	for(int kk=1;kk<=t;++kk){
		int r;
		cin>>r;
		minx=miny=100000;
		maxx=maxy=0;
		memset(map,0,sizeof(map));
		while(r--){
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			minx=min(minx,x1);
			minx=min(minx,x2);
			miny=min(miny,y1);
			miny=min(miny,y2);
			maxx=max(maxx,x1);
			maxx=max(maxx,x2);
			maxy=max(maxy,y1);
			maxy=max(maxy,y2);
			for(int i=min(x1,x2);i<=max(x1,x2);++i)
				for(int j=min(y1,y2);j<=max(y1,y2);++j)
					map[i][j]=1;
		}
		printf("Case #%d: %d\n",kk,go());
	}
	return 0;
}
