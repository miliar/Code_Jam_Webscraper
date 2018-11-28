#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

#define REP(i,n) for(typeof(n) _n=n, i=0;i<_n;++i)
#define FOREACH(i,x) for(typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define ALL(x) (x).begin(),(x).end()
#define INFTY 1000000

using namespace std;

struct FU{
	long rank;
	long father;
};

vector<FU> fu;

long fu_find(long i){
	if (fu[i].father == -1)
		return i;
	else{
		long result = fu_find(fu[i].father);
		fu[i].father = result;
		return result;
	}

}

void fu_union(long i, long j){
	if (i == j) return;
	if (fu[i].rank > fu[j].rank)
		fu[j].father = i;	
	else if (fu[j].rank > fu[i].rank)
		fu[i].father = j;
	else{
		fu[i].father = j;
		fu[j].rank++;	
	}
}

long long solveCase(){
	int a,b,p;
	cin >> a >> b >> p;
	
	fu = vector<FU>(b-a+1);

	REP(i,fu.size()){
		fu[i].rank = 0;
		fu[i].father = -1;
	}

	for(long prime = p; prime <= b; prime++){
		bool ok = true;
		for(long i=2; i*i <= prime; i++)
			if (prime % i == 0){
				ok = false;
				break;
			}
		if (!ok) continue;
		for(long mul = a/prime; mul <= b/prime; mul++){
			if ( (prime*mul >= a) && (prime*(mul+1) <= b))
				fu_union(fu_find(prime*mul-a),fu_find( prime*(mul+1)-a));
		}
	}
	//REP(i,b-a+1)
	//	cout << fu[i].father << " ";
	set<long> s;
	REP(i,b-a+1)
		if(fu_find(i) == -1)
			s.insert(i);
		else
			s.insert(fu_find(i));
	return s.size();
}	

int main(){
	int cases;
	cin >> cases;
	REP(i,cases){
		cout << "Case #" << i+1 << ": ";
		cout << solveCase();
		cout << endl;
	}		
	return 0;
}
