#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <math.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string.h>
typedef long long ll;

#define inf         99999999
#define SZ          1000000
#define LD          long double
#define VS          vector<string>
#define VI          vector<int>
#define VD          vector<double>
#define VLL         vector<ll>
#define pb          push_back
#define pi          2*acos(0)
#define sz          size()
#define mem(a,b)    memset(a,b,sizeof(a))
#define two(i)      (1<<i)
using namespace std;
typedef struct
{
   ll a,b;
}Ind;
//Ind ar[1000];
//ll ax[]={1,0,-1,0};ll ay[]={0,1,0,-1}; //4 Direction
//int ax[]={1,1,0,-1,-1,-1,0,1};int ay[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int ax[]={2,1,-1,-2,-2,-1,1,2};int ay[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int ax[]={2,1,-1,-2,-1,1};int ay[]={0,1,1,0,-1,-1}; //Hexagonal Direction
//ll month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

ll test,sum,ans,n,i,pos,Orange,Blue,posOrange,posBlue,diff,kase;
char ch;
string str;

int main()
{

    ios_base::sync_with_stdio(false);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin>>test;
    while(test--)
    {
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>ch;
            cin>>pos;
            if(!i)
            {
                sum=pos;
                if(ch=='O')
                {
                    diff=pos;
                    posOrange=pos;
                    posBlue=1;
                    Orange=1;
                    Blue=0;
                }
                else
                {
                    diff=pos;
                    posBlue=pos;
                    posOrange=1;
                    Orange=0;
                    Blue=1;
                }
            }
            else
            {
                if(ch=='O' && Orange==1)
                {
                    sum+=abs(posOrange-pos)+1;
                    diff+=abs(posOrange-pos)+1;
                    Orange=1;
                    Blue=0;
                    posOrange=pos;
                }
                else if(ch=='B' && Blue==1)
                {
                    sum+=abs(posBlue-pos)+1;
                    diff+=abs(posBlue-pos)+1;
                    Orange=0;
                    Blue=1;
                    posBlue=pos;
                }
                else
                {
                    if(ch=='O' && Blue==1)
                    {
                        diff=abs(posOrange-pos)+1-diff;
                        diff=max(diff,1LL);
                        sum+=diff;
                        Orange=1;
                        Blue=0;
                        posOrange=pos;
                    }
                    else
                    {
                        diff=abs(posBlue-pos)+1-diff;
                        diff=max(diff,1LL);
                        sum+=diff;
                        Orange=0;
                        Blue=1;
                        posBlue=pos;
                    }
                }

            }
        }
        cout<<"Case #"<<++kase<<": "<<sum<<endl;
    }
    return 0;
}
