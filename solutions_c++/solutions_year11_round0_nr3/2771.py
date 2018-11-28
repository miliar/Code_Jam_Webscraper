#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <cmath>
#include <sstream>
#include <memory.h>
     
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i, a) for(int i=0; i<(int)a.size(); i++)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define sz size()
#define VI vector< int >
#define VS vector< string >
#define PII pair< int,int >
#define PDD pair< double,double >
#define PIS pair< int, string >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pi 3.1415926535897932384626433832795
const int inf=500*1000*1000;
#define eps 1e-6
#define ll long long
using namespace std;


int main(){
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

	int T, xor, c, n, mm;
	long long sum;

	cin>>T;

	forn(q, T){
		cin>>n;

		xor=sum=0;
		mm=inf;
		forn(i, n){
			cin>>c;
			mm=min(mm, c);
			sum+=c;
			xor^=c;
		}
		
		sum-=mm;
		
		cout<<"Case #"<<q+1<<": ";
		if(xor!=0) cout<<"NO"<<endl;
		else cout<<sum<<endl;
		
	}



	return 0;
}