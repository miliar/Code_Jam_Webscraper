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
vector<int> v;

inline bool can(double t,int D){

    int i;
    double left=v[0]-t;
//    printf("%.2f,%d\n",t,D);
    for(i=1;i<v.size();i++) 
    {
 //       printf("i=%.2f\n",left);
        
        left=left +D;
  //      printf("%.2f,%d,i=%d\n",left,v[i],i);

        //
        // 1,3
        //
        //
        if(v[i]>left) 
        {
                if(v[i]-t>left) left=v[i]-t;
        }
        else {
                if(v[i]+t<left) return false;      
        }
        
    }
   // printf("RETURNING TRUE\n");
    return true;

}

int main(int argc,char **argv)
{
    int no,tc;
    scanf(" %d",&no);
    for(tc=1;tc<=no;tc++){
    int C,D;
    scanf(" %d %d",&C,&D);
    int i;
    v.clear();
    for(i=0;i<C;i++)
    {
            int x,y;
            scanf(" %d %d",&x,&y);
            while(y--) v.push_back(x);
    }
    sort(v.begin(),v.end());

    double low=0,high=1e18,mid=0;
    while(fabs(high-low)>1e-7){
        mid=(high+low)/2.;
        if(can(mid,D)) high=mid;
        else low=mid;
    }
    printf("Case #%d: ",tc);
    printf("%.6f\n",mid);
   }
    return 0;
}


