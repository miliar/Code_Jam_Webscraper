#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <cassert>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;

string s[4];
int check(){
	if(s[0][0]!='.' && s[0][0]==s[0][1] && s[0][1]==s[0][2] && s[0][2]==s[0][3])return (s[0][0]=='O'?1:2);
	if(s[1][0]!='.' && s[1][0]==s[1][1] && s[1][1]==s[1][2] && s[1][2]==s[1][3])return (s[1][0]=='O'?1:2);
	if(s[2][0]!='.' && s[2][0]==s[2][1] && s[2][1]==s[2][2] && s[2][2]==s[2][3])return (s[2][0]=='O'?1:2);
	if(s[3][0]!='.' && s[3][0]==s[3][1] && s[3][1]==s[3][2] && s[3][2]==s[3][3])return (s[3][0]=='O'?1:2);
	if(s[0][0]!='.' && s[0][0]==s[1][0] && s[1][0]==s[2][0] && s[2][0]==s[3][0])return (s[0][0]=='O'?1:2);
	if(s[0][1]!='.' && s[0][1]==s[1][1] && s[1][1]==s[2][1] && s[2][1]==s[3][1])return (s[0][1]=='O'?1:2);
	if(s[0][2]!='.' && s[0][2]==s[1][2] && s[1][2]==s[2][2] && s[2][2]==s[3][2])return (s[0][2]=='O'?1:2);
	if(s[0][3]!='.' && s[0][3]==s[1][3] && s[1][3]==s[2][3] && s[2][3]==s[3][3])return (s[0][3]=='O'?1:2);
	if(s[0][0]!='.' && s[0][0]==s[1][1] && s[1][1]==s[2][2] && s[2][2]==s[3][3])return (s[0][0]=='O'?1:2);
	if(s[3][0]!='.' && s[3][0]==s[2][1] && s[2][1]==s[1][2] && s[1][2]==s[0][3])return (s[3][0]=='O'?1:2);

	bool b=false;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(s[i][j]=='.')b=true;
		}
	}
	return (b?-1:-2);
}

int main() {
	// freopen ("input.txt", "r", stdin);
	// freopen ("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		bool b=false;
		int tx,ty;
		for(int j=0;j<4;j++){
			cin>>s[j];
			for(int k=0;k<4;k++){
				if(s[j][k]=='T'){
					b=true;
					tx=j;
					ty=k;
				}
			}
		}
		int res=0;
		if(b){
			s[tx][ty]='O';
			res=check();
			s[tx][ty]='X';
			int tmp=check();
			if(res<0)res=tmp;
		}else{
			res=check();
		}
		cout<<"Case #"<<(i+1)<<": ";
		if(res==1)cout<<"O won\n";
		else if(res==2)cout<<"X won\n";
		else if(res==-1)cout<<"Game has not completed\n";
		else cout<<"Draw\n";
	}
}