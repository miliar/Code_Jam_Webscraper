#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
using namespace std;

int K, N;
char G[60][60];

bool Check(char ch){
	for (int i=0;i<N;++i) for (int j=0;j<N;++j) if (G[i][j]==ch){
		if (i+K <= N) {
			int x = i+K-1;
			while ((x>=i)&&(G[x][j]==ch)) --x;
			if (x<i) return true;
		}
		if (j+K <= N) {
			int y = j+K-1;
			while ((y>=j)&&(G[i][y]==ch)) --y;
			if (y<j) return true;
		}
		if ((i+K<=N)&&(j+K<=N)){
			int x = i+K-1;
			int y = j+K-1;
			while ((x>=i)&&(G[x][y]==ch)) --x, --y;
			if (x<i) return true;
		}
		if ((i+K<=N)&&(j-K+1>=0)) {
			int x = i+K-1;
			int y = j-K+1;
			while ((x>=i)&&(G[x][y]==ch)) --x, ++y;
			if (x<i) return true;
		}
	}
	return false;
}

void Rotate(){
	char tmp[60][60];
	for (int i=0;i<N;++i) for (int j=0;j<N;++j) 
		tmp[i][j] = G[i][j];
	for (int i=0;i<N;++i) for (int j=0;j<N;++j)
		G[j][N-1-i] = tmp[i][j];

	for (int j=0;j<N;++j) {
		string tmp="";
		for (int i=0;i<N;++i) 
			if (G[i][j]!='.') {
				tmp = G[i][j] + tmp;
				G[i][j] = '.';
			}
		int len = tmp.size();
		for (int i=0;i<len;++i)
			G[N-1-i][j] = tmp[i];
	}
}

int main(){
	FILE* fin = freopen("input.in", "r", stdin);
	int T;
	scanf("%d", &T);
	char line[200];
	for (int t=0;t<T;++t){
		scanf("%d%d", &N, &K);
		gets(line);
		for (int i=0;i<N;++i) gets(G[i]);

		bool red = Check('R');
		bool blue = Check('B');
		Rotate();
		red = red || Check('R');
		blue = blue || Check('B');

		printf("Case #%d: ", t+1);
		if (red && blue) printf("Both");
		else if (red) printf("Red");
		else if (blue) printf("Blue");
		else printf("Neither");
		printf("\n");
	}

	return 0;
}
