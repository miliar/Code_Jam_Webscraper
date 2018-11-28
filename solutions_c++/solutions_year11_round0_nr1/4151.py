#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <vector>
#include <sstream>
#include <iostream>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>


#define print1(a) cout<<a<<endl
#define print2(a,b) cout<<a<<" "<<b<<endl
#define print3(a,b,c) cout<<a<<" "<<b<<" "<<endl
#define PI (2*acos(0))
#define ERR 1e-5
#define ll long long
#define VI vector<int>
#define mem(a,b) memset(a,b,sizeof a)
#define pb push_back
#define popb pop_back

using namespace std;

struct data
{
    char id;
    int pos;
} ;
queue<int>o;
queue<int>b;

vector<data>v;

bool task_complete(int orange,int blue,char who,int move_to)
{
    if(who=='O')
    {
        if(move_to==orange) return true;
        else return false;
    }
    else
    {
        if(move_to==blue) return true;
        else   return false;
    }
}

int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int loop,butn,i,val,tm,indx,orange,blue,top,cas=0;
    char ch;
    bool flag;
    char who;

    data tmp;
    scanf("%d",&loop);
    while(loop--)
    {

        while(!o.empty()) o.pop();
        while(!b.empty()) b.pop();
        v.clear();


        scanf("%d ",&butn);
        for(i=0;i<butn;i++)
        {
//            scanf("%c %d ",&ch,&val);
            cin>>ch>>val;

//            print2(ch,val);
            tmp.id=ch;
            tmp.pos=val;

            v.pb(tmp);

            if(ch=='O') o.push(val);
            else b.push(val);
        }
//        puts("new");
//        for(i=0;i<v.size();i++) print2(v[i].id,v[i].pos);

        indx=0;orange=1;blue=1;

        for(tm=1;indx<butn;tm++)
        {
            flag=0;
            if( task_complete(orange,blue,v[indx].id,v[indx].pos ) )
            {
                who=v[indx].id;
                indx++;
                flag=1;
            }

            if(who=='O' && flag) o.pop();
            else
            {
                if(!o.empty())
                {
                    top=o.front();
                    if(top>orange) orange+=1;
                    else if(top<orange) orange-=1;
                }
            }

            if(who=='B' && flag) b.pop();
            else
            {
                if(!b.empty())
                {
                    top=b.front();
                    if(top>blue) blue+=1;
                    else if(top<blue) blue-=1;
                }
            }
        }
//        cout<<"Case #"<<++cas<<": "<<tm-1<<endl;
        printf("Case #%d: %d\n",++cas,tm-1);
    }

    return 0;
}

