#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long		ui64;
typedef long long				i64;
typedef	vector<int>				vi;
typedef	vector<string>			vs;
typedef	pair<int,int>			pii;
typedef	pair<double,double>		point;

#define pb						push_back
#define mp						make_pair
#define X						first
#define Y						second
#define all(a)					(a).begin(), (a).end()
#define INF						(2000000000)


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests; cin >> tests;
	int testsK = tests;
	for(;tests;tests--){

		int n;
		cin >> n;
		vs done;
		for(int i=0;i<n;i++){
			string s;
			cin >> s;
			done.pb(s);
		}
		vs clr;
		cin >> n;
		for(int i=0;i<n;i++){
			string s;
			cin >> s;
			clr.pb(s);
		}
		cin >> n;
		char a[110];
		int it = 0;
		for(;n;n--){
			char ch;
			cin >> ch;
			if(!it){
				a[it] = ch;
				it++;
				continue;
			}

			char nw = '.';
			for(int i=0;i<(int)done.size();i++)
				if( (done[i][0]==a[it-1] && done[i][1]==ch) || (done[i][1]==a[it-1] && done[i][0]==ch) )
					nw = done[i][2];

			bool bx = false;
			for(int i=0;i<(int)clr.size();i++)
				for(int j=0;j<it;j++)		
					if( (clr[i][0]==a[j] && clr[i][1]==ch) || (clr[i][1]==a[j] && clr[i][0]==ch) )
						bx = true;
		
		
			if(nw!='.'){
				a[it-1] = nw;
				continue;
			}

			if(bx){
				it=0;
				continue;
			}

			a[it] = ch;
			it++;

			
			

		}
		cout << "Case #" << testsK-tests+1 << ": [";
		
		for(int i = 0;i<it-1;i++)
			cout << a[i] << ", ";
		if(it)
			cout << a[it-1];
		cout << "]\n";

	}
	return 0;
}