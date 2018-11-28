#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)
int ABS(int a)
{
    if(a<0)return -a;
    return a;
}
int main()
{
    int cn=1,t,n;
    freopen("input.txt","r",stdin);
    freopen("outputA.txt","w",stdout);
	cin>>t;
	while(t--)
	{
        cin>>n;
        int o=0,b=0,opos=1,bpos=1,x,i;
        string str;
        FOR(i,n)
        {
            cin>>str>>x;
            if(str=="O")
            {
                o=max(o+ABS(opos-x)+1,b+1);
                opos=x;
            }
            else if(str=="B")
            {
                b=max(b+ABS(bpos-x)+1,o+1);
                bpos=x;
            }

        }
        cout<<"Case #"<<cn++<<": "<<max(o,b)<<endl;
	}
	return 0;
}
