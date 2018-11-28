#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

//BEGINTEMPLATE_BY_SCORPIOLIU
const double PI  = acos(-1.0);
const double EPS = 1e-11;
const double INF  = 1E200;

typedef long long int64;
typedef unsigned long long uint64;

typedef pair<int,int> ipair;
#define MP(X,Y) make_pair(X,Y)
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))

#define REP(i,a) for(int i=0;i<int(a);++i)
#define REP2(i,n,m) for(int i=n;i<(int)(m);++i)
#define FORE(it,a) for (typeof((a).begin()) it=(a).begin();it!=(a).end();++it)
#define ALL(a) (a).begin(),(a).end()
//ENDEMPLATE_BY_SCORPIOLIU

//Temp function list begine
inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < EPS)
		return 0;
	return a > b ? 1 : -1;
}
char alpha[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
int  T9[27]    = {2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999,0};
//Temp function list end

//#define SMALL
#define LARGE
int main()
{
#ifdef SMALL
    //ifstream fin("C-small-practice.in");ofstream fout("C-small-practice.out");
    ifstream fin("C-small-attempt0.in");ofstream fout("C-small-attempt0.out");
    //freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("C-large-practice.in");ofstream fout("C-large-practice.out");
    //ifstream fin("C-large.in");ofstream fout("C-large.out");
    freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
#endif
     int N;
    cin>>N;
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int64 r,k,n;
        scanf("%I64d",&r);scanf("%I64d",&k);scanf("%I64d",&n);
        int64 temp = 0;
        int64 count = 0;
        vector<int64>arr;
        REP(i,n)
        {
            cin>>temp;
            arr.push_back(temp);
        }
        temp = 0;
        int64 nsum = 0;
        FORE(it,arr) nsum+=(*it);
        if (nsum<=k)
        {
            printf("%I64d",r*nsum);cout<<endl;
            continue;
        }
        int nflag =0;
        for(vector<int64>::iterator it= arr.begin();it!=arr.end()-1;it++)
        {
            if (*it!=*(it+1))
            {nflag=1;break;}
        }
        if (nflag==0)
        {
            printf("%I64d",r*(k/arr[0])*arr[0]);cout<<endl;
            continue;
        }
        vector<int64>arr1;
        vector<int64>arr2;
        vector<int64>arr3;
        arr1.push_back(temp);

        int nflag2 = 0;
        int nflag3=0;
        int64 ntemp=0;
        int64 countsum=0;
        while(r--)
        {


            int64 counttemp = 0;
            int64 j;

            for(j=(temp%arr.size());arr[j]+counttemp<=k;j=(j+1)%arr.size())
            {
                    counttemp =counttemp+arr[j];
                    ntemp++;
            }
            temp=j;
            count = count + counttemp;


            if(find(ALL(arr1),temp)==arr1.end())
            {
                arr1.push_back(temp);
            }
            else
            {
                if(find(ALL(arr3),temp)==arr3.end())
                {
                    arr3.push_back(temp);
                    arr2.push_back(counttemp);
                }
                else{
                    nflag2 = 1;
                }

            }

            if (nflag2==1 && nflag3==0)
            {
                FORE(it,arr2) countsum+=(*it);
                nflag3 = 1;
                count = count+countsum*(r/arr3.size());
                r=r%arr3.size();
            }

        }
        //////////////////////////////////////
        printf("%I64d",count);
        cout<<endl;
    }


    return 0;
}
