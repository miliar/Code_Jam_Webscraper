#include <iostream>
#include <algorithm>
using namespace std;
typedef struct train
{
    int begin;
    int end;
    int from;
    bool used;
};
train a[1000];
bool cmp1(train a,train b)
{
    if(a.begin<b.begin)return true;
    else if(a.begin==b.begin)
    return a.end<b.end;
    return false;
}

int main()
{
    int n;
    int T;
    int tp1,tp2;
    while(cin>>n)
    {
        for(int c=0;c<n;c++)
        {
        cin>>T;
        memset(a,0,sizeof(a));
        cin>>tp1>>tp2;
        for(int i=0,tp3=0,tp4=0,tp5=0,tp6=0;i<tp1+tp2;i++)
        {
            scanf("%d:%d %d:%d",&tp3,&tp4,&tp5,&tp6);
            tp3=tp3*60+tp4;
            tp5=tp5*60+tp6;
            a[i].begin=tp3;
            a[i].end=tp5;
            if(i<tp1)
            a[i].from=0;
            else
            a[i].from=1;
        }
        sort(a,a+tp1+tp2,cmp1);
        int i=0;
        int curvalue=0;
        int flag=0;
        int k=0;
        int count1=0;
        int count2=0;
        for(int i=0;i<tp1+tp2;i++)
        {
            if(a[i].used==0)
            {
                curvalue=a[i].end;
                if(a[i].from==0)
                count1++;
                else if(a[i].from==1)
                count2++;
                flag=a[i].from;
                for(int j=i+1;j<tp1+tp2;j++)
                {
                    if(a[j].begin-curvalue>=T&&a[j].used==false&&a[j].from!=flag)
                    {
                        curvalue=a[j].end;
                        a[j].used=true;
                        flag=a[j].from;
                        
                    }
                }               
                a[i].used==true;
            }
        }
        printf("Case #%d: %d %d\n",c+1,count1,count2);
       }
    }
}
