#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>


using namespace std;



vector<int> move(int a)
{
    vector<int> ret;

    int i , j ;
    int num = 1;
    int t = a ;
    char str[1000];
    sprintf(str,"%d",a);

    int len = strlen(str);
    for(i = 1 ; i < len ; i++)
    {
        char s2[1000] = "";

        for(j = 0 ; j < len-i ; j++)
        {
            s2[j]=str[i+j];
        }
        int k = 0 ;
        for(j = len-i ;  j < len ; j++)
        {
            s2[j] = str[0+k];

            k++;
        }

 //       puts(s2);
        int rr ;
        sscanf(s2,"%d",&rr);
        ret.push_back(rr);
    }
    return ret;
}



int main()
{
    int T;
    int tt = 0;
//    move(12345);
   // v = move(12345);
   // for(int i = 0 ; i < v.size() ; i++)
   //     printf("%d\n",v[i]);

    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&T);//'!=EOF)
    while(T--)
    {
        int a , b ;
        scanf("%d%d",&a,&b);
        int i , j ;

        printf("Case #%d: ",++tt);
        int cnt = 0;

        pair<int,int> pp;
        set< pair<int,int> > ss;
        for(i = a ; i <= b; i++)
        {
            vector<int> v;
            v = move(i);
            char zz[1000];
            sprintf(zz,"%d",i);

            for(j = 0 ; j < v.size() ; j++)
            {
                char zero[1000] ;
                sprintf(zero,"%d",v[j]);
                int ll1 = strlen(zero) ,ll2 = strlen(zz);
                if(v[j] >= a && v[j] <= b && v[j] > i && ll1 == ll2)
                {
                    //printf("%d %d\n",i,v[j]);
                    //cnt++;
                    pp = make_pair(i,v[j]);
                    ss.insert(pp);
                }
            }
        }
        printf("%d\n",ss.size());
    }
    return 0;
}

