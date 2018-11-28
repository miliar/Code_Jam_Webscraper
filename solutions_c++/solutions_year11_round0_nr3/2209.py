#include <iostream>
#include <cstring>
#include <cmath>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <deque>
#include <queue>

#define min(a,b) (((a) < (b)) ? (a) : (b))
#define max(a,b) (((a) > (b)) ? (a) : (b))
using namespace std;
int t,n,i,j,a[10001],m,s,y,x;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>t;
	for(i=0;i<t;++i){
        cin>>n;
        m=1e9;
        s=0;
        for(j=0;j<n;++j){
            cin>>x;
            s+=x;
            if (j==0) y = x;
            else y^=x;
            if (x<m) m = x;
        }
        cout<<"Case #"<<i+1<<": ";
        if (y!=0)  cout<<"NO";
        else cout<<s-m;
        cout<<"\n";
	}
	return 0;
}
