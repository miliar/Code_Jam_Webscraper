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

int t,i,c,d,n,a[30],k,z,j;
char comb[101][10], opos[101][6],x,s[10001];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>t;
	for(i=0;i<t;++i){
        cin>>c;
        for(j=0;j<c;++j) cin>>comb[j];
        cin>>d;
        for(j=0;j<d;++j) cin>>opos[j];
        cin>>n;
        k=0;
        memset(a,0,sizeof(a));
        for(j=0;j<n;++j){
            cin>>x;
            a[x-65]++;
            s[k] = x;
            k++;

            for(z=0;z<c;++z)
                if ((comb[z][0] == s[k-2] && comb[z][1] == s[k-1]) || (comb[z][0] == s[k-1] && comb[z][1] == s[k-2])) {
                    a[s[k-1]-65]--;
                    a[s[k-2]-65]--;
                    k-=2;
                    s[k] = comb[z][2];
                    k++;
                    s[k]=0;
                    a[s[k-1]-65]++;

                     break;
                }

            for(z=0;z<d;++z)
                if (a[opos[z][0]-65] && a[opos[z][1]-65]) {
                   memset(a,0,sizeof(a));
                    k=0;
                    s[k]=0;
                    break;
                }
        }

        cout<<"Case #"<<i+1<<": [";
        for(z=0;z<k;++z) {
            cout<<s[z];
            if (z<k-1) cout<<", ";
        }
        cout<<"]\n";
	}
	return 0;
}
