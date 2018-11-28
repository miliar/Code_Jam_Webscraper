#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int t,n;

const int MAXN = 510;
const int PRIME = 100003;

int com[MAXN][MAXN];
int a[MAXN][MAXN];
int b[MAXN];

int main(){
	memset(com,0,sizeof(com));
	com[0][0] = 1;
	for(int i=1;i<MAXN;++i){
		com[i][0] = 1;
		for(int j=1;j<MAXN;++j){
			com[i][j] = (com[i-1][j-1]+com[i-1][j])%PRIME;
		}
	}
	
	memset(a,0,sizeof(a));
	for(int i=2;i<MAXN;++i){
		a[i][1] = 1;
		for(int j=2;j<i;++j){
			for(int k=1;k<j;++k){
				a[i][j]+=(int)(((long long)(com[i-j-1][j-k-1]*a[j][k]))%PRIME);
			}
		}
	}
	memset(b,0,sizeof(b));
	for(int i=2;i<MAXN;++i){
		for(int j=1;j<i;++j){
			b[i]+=a[i][j];
			b[i]%=PRIME;
		}
	}

	ifstream fin("test.in");
	ofstream fout("test.out");
	fin>>t;
	for(int time = 1; time<=t;++time){
		fin>>n;
		fout<<"Case #"<<time<<": "<<b[n]<<endl;
	}
	fin.close();
	fout.flush();
	fout.close();
	return 0;
}


