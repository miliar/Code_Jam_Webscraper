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
int i,t,k,l,h,n,a[1001],fl,p,j;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    for(k=0;k<t;++k){
        cin>>n>>l>>h;
        for(i=0;i<n;++i)
            cin>>a[i];

        for(i=l;i<=h;++i){
            p=0; fl=0;

            for(j=0;j<n && !fl;++j)
                if (i%a[j]!=0 && a[j]%i!=0) {fl=1;break;}
                else p++;
            if (!fl && p==n) {h=i; break;}
        }
        cout<<"Case #"<<k+1<<": ";
        if (!fl) {cout<<h<<endl;}
        else cout<<"NO\n";
    }
	return 0;
}
