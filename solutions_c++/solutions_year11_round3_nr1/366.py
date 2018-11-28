#include <iostream>
using namespace std;

char g[100][100];

int n,m;

bool put(int x,int y) {
	int dx[]=  {0,0,1,1};
	int dy[] = {0,1,0,1};
	char patt[] = "/\\\\/";
	for(int i = 0;i<4;i++)
		if (x+dx[i]<n && y+dy[i]<m && g[x+dx[i]][y+dy[i]]=='#')
			g[x+dx[i]][y+dy[i]] = patt[i];
		else return false;
		return true;

}

void compute() {
	//int n,m;
	cin>>n>>m;
	for(int i = 0;i<n;i++)
		for(int j = 0;j<m;j++)
			cin>>g[i][j];
	for(int i = 0;i<n;i++)
		for(int j = 0;j<m;j++)
			if (g[i][j]=='#')
				if (!put(i,j)) {
					cout<<"Impossible\n";
					return ;
				}
	for(int i = 0;i<n;i++) {
		for(int j = 0;j<m;j++)
			cout<<g[i][j];
		cout<<endl;
	}

}

int main() {
	int ncase;
	cin>>ncase;
	for(int i = 0;i<ncase;i++) {
		cout<<"Case #"<<i+1<<":\n";
		compute();
	}
}