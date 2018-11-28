/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

typedef long long ll;
typedef unsigned long long ull;

int main(int argc,char **argv){
        int no;
        scanf(" %d",&no);
        int tc,i;
        for(i=1;i<=no;i++){
                printf("Case #%d: ",i);
                int pd,pg;
                long long N;
                scanf(" %lld %d %d",&N,&pd,&pg);
                if((pd<100) and (pg==100)) printf("Broken\n");
                else {
                    int j;
                    int twos=0,fives=0;
                    int x=pd;
                    if((pd==0)) {
                            printf("Possible\n"); continue;
                    }
                    while((x%2)==0) twos++,x/=2;
                    x=pd;
                    while((x%5)==0) fives++,x/=5;
                    int n5=2-min(2,fives);
                    int n2=2-min(2,twos);
                    int days=1;
                    while(n5--) days*=5;
                    while(n2--) days*=2;
                    if((pd>0) and (pg==0)){ printf("Broken\n"); continue; }
                    if(days<=N){
                        printf("Possible\n");

                    } else 
                    {
                            printf("Broken\n");
                    }


                       
                    
                }
        }
        return 0;
}


