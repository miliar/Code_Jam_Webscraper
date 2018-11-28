#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <list>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define rep2(i,x,m) for(int i=x;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
int oo = (int) 1e9;
int main() {
//#define SAMPLE
#ifndef SAMPLE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif
#ifdef SAMPLE
	freopen("a.txt", "rt", stdin);
#endif
	int N;
	cin>>N;
	string s;
	int mn,ind;
	rep(nn,N){
		cin>>s;
		for(int i=s.sz-1;i>=0;i--){
			mn=oo;
			ind=-1;
			for(int j=i+1;j<s.sz;j++)
				if(s[j]>s[i]){
					mn=s[j];
					ind=j;
				}
			if(ind!=-1){
				swap(s[i],s[ind]);
				sort(s.begin()+i+1,s.end());
				goto END;
			}
		}
		s+="0";
		mn=oo;
		ind=-1;
		rep(i,s.sz)
			if(s[i]<mn && s[i]!='0'){
				mn=s[i];
				ind=i;
			}
		swap(s[0],s[ind]);
		sort(s.begin()+1,s.end());
		END:;
		cout<<"Case #"<<nn+1<<": "<<s<<endl;
	}
	return 0;
}
