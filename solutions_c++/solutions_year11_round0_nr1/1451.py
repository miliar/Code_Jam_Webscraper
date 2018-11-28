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

void doit(){
	int pt[2],pp[2],n,np,ret=0,ctime=0,diff,rtime;
	string s;
	pt[0]=pt[1]=0;pp[0]=pp[1]=1;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>s>>np;
		if(s=="O"){
			diff=ctime-pt[0];
			rtime=abs(pp[0]-np);
			if(rtime>diff)ret+=(rtime-diff);
			ret++;
			ctime=ret;
			pt[0]=ret;pp[0]=np;
		}
		else{
			diff=ctime-pt[1];
			rtime=abs(pp[1]-np);
			if(rtime>diff)ret+=(rtime-diff);
			ret++;
			ctime=ret;
			pt[1]=ret;pp[1]=np;
		}
	}
	cout<<ret<<endl;
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

