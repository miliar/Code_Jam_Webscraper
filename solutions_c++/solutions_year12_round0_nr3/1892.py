#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

int a,b;
int GetCount(int num)
{
    int sum=0;
    map<int,bool> track;
    track.clear();
    char numstr[15];
    sprintf(numstr,"%d",num);
    int len = strlen(numstr);
    int rot;
    for(rot=0;rot<len-1;rot++)
    {
        char temp = numstr[len-1];
        int shifter;
        for(shifter=len-1;shifter>0;shifter--)
            numstr[shifter] = numstr[shifter-1];
        numstr[0] = temp;
        int newNum;
        sscanf(numstr,"%d",&newNum);
        if ( newNum >num && newNum <= b)
            if ( track[newNum] == false)
                sum++, track[newNum] = true;
    }
    return sum;
}
int main()
{
    //freopen("sample.in","r",stdin);

    freopen("c.in","r",stdin);
    freopen("c.ans","w",stdout);

    int kase=1;
    int test;
    sf("%d",&test);
    while ( test--)
    {

        sf("%d %d",&a,&b);
        int counter=0;
        int num;
        for(num=max(a,12);num<=b;num++)
        {
            counter+= GetCount(num);
        }
        pf("Case #%d: %d\n",kase++,counter);
    }
    return 0;
}
