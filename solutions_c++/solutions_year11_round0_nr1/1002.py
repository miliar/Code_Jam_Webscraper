#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

int main(){
	int casos,cc;
	cin>>casos;
	
	int lastO,lastB,time,Otime,Btime;
	for (cc=0;cc<casos;cc++) {
		lastO=lastB=1;
		Otime=Btime=time=0;
		int n, pos;
		cin>>n;
		char ro;
		for (int i=0;i<n;i++) {
			cin>>ro>>pos;
			if (ro=='O') {
				time=1+max(abs(pos-lastO)+Otime, time);
				Otime=time;
				lastO=pos;
			} else {
				time=1+max(abs(pos-lastB)+Btime, time);
				Btime=time;
				lastB=pos;
			}
		}
		cout<<"Case #"<<cc+1<<": "<<time<<endl;
		
	}
	return 0;
}
