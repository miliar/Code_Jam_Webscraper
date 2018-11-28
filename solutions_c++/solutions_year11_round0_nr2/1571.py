// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
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

typedef long long Int;
typedef long long ll;
typedef long double ld;
// }}}

const int M=110;
int c,d,n;

char com[M][M],op[M][M];
int len[M];
char inv[M];

vector<char> v;

void clearq(){
	if(v.size()==0)return;
	REP(i,d){
		bool valid=true;
		REP(j,len[i]){
			char ch=op[i][j];
			bool found=false;
			REP(k,v.size()){
				if(ch==v[k]){
					found=true;
					break;
				}
			}
			if(not found){
				valid=false;
				break;
			}
		}
		if(not valid)continue;
		v.clear();
		return;
	}
}

void combq(){
	if(v.size()<=1)return;
	int s=v.size();
	char c1=v[s-1],c2=v[s-2];
	REP(i,c){
		if((c1==com[i][0] and c2==com[i][1])
				or (c1==com[i][1] and c2==com[i][0])){
			v.pop_back();v.pop_back();
			v.push_back(com[i][2]);
			break;
		}
	}
}

void main2(){
	v.clear();
	scanf("%d",&c);
	REP(i,c){
		scanf("%s",com[i]);
	}
	scanf("%d",&d);
	REP(i,d){
		scanf("%s",op[i]);
		len[i]=strlen(op[i]);
	}
	scanf("%d",&n);
	scanf("%s",inv);
	int l=strlen(inv);
	REP(i,l){
		v.push_back(inv[i]);
		combq();
		clearq();
	}
	putchar('[');
	REP(i,v.size()){
		putchar(v[i]);
		if(i!=v.size()-1){
			printf(", ");
		}
	}
	putchar(']');
	printf("\n");
}

int main() {
	int T;scanf("%d", &T);
	REP(ct, T){
		printf("Case #%d: ",ct+1);
		main2();
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

