#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>
#include <sstream>
#include <fstream>
#include <map>
#include <algorithm>
#define sqr(a) (a*a)
#define pb push_back
#define fs first
#define sd second
#define debug(a) cout<<#a<<" = "<<a<<endl;
#define all(a) a.begin(),a.end()
#define forn(i,n) for(int i=0;i<n;i++)
using namespace std;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;

const double EPS=1E-10;

void dbgVint(vector <int> a){
	for (int i=0;i<a.size();i++){
		printf("%d ",a[i]);
	}
	printf("\n");
}

void dbgVvint(vector <vector <int> > a){
	for (int i=0;i<a.size();i++){
		dbgVint(a[i]);
	}
}

void dbgVstr(vector <string> a){
	for (int i=0;i<a.size();i++){
		printf("%s\n",a[i].data());
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n,k;
	int t;
	cin >> t;
	for (int i=0;i<t;i++){
		cin >> n >> k;
		k=k%(1<<n);
		printf("Case #%d: ",i+1);
		if (k==(1<<n)-1) cout <<"ON" << endl; else cout << "OFF" << endl;
	}
	
	return 0;
}

