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
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

	int T, n;
	int ot, bt, op, bp, p;
	char ch;

	cin>>T;

	forn(q, T){
		cin>>n;

		op=bp=1;
		ot=bt=0;

		forn(i, n){
			cin>>ch>>p;

			if(ch=='O'){
				ot+=abs(op-p)+1;
				op=p;
				if(ot<=bt) ot=bt+1;
			}
			else{
				bt+=abs(bp-p)+1;
				bp=p;

				if(bt<=ot) bt=ot+1;
			}
		}

		cout<<"Case #"<<q+1<<": "<<max(bt, ot)<<endl;
	}



	return 0;
}