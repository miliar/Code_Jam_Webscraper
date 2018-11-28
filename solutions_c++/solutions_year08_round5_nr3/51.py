#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <stdio.h>

#define LL long long


using namespace std;


bool domatching(int v,  vector<int> * const &adjlist, bool *visited, int *matched) {
	visited[v]=true;
	int i;
	for (i=0; i<adjlist[v].size(); i++) {
		int next=adjlist[v][i];
		if (matched[next]==-1) {
			matched[next]=v;
			return true;
		}
		else {
			if (!visited[matched[next]] && domatching(matched[next],adjlist,visited,matched)) {
				matched[next]=v;
				return true;
			}
		}
	}
	return false;
}

int getmaximummatching(vector<int> * const &adjlist, int N, int M,int *matched) {
	int i;
	int ans=0;
	bool *visited=new bool[N];
	memset(matched,-1,M*sizeof(int));
	for (i=0; i<N; i++) {
		memset(visited,0,N);
		if (domatching(i,adjlist,visited,matched)) ans++;		
	}
	delete[] visited;
	return ans;
}

bool ada[100][100];
int W,H;

char str[1000];

int incx[] = {-1,-1,-1,1,1,1};
int incy[] = {-1,0,1,-1,0,1};

int encode(int x, int y) {
	if (x%2==0) {
		return (x/2)*H+y;
	}
	else {
		return ((x-1)/2)*H+y;
	}
}
vector<int> adjlist[8000];
int matched[8000];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,T;
	scanf("%d", &T);
	int i,j,x,y,k;
	for (t=1; t<=T; t++) {
		int nbroken=0;
		scanf("%d %d", &H, &W);
		for (i=0; i<H; i++) {
			scanf("%s", str);
			for (j=0; j<W; j++) {
				if (str[j]=='.')
					ada[i][j]=true;
				else {
					ada[i][j]=false;
					nbroken++;
				}
			}
		}

		for (x=0; x<W; x+=2) {
			for (y=0; y<H; y++) {
				int from=encode(x,y);
				adjlist[from].clear();
				if (!ada[y][x]) continue;

				for (k=0; k<6; k++) {
					int nx=x+incx[k];
					int ny=y+incy[k];
					if (!ada[ny][nx]) continue;
					if (nx<0 || nx>=W || ny<0 || ny>=H) continue;
					adjlist[from].push_back(encode(nx,ny));
				}
			}
		}
		int ans=getmaximummatching(adjlist,H*((W+1)/2),H*(W/2),matched);
		printf("Case #%d: %d\n",t,H*W-ans-nbroken);
	}
	return 0;
}

