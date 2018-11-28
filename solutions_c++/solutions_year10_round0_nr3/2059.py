#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)


typedef long long int LL;

int main() {
    freopen("C-large.in","r",stdin);
       freopen("C-large.out","w",stdout);
   // freopen("i","r",stdin);

    int t;
    cin>>t;
    FOR(test,1,t+1) {
        cout<<"Case #"<<test<<": ";
        LL r,k,n;
        LL arr[2005];

        cin>>r>>k>>n;

        FOR(i,0,n) {
            cin>>arr[i];
            arr[i+n]=arr[i];
        }

        int con[2002];
        LL total[2002];
        int next[2002];
        SET(con,0);
        SET(total,0);
        FOR(i,0,n) {
            int lastindex;
            FOR(j,i,i+n) {
                if (total[i]+arr[j]<=k) {
                    total[i]+=arr[j];

                } else {

                    break;
                }
                lastindex=j;
            }
            int index=lastindex+1;
            if (index>=n) {
                index-=n;
            }
            next[i]=index;
            //   cout<<i<<" "<<total[i]<<" "<<index<<endl;

        }

        LL cyclelength=0,cyclecost=0,curr=0;
        int startind;
        while (1) {
            if (!con[curr]) {
                con[curr]=1;
                curr=next[curr];
            } else {
                startind=curr;
                break;
            }
        }
        curr=startind;
        SET(con,0);
        while (1) {
            if (!con[curr]) {
                cyclecost+=total[curr];
                con[curr]=1;
                cyclelength++;
                curr=next[curr];
            } else {
                break;
            }
        }
        // cout<<cyclelength<<" "<<cyclecost<<" + "<<startind<<endl;
        //  return 0;
        int c=0;
        LL R=r;
        LL net=0;

        while (c!=startind && R) {
            net+=total[c];
            c=next[c];
            R--;
        }


        LL coeff=R/cyclelength;

        net+=coeff*cyclecost;

        LL rem=R-cyclelength*coeff;

        LL add=0;
        c=startind;
        FOR(i,0,rem) {
            add+=total[c];
            c=next[c];
        }
        net+=add;

        cout<<net<<endl;
    }


    return 0;
}
