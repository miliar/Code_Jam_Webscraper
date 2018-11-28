// #includes {{{
#include <algorithm>
#include <numeric>
 
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
 
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cstring>
 
#include <cmath>
#include <complex>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
// }}}
 

int T, K, N;

const int MAX=60;
char c[MAX][MAX];

void print(){
	REP(i, N){
		REP(j, N){
			cout<<c[i][j];
		}
		cout<<endl;
	}
	cout<<endl;
}
void init(){
	REP(i, MAX)REP(j, MAX)c[i][j]='.';
}
int dir[4][2]={{0, 1}, {1, 0}, {1, 1}, {1, -1}};

bool can_win(char p){
	REP(i, N){
		REP(j, N){
			REP(d, 4){
				int i2=i, j2=j;
				bool found=true;
				REP(k, K){
					if(i2>=N or j2>=N or j2<0 or j2<0){
						found=false;
						break;
					}
					if(c[i2][j2]!=p){
						found=false;
						break;
					}
					i2+=dir[d][0];j2+=dir[d][1];
				}
				if(found){
					return true;
				}
			}
		}
	}
	return false;
}

void grav(){
	REP(i, N){
		int j2=N-1;
		bool found=true;
		vector<char> v;
		for(int j=N-1;j>=0;j--){
			while(j2>=0 and c[i][j2]=='.'){j2--;}
			if(j2<0)found=false;
			if(found){
				v.push_back(c[i][j2]);
			}else{
				v.push_back('.');
			}
			j2--;
		}
		assert((int)v.size()==N);
		REP(j, N){
			c[i][j]=v[N-1-j];
		}
	}
}

int main() {
	cin>>T;
	REP(ct, T){
		cin>>N>>K;
		init();
		REP(i, N){
			REP(j, N){
				cin>>c[i][j];
			}
		}
		grav();
		//		print();
		bool R=can_win('R'), B=can_win('B');
//		print();
		printf("Case #%d: ", ct+1);
		if(R and B)cout<<"Both";
		else if(R)cout<<"Red";
		else if(B)cout<<"Blue";
		else cout<<"Neither";
		cout<<endl;
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
