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

int data[10010];
#define SMALL
//#define LARGE
int main() {
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif
	int Test;cin>>Test;
	for(int test=1;test<=Test;test++){
		int N,L,H;
		cin>>N>>L>>H;
		for(int i=0;i<N;i++){
			cin>>data[i];
		}
		cout<<"Case #"<<test<<": ";
		bool found=false;
		for(int k=L;k<=H;k++){
			bool flag=true;
			for(int i=0;i<N&&flag;i++){
				if(data[i]%k!=0&&k%data[i]!=0)flag=false;
			}
			if(flag){
				found=true;
				cout<<k<<endl;
				break;
			}
		}
		if(!found)cout<<"NO"<<endl;
	}
	return 0;
}
