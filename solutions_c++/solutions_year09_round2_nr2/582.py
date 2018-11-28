#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>
 
using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;


bool ismax(string num){
	string sorted = num, rsorted = num;
	sort(all(sorted));
	sort(all(rsorted));
	reverse(all(rsorted));
	if(num==rsorted) return true;
	return false;
}
string getnext(string num){
	if(num=="") return num;
	string sorted = num, rsorted = num;
	sort(all(sorted));
	sort(all(rsorted));
	reverse(all(rsorted));
	if(ismax(num)){
		return num;
	}else{
		
		string part = num.substr(1);
		string sol=getnext(part);
		int imin = -1;
		if(sol==part){//si la subparte es maxima
			FORE(i,1,SZ(num)) {
				if(imin==-1){
					if(num[i]>num[0]) imin=i;
				}
				else if(num[i]>num[0] && num[i]<num[imin]) imin=i;
			}
			sol=num[imin];
			string fin = "";
			REP(i,SZ(num))
				if(i!=imin)fin+=num[i];
			sort(all(fin));
			sol+=fin;
			return sol;
		} else return num[0]+sol;
	}
	return "";
}
void run1(int caso){

	string num;
	cin >> num;
	
	
	string sol = getnext(num);	
	if(sol==num){
		string sorted = num;
		sort(all(sorted));
		int ind = 0;
		while(sorted[ind]=='0') ind++;
		sol = sorted[ind];
		sol+='0';
		REP(i,SZ(sorted)) if(i!=ind) sol+=sorted[i];
				
	}
	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}