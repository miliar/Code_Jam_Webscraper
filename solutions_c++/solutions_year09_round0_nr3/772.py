#include <iostream>
#include <cmath>
#include <string>
#include <sstream>

#define TASK "file"
#define N 600
using namespace std;

string word="welcome to code jam";
int test;
string s;

int d[N][20];
int mark[N][20];

int cur_mark;

int fuck(int n,int m){
	if (m==0) return 1;
	if (n==0) return 0;
	if (mark[n][m]==cur_mark) return d[n][m];
	mark[n][m]=cur_mark;
	d[n][m]=0;
	if (s[n-1]==word[m-1]) d[n][m]=(d[n][m]+fuck(n-1,m-1))%10000;
	d[n][m]=(d[n][m]+fuck(n-1,m))%10000;
	return d[n][m];
}

int main(void){
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
	getline(cin,s);
	stringstream ss(s);
	ss>>test;
	for (int z=0;z<test;z++){
		cur_mark=z+1;
		printf("Case #%i: ",z+1);
		getline(cin,s);
		
		int ans=fuck(s.size(),word.size());
		printf("%04i\n",ans);
	}

	return 0;
}