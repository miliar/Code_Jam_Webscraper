#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair

typedef long long ll;
int main(){
	int T;
	cin>>T;
	REP(i,T){
		int r,c;
		cin>>r>>c;
		char arr[r][c+1];
		REP(j,r)  cin>>arr[j];
		bool ok=true;
		for(int j=1;j<r;j++){
			for(int k=0;k<c;k++){
				if(arr[j][k] == '#' && arr[j][k+1] == '#' && arr[j-1][k] == '#' && arr[j-1][k+1] == '#'){
					arr[j-1][k] = '/';arr[j][k+1] = '/';
					arr[j-1][k+1] = '\\'; arr[j][k] = '\\';
					k++;
					}
				}			
			}
		REP(j,r) REP(k,c) if(arr[j][k] == '#') {
			ok = false;
			break;
			}
		cout<<"Case #"<<i+1<<":"<<endl;
		if(!ok)
			cout<<"Impossible"<<endl;
		else{
			REP(j,r) cout<<arr[j]<<endl;
			}
		}	
	}