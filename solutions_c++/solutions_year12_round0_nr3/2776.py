#include <iostream>
#include <vector>
#include <sstream>
#include <cstdlib>
#include <stdlib.h>
#include <algorithm>
#include <set>
using namespace std;
       
char str[20];
char rot[20];


typedef unsigned long ll;

set<pair<ll,ll> > pg;

char *rotate(char *,int);

char *rotate(char *strx,int count)
{
    int len=(int)strlen(strx);
    int ind=0;
    for(int i=count;i<len;i++) {
        rot[ind++]=strx[i];
    }
    for(int i=0;i<count;i++) {
        rot[ind++]=strx[i];
    }
    rot[ind]='\0';
    return &rot[0];
}
int main(int argc,char *argv[])
{
    int testCaseCount;
    cin >> testCaseCount;
    for(int testCase=1;testCase<=testCaseCount;testCase++)
    {
        pg.clear();
        ll min;
        ll max;
        cin >> min >> max;

        if(min>max) {
            swap(min,max);
        }

        for(ll i=min;i<=max;i++) {
            sprintf(str,"%lu",i);
            ll len=strlen(str);

            for(int r=1;r<len;r++) {
                char *rotated=rotate(str,r);
                ll n=atol(rotated);

                if((n>=min && n<=max) && (n!=i))
                {
                    if(i<n) {
                        pg.insert(pair<ll,ll>(i,n));
                    } else {
                        pg.insert(pair<ll,ll>(n,i));
                    }
                   
                }
            }
        }
        cout << "Case #"<< testCase << ": " << pg.size() << endl;
    }
    return 0;
}
