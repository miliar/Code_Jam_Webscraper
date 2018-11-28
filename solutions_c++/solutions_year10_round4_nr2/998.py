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
#include <stdlib.h>
#include <ctime>
#include <fstream>

using namespace std;

int ans,P,K,a[2058];
int work(int x,int y);
int main() {
	freopen("f:\\b-small.in","r",stdin); freopen("f:\\b-small.out","w",stdout);
	//freopen("f:\\a-large.in","r",stdin); freopen("f:\\a-large.out","w",stdout);
	int t,ans;
	cin>>t;
	for(int j=1;j<=t;j++){
		cout<<"Case #"<<j<<": ";
		cin>>P;
		K=1<<P;
		for(int i=0;i<K;i++) {
			cin>>a[i];
			a[i]=P-a[i];
		}
		int temp;
		for(int i=0;i<K-1;i++) {
			cin>>temp;
		}
		cout<<work(0,K)<<endl;
	}
}
int work(int x,int y) 
{
	if(y-x==2) {
		if(a[x] == 1 || a[y-1] ==1) return 1;
		else return 0;
	}
	int flag = true;
	for(int i=x;i<y;i++) {
		if( a[i]>0 ) {
			flag = false;
		}
	}
	if(flag) return 0;
	int m=x+y;
	m=m/2;
	for(int i=x;i<y;i++) if(a[i]>0) a[i]-=1;
	return 1+work(x,m)+work(m,y);
}