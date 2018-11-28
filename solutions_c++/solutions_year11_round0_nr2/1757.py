#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<list>
using namespace std;
int q[201][201];
int o[201][201];
int idxa;
list<int> l;
list<int> :: iterator it;
list<int> :: iterator it1;
main()
{
    freopen("B-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int t;
    char a1,a2,a3;
    int st,ed;
    char in[5];
    char str[201];
    scanf("%d",&t);
    int i,j,k;
    int c,d,n;
    for(i=0;i<t;i++)
    {
        l.clear();
        idxa=0;
        for(j=0;j<201;j++)
        {
            for(k=0;k<201;k++)
            {
                q[j][k]=0;
                o[j][k]=0;
            }
        }
        scanf("%d",&c);
        for(j=0;j<c;j++)
        {
            scanf("%s",in);
            a1=in[0];
            a2=in[1];
            a3=in[2];
            q[(int)a1][(int)a2]=(int)a3;
            q[(int)a2][(int)a1]=(int)a3;
        }   
        scanf("%d",&d);
        for(j=0;j<d;j++)
        {
            scanf("%s",in);
            a1=in[0];
            a2=in[1];
            o[(int)a1][(int)a2]=1;
            o[(int)a2][(int)a1]=1;
        }
        scanf("%d",&n);
        scanf("%s",str);
        int t1,t2;
        for(j=0;j<n;j++)
        {
            l.push_back((int)str[j]);
            if((int)l.size()>=2)
            {
                it=l.end();
                it--;
                t1=(*it);
                it--;
                t2=(*it);
                if(q[t1][t2]!=0)
                {
                    l.pop_back();
                    l.pop_back();
                    l.push_back((int)q[t1][t2]);
                }   
            }
            for(it=l.begin();it!=l.end();it++)
            {
                for(it1=l.begin();it1!=l.end();it1++)
                {
                    if(o[(*it)][(*it1)]==1){ l.clear(); break; }
                }
                if(l.empty()) break;
            }
        }
        printf("Case #%d: [",i+1);
        it1=l.end();
        it1--;
        for(it=l.begin();it!=l.end();it++)
        {
            printf("%c",(*it));
            if(it!=it1) printf(", ");
        }
        printf("]\n");
    }
    scanf(" ");
}
