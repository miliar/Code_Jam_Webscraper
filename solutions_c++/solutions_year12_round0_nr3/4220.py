#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <stack>
#include <utility>
#include <queue>

using namespace std;

#define CLR(_x) memset((_x),0,sizeof(_x))
#define all(_x) _x.begin(),_x.end()
#define pb push_back
#define mp make_pair
#define px first
#define py second

typedef long long ll;
typedef pair <int,int> point;

bool func(int x, int y){
	
	//1234 -> 4123
	
	int xx=x,yy=y,pow=1;
	int s1=0;
	while(xx>0){ s1++; xx/=10; pow*=10; }
	int s2=0;
	while(yy>0){ s2++; yy/=10; }
	
	if(s1!=s2) return 0;
	
	pow/=10;
	for(int i=0; i<s1; i++){
	  int tmp=x%10;
	  tmp=pow*tmp+x/10;
	  x=tmp;
	  if(x==y) return 1;
	}
	return 0;
}

int main(){
	
 	freopen("bsmall.in","r",stdin);	
	freopen("bsmall.out","w",stdout);
	
	int T,cases=1;
	cin>>T;
	
	while(T--){
	  int x,y;
	  cin>>x>>y;
	  
	  int ret=0;
	  for(int i=x; i<=y; i++)
	    for(int j=i+1; j<=y; j++)
	      if(func(i,j)) ret++;
	  
	  cout<<"Case #"<<cases++<<": "<<ret<<endl;
	}
	
	return 0;
}
