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
#define MAXV 10000
long long n, l, h;
long long fn[MAXV];
void doit(){
	bool fnd;
	cin>>n>>l>>h;
	for(int i=0;i<n;i++)cin>>fn[i];
	for(int i=l;i<=h;i++){
		fnd=true;
		for(int j=0;j<n;j++){
			if(fn[j]<=i && (i%fn[j])>0)fnd=false;
			if(fn[j]>i && (fn[j]%i)>0)fnd=false;
		}
		if(fnd){
			cout<<i<<endl;
			return;
		}
	}
	cout<<"NO"<<endl;
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

