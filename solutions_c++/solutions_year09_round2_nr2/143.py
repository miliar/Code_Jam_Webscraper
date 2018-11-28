#include <algorithm>
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
#include <cmath>

#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define FILL(a) memset(&a,0,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,a) for (int i = 0; i < (int)(a); ++i)
typedef long long LL;

using namespace std;

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int tc;
	scanf("%d\n",&tc);
	REP(it,tc){
		printf("Case #%d: ", it+1);
		string s;
		getline(cin,s);
		if (next_permutation(ALL(s))){
			puts(s.c_str());
		}
		else{
			string d = s;
			REP(i,SIZE(d)){
				if (d[i] == '0'){
					d = d.erase(i,1);
					--i;
				}
			}
			sort(ALL(d));
			while (d.length() <= s.length()){
				d = d.insert(1, "0");
			}
			puts(d.c_str());
		}
	}
}
