#include<iostream>
#include<stack>
#include<algorithm>
#include<vector>
#include<map>
#include<cstdlib>
#include<cstdio>
#include<sstream>
#include<string>
#include<cassert>
#include<iomanip>
#include<ctime>
#include<set>
#include<cstring>
#include<cmath>
#include<queue>
#include<cassert>
#define ull unsigned long long
#define MP make_pair
#define pb push_back
#ifndef INT_MAX
#define INT_MAX (1<<30)
#endif
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
int gcd(int a,int b){
	if(b==0)return a;
	else return gcd(b,a%b);
}
#define SMALL
//#define LARGE
int main() {
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		int N,pd,pg;
		cin>>N>>pd>>pg;
		cout<<"Case #"<<t<<": ";
		if((pg==0&&pd!=0)||(pg==100&&pd!=100))cout<<"Broken"<<endl;
		else {
			int tmp=100/gcd(pd,100);
			if(tmp<=N)cout<<"Possible"<<endl;
			else cout<<"Broken"<<endl;
		}
	}
	return 0;
}
