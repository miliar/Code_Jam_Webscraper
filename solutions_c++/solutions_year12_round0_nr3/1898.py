#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<list>
#include<queue>
#include<stack>
#include<cstdlib>
#include<sstream>

using namespace std;

int data[2000010];
int rot10[]={1,10,100,1000,10000,100000,1000000,10000000};

int fill(int a,int b)
{
    set<pair<int,int> > dump;

    for(int i=a;i<=b;i++)
    {
        int num =i;
        int digit=0;
        while(num)
        {
            digit++;
            num /= 10;
        }

        for(int j=1;j<digit;j++)
        {
            num  =  i/rot10[j] + (i%rot10[j])*rot10[digit-j];
            if(i!=num && num>=a && num<=b)
            {
                dump.insert(make_pair(min(i,num),max(i,num)));
            }
        }
    }

    return dump.size();
}

int main()
{
    int t;
    scanf("%d",&t);
   // fill();
    for(int i=1; i<=t; i++)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d\n",i,fill(a,b));
    }

    return 0;
}



