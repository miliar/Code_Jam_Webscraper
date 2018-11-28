#include <iostream>
#include <deque>
#include <cstdio>

using namespace std;

struct node
{
    int id,btn;
}press[200];

int T,N;
deque<int> no,nb;

int iabs(int a,int b)
{
    return a>b?a-b:b-a;
}

int solv()
{
    int sum=0,now1=1,now2=1;
    int tmp,next;
    for(int i=0;i<N;i++)
    {
        if(press[i].id==1)
        {
            tmp=iabs(press[i].btn,now1)+1;
            sum+=tmp;
            now1=press[i].btn;
            no.pop_front();
            next = nb.empty()? 100 : nb.front();
            if(next>=now2)
            {
                if(now2+tmp>=next)
                {
                    now2=next;
                }
                else
                {
                    now2+=tmp;
                }
            }
            else
            {
                if(now2-tmp<=next)
                {
                    now2=next;
                }
                else
                {
                    now2-=tmp;
                }
            }
        }
        else
        {
            tmp=iabs(press[i].btn,now2)+1;
            sum+=tmp;
            now2=press[i].btn;
            nb.pop_front();
            next= no.empty()? 100 : no.front();
            if(next>=now1)
            {
                if(now1+tmp>=next)
                {
                    now1=next;
                }
                else
                {
                    now1+=tmp;
                }
            }
            else
            {
                if(now1-tmp<=next)
                {
                    now1=next;
                }
                else
                {
                    now1-=tmp;
                }
            }
        }
    }
    return sum;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    for(int cnt=1;cnt<=T;cnt++)
    {
        no.clear();
        nb.clear();
        cin>>N;
        for(int i=0;i<N;i++)
        {
            char tmp;
            int num;
            cin>>tmp>>num;
            press[i].btn=num;
            if(tmp=='O')
            {
                press[i].id=1;
                no.push_back(num);
            }
            else
            {
                press[i].id=2;
                nb.push_back(num);
            }
        }
        printf("Case #%d: %d\n",cnt,solv());
    }
    return 0;
}
