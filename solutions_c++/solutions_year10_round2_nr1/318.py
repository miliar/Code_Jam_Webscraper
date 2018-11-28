#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <sstream>
#include <cstring>
using namespace std;

#define FALL(ii,vv) for (int (ii)=0; (ii)<(vv).size();(ii)++)
#define REP(i,b) for(int (i)=(0);(i)<(b);(i)++)
#define FUP(i,a,b) for(int (i)=(a); (i)<=(b); (i)++)
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef vector<int> vi;
typedef long long ll;

vector<string> split(string a){
	FALL(i,a) if (a[i]=='/') a[i]=' ';
	stringstream aa(a);
	vector<string> res;
	string tmp;
	while(aa>>tmp){
		res.PB(tmp);
	}
	return res;
}

int compute(string a,string b){
	vector<string> A = split(a);
	vector<string> B = split(b);
	
	int i =0;
	while(i<A.size() && i<B.size() && A[i] == B[i]) i++;
	return int(B.size())-i;
}

char c[55555];

int main(){
	int test,n,m;
	scanf("%d",&test);
	FUP(ii,1,test){
		
		scanf("%d %d",&n,&m);
		vector<string> t; t.PB("");
		REP(i,n){
			scanf("%s",c);
			t.PB(c);
		}
		int res = 0;
		REP(i,m){
			scanf("%s",c);
			int ile = 1<<30;
			
			FALL(i,t) ile = min(ile, compute(t[i], c));
			
			t.PB(c);
			res+=ile;
		}
	

		printf("Case #%d: %d\n",ii,res);
	}
	return 0;
}
