#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/

int test, a[1002],n,s,p;
int main(){
    FILE *f = fopen("input.txt","r");
    fscanf(f,"%d", &test);
    for (int cas=1;cas<=test;cas++){
        int ret=0;
        vector<int> cur ;
        fscanf(f,"%d %d %d",&n,&s,&p);
        For(i,0,n){
            fscanf(f,"%d",&a[i]);
            if (a[i]%3==2){
                cur.pb(a[i]);
            } else{

                if (a[i]%3==0){
                    if (a[i]/3 >=p){
                        ret++;
                        continue;

                    }
                    if (a[i]>0 && a[i]/3 +1 >=p && s>0){
                        s--;
                        ret++;
                        continue;
                    }

                } else{
                    if (a[i]/3 + 1 >=p){
                        ret++;
                        continue;
                    }



                }

            }
        }
        For(i,0,cur.size()){
            if (cur[i]/3 +1 >=p){
                ret++;
                continue;
            }
            if (cur[i]/3 +2 ==p && s>0){
                s--;
                ret++;
                continue;
            }

        }
        printf("Case #%d: %d\n",cas,ret);


    }
    return 0;
}
