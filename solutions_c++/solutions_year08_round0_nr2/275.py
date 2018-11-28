#include<stdio.h>
#include<stdlib.h>
#include<set>
using namespace std;
struct node
{   int ar1,ar2,de1,de2;
    bool operator < (const node &r) const
    {   if(ar1 != r.ar1) return ar1 < r.ar1;
        if(ar2 != r.ar2) return ar2 < r.ar2;
        if(de1 != r.de1) return de1 < r.de1;
        else return de2 < r.de2;
    }
}x;

int main()
{   int n,na,nb,t,i,j,c,ansa=0,ansb=0,out;
    char scan[10];
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    multiset<node> treea,treeb;
    multiset<node>::iterator sa,sb;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {   ansa=0;
        ansb=0;
        scanf("%d %d %d",&t,&na,&nb);
        for(j=0;j<na;j++)
        {   scanf("%s",scan);
            x.ar1=(scan[0]-'0')*10;
            x.ar1+=(scan[1]-'0');
            x.ar2=(scan[3]-'0')*10;
            x.ar2+=(scan[4]-'0');
            scanf("%s",scan);
            x.de1=(scan[0]-'0')*10;
            x.de1+=(scan[1]-'0');
            x.de2=(scan[3]-'0')*10;
            x.de2+=(scan[4]-'0');
            treea.insert(x);
        }
        //for(sa=treea.begin();sa!=treea.end();sa++)
          //  printf("%d:%d %d:%d\n",sa->ar1,sa->ar2,sa->de1,sa->de2);
        for(j=0;j<nb;j++)
        {   scanf("%s",scan);
            x.ar1=(scan[0]-'0')*10;
            x.ar1+=(scan[1]-'0');
            x.ar2=(scan[3]-'0')*10;
            x.ar2+=(scan[4]-'0');
            scanf("%s",scan);
            x.de1=(scan[0]-'0')*10;
            x.de1+=(scan[1]-'0');
            x.de2=(scan[3]-'0')*10;
            x.de2+=(scan[4]-'0');
            treeb.insert(x);
        }
        //for(sb=treeb.begin();sb!=treeb.end();sb++)
          //  printf("%d:%d %d:%d\n",sb->ar1,sb->ar2,sb->de1,sb->de2);
        while(!treea.empty()||!treeb.empty())
        {   sa=treea.begin();
            sb=treeb.begin();
            if(treea.empty()) c=2;
            else if(treeb.empty()) c=1;
            else
            {   if( (sa->ar1)<(sb->ar1) ) c=1;
                else if( (sa->ar1)>(sb->ar1) ) c=2;
                else if( (sa->ar2)<=(sb->ar2) ) c=1;
                else c=2;
            }
            x.de1=0;
            x.de2=0;
            if(c==1)
            {   ansa++;
                x.ar1=sa->de1;
                x.ar2=sa->de2;
                c=2;
                treea.erase(sa);
            }
            else
            {   ansb++;
                x.ar1=sb->de1;
                x.ar2=sb->de2;
                c=1;
                treeb.erase(sb);
            }
            out=0;
            //printf("[%d %d %d]\n",x.ar1,x.ar2,c);
            do{
            x.ar2+=t;
            if(x.ar2>=60)
            {   x.ar2-=60;
                x.ar1++;
            }
            switch(c)
            {   case 1: sa=treea.lower_bound(x);
                //printf("1 [%d %d]\n",x.ar1,x.ar2);
                //if(sa!=treea.end())printf("%d %d\n",sa->ar1,sa->ar2);
                while(sa!=treea.end()&&sa->ar1==x.ar1&&sa->ar2<x.ar2)
                    sa++;
                if(sa!=treea.end())
                {   x.ar1=sa->de1;
                    x.ar2=sa->de2;
                    treea.erase(sa);
                }
                else out=1;
                c=2;
                break;
                case 2: sb=treeb.lower_bound(x);
                //printf("2 [%d %d]\n",x.ar1,x.ar2);
                //if(sb!=treeb.end())printf("%d %d\n",sb->ar1,sb->ar2);
                while(sb!=treeb.end()&&sb->ar1==x.ar1&&sb->ar2<x.ar2)
                    sb++;
                if(sb!=treeb.end())
                {   x.ar1=sb->de1;
                    x.ar2=sb->de2;
                    treeb.erase(sb);
                }
                else out=1;
                c=1;
            }
            }while(out==0);
        }
        printf("Case #%d: %d %d\n",i,ansa,ansb);
    }
    //system("pause");
    return 0;
}
