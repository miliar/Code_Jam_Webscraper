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
#define rp(i,a,b) for(int i = (a); i < (b); i++)
#define rrp(i,a,b) for(int i = (b); i >= (a); i--)
#define ri(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define C(x,with) memset(x,with,sizeof(x))
#define S(v) (v).size()
#define ll long long int
#define ii pair<int,int>

void op(int t){
	cout << "Case #" << t << ": ";
}

int main()

{

	int _test;
	cin >> _test;
	int a[100000];
	rp(_t,1,_test+1){
		op(_t);
	
		int n,l,h;
		cin >> n>>l>>h;
		rp(i,0,n)	cin>>a[i];
		int ok=0;
		rp(i,l,h+1){
			bool b=1;
			rp(j,0,n)
				if(!((a[j]%i==0)||(i%a[j]==0)))
					b=0;
			if(b){
				ok = i;	
				break;
			}
		}
		if(ok)
			cout << ok << "\n";
		else	cout << "NO\n";


	}


	return 0;
}
