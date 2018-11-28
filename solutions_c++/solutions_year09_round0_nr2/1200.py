#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
using namespace std;
struct point{
	int i,j,al;
	bool operator <(const point p)const{
		if(al==p.al){
			if(i==p.i)return(j<p.j);
			return(i<p.i);
		}
		return (al<p.al);
	}
};
int tab[110][110], col[110][110], color=0;
char ans[110][110];
int cls[50];
vector <point> vp;
int main(){
	int T, x;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(x=1;x<=T;x++){
		int h, w;
		scanf("%d %d", &h, &w);
		vp.resize(h*w);
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				scanf("%d", &tab[i][j]);
				vp[i*w+j].i=i;vp[i*w+j].j=j;vp[i*w+j].al=tab[i][j];
			}
		}
		sort(vp.begin(),vp.end());
		memset(col,0,sizeof(col));color=0;
		for(int i=0;i<(int)vp.size();i++){
			if(!col[vp[i].i][vp[i].j]){
				int m=100000;
				int ii=vp[i].i, jj=vp[i].j;
				if(ii>0&&tab[ii-1][jj]<tab[ii][jj]&&tab[ii-1][jj]<m)m=tab[ii-1][jj];
				if(ii<h-1&&tab[ii+1][jj]<tab[ii][jj]&&tab[ii+1][jj]<m)m=tab[ii+1][jj];
				if(jj>0&&tab[ii][jj-1]<tab[ii][jj]&&tab[ii][jj-1]<m)m=tab[ii][jj-1];
				if(jj<w-1&&tab[ii][jj+1]<tab[ii][jj]&&tab[ii][jj+1]<m)m=tab[ii][jj+1];
				if(m==100000){col[ii][jj]=++color;continue;}
				if(ii>0&&tab[ii-1][jj]==m)col[ii][jj]=col[ii-1][jj];
				else if(jj>0&&tab[ii][jj-1]==m)col[ii][jj]=col[ii][jj-1];
				else if (jj<w-1&&tab[ii][jj+1]==m)col[ii][jj]=col[ii][jj+1];
				else col[ii][jj]=col[ii+1][jj];
			}
		}
		memset(cls,-1,sizeof(cls));
		int next=0;
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				if(cls[col[i][j]]==-1)cls[col[i][j]]=next++;
			}
		}
		printf("Case #%d:\n",x);
		for(int i=0;i<h;i++){
			printf("%c", cls[col[i][0]]+'a');
			for(int j=1;j<w;j++){
				printf(" %c", cls[col[i][j]]+'a');
			}
			printf("\n");
		}
	}
	return 0;
}
/*
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8
*/