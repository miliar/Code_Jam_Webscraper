#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <map>

#pragma comment(linker, "/STACK:64000000")

using namespace std;

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int a[35];
	a[0]=0;
	for (int i=1;i<=30;i++){
		a[i]=(a[i-1]+1)*2-1;
	}
	int t,n,k;
	cin>>t;
	for (int z=0;z<t;z++){
		cout<<"Case #"<<z+1<<": ";
		cin>>n>>k;
		if ((a[n]<=k)&&(k%(a[n]+1)==a[n])){
			cout<<"ON";
		}
		else{
			cout<<"OFF";
		}
		cout<<endl;
	}
    return 0;
}