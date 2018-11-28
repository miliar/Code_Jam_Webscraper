#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const long long INF = 1LL<<62;
const int MAX = 10000000;
ifstream fin("A-small-attempt0.in");
ofstream fout("A-small.out");
int noCase;
typedef long long ll;
ll pow(int a,int b){
	if(b==0)return 1;
	return a*pow(a,b-1);
}
long long doit(string str,int base){
	set<char> s;
	REP(i,SIZE(str))s.insert(str[i]);
	if(SIZE(s)>base)return INF;
	vector<int> nums;
	REP(i,base)nums.push_back(i);
	map<char,int> m;
	m[str[0]] = nums[1];
	nums.erase(nums.begin()+1);
	for(int i=1;i<SIZE(str);i++){
		if(m.find(str[i])==m.end()){
			m[str[i]] = nums[0];
			nums.erase(nums.begin());
		}
	}
	ll ret = 0;
	int p = 0;
	for(int i=SIZE(str)-1;i>=0;i--){
		ret += m[str[i]]*pow(base,p);
		p++;
	}
	return ret;
}
int main() {
	fin>>noCase;
	for(int k=1;k<=noCase;k++){
		string str;
		fin>>str;
		ll ret = 1LL<<61;
		for(int base = 2;base<=10;base++){
			ret = min(ret,doit(str,base));
		}
		fout<<"Case #"<<k<<": "<<ret<<endl;
		
	}
    return 0;
}
