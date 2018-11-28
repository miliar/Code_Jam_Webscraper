#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

#define GCDTYP long long //fill type here

GCDTYP gcd(GCDTYP a, GCDTYP b){
  if(b==0)return a;
  return gcd(b,a%b);
}


void doit(){
	int n, pd, pg;
	int gd, gg, md, mg;
	cin>>n>>pd>>pg;
	gd=gcd(pd,100);
	md=100/gd;
	gg=gcd(pg,100);
	mg=100/gg;
	if(md>n){
		cout<<"Broken"<<endl;
		return;
	}
	if(pg==100 && pd<100){
		cout<<"Broken"<<endl;
		return;
	}
	if(pg==0 && pd>0){
		cout<<"Broken"<<endl;
		return;
	}
	cout<<"Possible"<<endl;
	return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}

