#include<iostream>
#include<vector>
#include<string.h>
#include<stdio.h>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<math.h>
#include<limits.h>
using namespace std;
#define FOR(i,a,b) for(i = (a); i < (b); i++)
#define RFOR(i,a,b)for(i = (b); i >= (a); i--)
#define FORI(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(v) (v).size()
#define ll long long int
#define ii pair<int,int>
void f(int i){
	cout << "Case #" << i << ": ";
}
int main()

{
	//ios_base::sync_with_stdio(0);	
	int i,j,t,x;
	char c;
	int n;
	cin >> n;
	FOR(i,1,n+1){
		cin>>t;
		int a = 0 , b = 0;
		int p1 = 1 , p2 = 1;
		
		FOR(j,0,t){
			
			cin >> c >> x;

			if(c == 'O'){
				a += abs(p1 - x);
				a = max(a , b);
				a += 1;
				p1 = x;
			}
			else{
				b += abs(p2 - x);
				b = max(b , a);	
				b += 1;
				p2 = x;
			}
		}
		f(i); cout << max(a,b) << "\n";
	
	}
	return 0;
}
