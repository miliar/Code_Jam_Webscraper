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
long long t,i,k,j,l,d,n,c,a[1000001],b[1000001],s,p,x;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(k=0;k<t;++k){
        cin>>l>>d>>n>>c;
        s=0;x=0;
        for(i=0;i<n;++i) b[i]=0;
        for(i=0;i<c;++i){
            cin>>a[i];
            s+=2*a[i];
            if (s-2*a[i]>=d || s==d) {b[x]=a[i]; x++;}
            else if (s-2*a[i]<d && s>d) {
                b[x]=a[i]-(d-(s-2*a[i]))/2; x++;}
        }
        j=c;
        while (j<n)
            for(i=0;i<c && j<n;++i,++j){
                a[j]=a[i];
                s+=2*a[i];
            if (s-2*a[i]>=d || s==d) {b[x]=a[i]; x++;}
            else if (s-2*a[i]<d && s>d) {b[x]=b[x]=a[i]-(d-(s-2*a[i]))/2; x++;}
            }
        sort(b,b+x);
        j=x-1; p=0;
        for(i=0;i<l;++i)  {p+=b[j];j--;}
        cout<<"Case #"<<k+1<<": ";
        cout<<s-p<<endl;
	}
	return 0;
}
