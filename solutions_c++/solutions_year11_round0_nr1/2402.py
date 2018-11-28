#include<cstdio>
#define abs(x) ((x)<0?-(x):(x))

using namespace std;

int T,n,lo,lb;
int d[1000],o[1000],b[1000];

int work()
{
    scanf("%d",&n);
    char c[10];
    lo=0;lb=0;
    for (int i=0;i<n;i++){
        scanf("%s%d",&c,&d[i]);
        if (c[0]=='O')
            o[lo++]=i;
        else
            b[lb++]=i;
    }

    int to=0,tb=0,t=0,x=1,y=1,s=0;
    for (int i=0;i<n;i++){
        if (o[to]==i&&to<lo){
            s=abs(d[o[to]]-x)+1;
            t+=s;
            x=d[o[to]];
//            printf("O %d %d\n",t,x);
            to++;
            if (abs(d[b[tb]]-y)<=s)
                y=d[b[tb]];
            else
                if (d[b[tb]]>y)
                    y=y+s;
                else
                    y=y-s;
        }else{
//            printf("B %d %d\n",b[tb],y);
            s=abs(d[b[tb]]-y)+1;
            t+=s;
            y=d[b[tb]];
//            printf("B %d %d\n",t,y);
            tb++;
            if (abs(d[o[to]]-x)<=s)
                x=d[o[to]];
            else
                if (d[o[to]]>x)
                    x=x+s;
                else
                    x=x-s;
        }
    }
    return t;
}

int main()
{
    FILE *cin=freopen("A.txt", "w", stdout);
    scanf("%d",&T);
    for (int tnum=1;tnum<=T;tnum++){
        printf("Case #%d: %d\n",tnum,work());
    }
}
