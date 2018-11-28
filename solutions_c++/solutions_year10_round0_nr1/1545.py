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
	int n,k;
	int a[32];
	memset(a,0,sizeof(a));
	cin>>n>>k;
	a[1]=1;
	for(int i=2;i<32;i++)
		a[i]=a[i-1]*2+1;
	if(k<a[n])cout<<"OFF"<<endl;
	else{
		k-=a[n];
		if(k%(a[n]+1))cout<<"OFF"<<endl;
		else cout<<"ON"<<endl;
	}
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
