#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int N,M;
char mp[101][101];
int height[101][101];
int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};
char next;

bool valid(int i,int j){
	return (i>=0 && i < N && j >= 0 && j < M);
}

char search(int i,int j){
	if (mp[i][j]) return mp[i][j];
	int best = 1000000000,bestk = -1;
	for (int k=0;k<4;k++)
		if (valid(i+di[k],j+dj[k]) && height[i+di[k]][j+dj[k]] < best){
			best = height[i+di[k]][j+dj[k]];
			bestk = k;
		}
	if (best < height[i][j]){
		return mp[i][j] = search(i+di[bestk],j+dj[bestk]);
	}
	return mp[i][j] = next++;

}

int main(int argc,const char* argv[]){
	istream * _in = 0;
	ostream * _out = 0;
	if (argc > 1) _in = new ifstream(argv[1]); else _in = & cin;
	if (argc > 2) _out = new ofstream(argv[2]); else _out = & cout;
	istream & in = *_in;
	ostream & out = *_out;
	int TC,cas = 1;
	for (in >> TC;cas <= TC;cas++){
		
		in >> N >> M;
		memset(mp,0,sizeof(mp));
		next = 'a';
		for (int i=0;i<N;i++)
			for (int j=0;j<M;j++)
				in >> height[i][j];
		out << "Case #" << cas << ":" << endl;
		for (int i=0;i<N;i++){
			for (int j=0;j<M;j++)
				out << (j>0?" ":"") << search(i,j);
			out << endl;
		}
	}

	if (_in != &cin) delete _in;
	if (_out != &cout) delete _out;
};
