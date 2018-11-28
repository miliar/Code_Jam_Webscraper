#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
template <typename T> string tostr(const T& t) {
	ostringstream os;
	os << t;
	return os.str();
}
int main() {
	freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int n;
	string a;
	scanf("%d", &n);
	F(i, n) {
		cin>>a;
		string s = a, s2 = s;
		if(next_permutation(ALL(s))){
			cout<<"Case #"<<i+1<<": "<<s<<endl;
		}
		else{
			sort(ALL(s2));
			string aux;
			int ce = 0, it  =0;
			while(s2[it]=='0'){
				it++;
				aux.PB('0');
			}
			aux.PB('0');
			s = s2[it] + aux;
			it++;
			while(it<s2.S){
				s.PB(s2[it]);
				it++;
			}
			cout<<"Case #"<<i+1<<": "<<s<<endl;
		}
	}
	fclose(stdout);
	return 0;
}
