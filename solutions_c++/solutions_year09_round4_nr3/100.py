#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

template <int size>
int dfs(int mat[size][size], int s, int t, bool *mark){
	if(s==t) return 1;
	mark[s]=1;
	for(int i=0; i<size; i++)
		if(mat[s][i] && !mark[i] && dfs(mat, i, t, mark)){
			mat[s][i]--;
			mat[i][s]++;
			return 1;
		}
	return 0;
}

template <int size>
int flow(int mat[size][size], int s, int t){
	int res=0;
	bool mark[size]={0};
	while(dfs(mat, s, t, mark)){
		res++;
		fill_n(mark, size, 0);
	}
	return res;
}

int eval(){
	int n, k;
	cin>>n>>k;
	vector<vector<int> > mat(n, vector<int>(k));
	for(int i=0; i<n; i++)
	for(int j=0; j<k; j++)
		cin>>mat[i][j];
	int cap[202][202];
	memset(cap, 0, sizeof(cap));
	int s=2*n, t=2*n+1;
	for(int i=0; i<n; i++){
		cap[s][2*i]=1;
		cap[2*i+1][t]=1;
	}
	for(int i=0; i<n; i++)
	for(int j=0; j<n; j++){
		if(i==j)
			continue;
		int m=0;
		for(m=0; m<k; m++)
			if(mat[i][m]<=mat[j][m])
				break;
		if(m==k)
			cap[2*i][2*j+1]=1;
	}
	return n-flow(cap, s, t);
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		cout<<eval()<<endl;
	}
	return 0;
}
