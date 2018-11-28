#include <stdio.h>
#include <utility>
#include <iostream>
#include <string>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <queue>
#include <sstream>
#include <vector>
#include <stack>


using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define FORN(i,x,y) for(i=x;i<y;++i)
#define FOR(i,x) FORN(i,0,x)
#define MP make_pair
#define PB push_back
#define FOREACH(it,vec) for(typeof(vec.begin()) it=vec.begin();it != vec.end();it++)
#define SET(x,a) memset(x,a,sizeof x)
#define FIR first
#define SEC second
#define ALL(x) x.begin(),x.end()
#define vi vector<int >
#define vvi vector<vi >
#define VS vector<string >
#define checkmax(a,b) a=max(a,b)
#define checkmin(a,b) a=min(a,b)

int sol(int x,int y){
	if(x<y)swap(x,y);
	if(y==0)return true;
	if(!sol(y,x%y))return true;
	if(x == y+(x%y))return false;
	return true;
}

int main(){
	int cas,it;
	cin>>cas;
	FOR(it,cas){
		int a1,a2,b1,b2;
		cin>>a1>>a2>>b1>>b2;
		int ret=0,i,j;
		FORN(i,a1,a2+1)FORN(j,b1,b2+1)
			ret+=sol(i,j);
		cout<<"Case #"<<(it+1)<<": "<<ret<<endl;
	}
	return 0;
}
