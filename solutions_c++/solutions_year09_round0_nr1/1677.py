#include <iostream>

using namespace std;

char a[5005][17]={'\0'};
char b[555]={'\0'},temp[20]={'\0'};
int c[22][2]={0},p=0,k,d;
int len=0,ans=0,l;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,i,j;
    while(scanf("%d%d%d",&l,&d,&n)!=EOF)
    {
        getchar();
        for(i=0;i<d;i++)
        {
            scanf("%s",a[i]);
//            cout<<a[i]<<endl;
        }
//        for(i=0;i<30;i++)
//            cout<<v[i]<<"  ";

        getchar();
        for(i=0;i<n;i++)
        {
            scanf("%s",b);
//            cout<<b<<endl;
            len=strlen(b);
            k=0;
            for(j=0;j<len;j++)
            {
                if(b[j]=='(')
                {
                    int x;
                    for( x=j;x<len;x++)
                        if(b[x]==')')break;
                    c[k][0]=j+1;
                    c[k++][1]=x;
                    j=x;
                }
                else
                {
                    c[k][0]=j;
                    c[k++][1]=j+1;
                }
            }
//            for(j=0;j<k;j++)
//            {
//                cout<<c[j][0]<<" "<<c[j][1]<<endl;;
//            }
            int x,y,tag;
            for(j=0;j<d;j++)
            {
                for(x=0;x<l;x++)
                {
                    tag=0;
                    for(y=c[x][0];y<c[x][1];y++)
                    {
                        if(b[y]==a[j][x])tag=1;
                    }
                    if(tag!=1)break;
                }
                if(x==l)ans++;
            }
            printf("Case #%d: %d\n",i+1,ans);
            ans=0;
        }
    }
    return 0;
}
