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
    int tc=1,i,no,n;
    scanf(" %d",&no);

    for(tc=1;tc<=no;tc++){
        scanf(" %d",&n);
        int cnt=0;
        for(i=1;i<=n;i++){
                int x;
                scanf(" %d",&x);
                if(x!=i) cnt++;
        }
        printf("Case #%d: %.6f\n",tc,(double)cnt);
    }
        return 0;
}


