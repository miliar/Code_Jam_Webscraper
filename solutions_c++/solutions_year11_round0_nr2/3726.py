/*  
	NAME:
	PROG:
	LANG:C++
*/

#define REP(_i_,_a_) for(unsigned int _i_ = 0,_X_ = _a_;_i_ < _X_;_i_++)
#define FOR(_i_,_a_,_b_) for(int _i_ = _a_,_X_ = _b_;_i_ <= _X_;_i_++)
#define FORD(_i_,_a_,_b_) for(int _i_ = _a_,_X_ = _b_;_i_ >= _X_;_i_--)
#define FE(_i_,_a_) for(__typeof(_a_.begin()) _i_ = _a_.begin();_i_ != _a_.end();_i_++)
#define LOOP for(;;)

#define iofile(_a_,_b_) freopen(_a_,"r",stdin);freopen(_b_,"w",stdout)
#define ioclose fclose(stdin);fclose(stdout)
#define isOn(_x_,_i_) (bool)((1<<_i_)&_x_)

#define mp make_pair
#define pb push_back
#define fi first
#define se second

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>

#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <list>
#include <algorithm>
#include <utility>
#include <iostream>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;

inline void solve(int tc){
	int N,n1,n2;
	map<string,char> jenis1;
	set<char> jenis2;
	map<char,char> jenis22;
	string input;
	vector<char> hasil;
	map<char,int> ditunggu;
	
	scanf("%d",&n1);
	REP(i,n1){
		char tmp[5];
		scanf("%s",tmp);
		tmp[3] = 0;tmp[4] = 0;
		swap(tmp[2],tmp[3]);
		jenis1[tmp] = tmp[3];
		swap(tmp[0],tmp[1]);
		jenis1[tmp] = tmp[3];
	}
	
	scanf("%d",&n2);
	REP(i,n2){
		char tmp[5];
		scanf("%s",tmp);
		jenis2.insert(tmp[0]);
		jenis2.insert(tmp[1]);
		jenis22[tmp[0]] = tmp[1];
		jenis22[tmp[1]] = tmp[0];
	}
	
	scanf("%d",&N);
	cin >> input;
	
	REP(i,input.size()){
		char in = input[i];
		if(hasil.size() == 0){
			hasil.pb(in);
			if(jenis2.find(in) != jenis2.end()){
				ditunggu[jenis22[in]]++;
			}
		} else {
			char tmp[3];
			tmp[0] = hasil.back();
			tmp[1] = in;
			tmp[2] = 0;
			map<string,char>::iterator it = jenis1.find(tmp);
			if(it != jenis1.end()){
				map<char,char>::iterator it2 = jenis22.find(hasil.back());
				char x = it2!=jenis22.end()?it2->se:0;
				if(x != 0){
					map<char,int>::iterator it2 = ditunggu.find(x);
					(it2->se)--;
					if(it2->se == 0) ditunggu.erase(it2);
				}
				hasil.pop_back();
				hasil.pb(it->se);
			} else {
				if(ditunggu.find(in) != ditunggu.end()){
					ditunggu.clear();
					hasil.clear();
				} else {
					if(jenis2.find(in) != jenis2.end()){
						ditunggu[jenis22[in]]++;
					}
					hasil.pb(in);
				}
			}
		}
	}
	
	printf("Case #%d: [",tc);
	REP(i,hasil.size()){
		if(i > 0) printf(", ");
		printf("%c",hasil[i]);
	}
	printf("]\n");
	
}


int main(){
	int tc;scanf("%d",&tc);
	int x = tc;
	while(tc--){
		solve(x - tc);
	}
	return 0;
}
