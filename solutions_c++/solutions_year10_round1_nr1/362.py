#include<algorithm>
#include<cstdio>
using namespace std;
const int L=100;

int n,table[L][L],win[5],K;

int bound(int x,int y) {return x>=0 && x<n && y>=0 && y<n;}

int chk(int mx,int my,int d,int dx,int dy)
{
    int i;
    for(i=1;i<K;i++)
    {
        mx+=dx;
        my+=dy;
        if(bound(mx,my))
        {
            if(table[mx][my]!=d)
                return 0;
        }
        else
            return 0;
    }
    return 1;
}

int yiping()
{
    int i,j,c;
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
        {
            c=table[i][j];
            if(c)
            {   
                win[c]+=chk(i,j,c,0,1);
                win[c]+=chk(i,j,c,1,0);
                win[c]+=chk(i,j,c,1,1);
                win[c]+=chk(i,j,c,1,-1);
//                printf("(%d %d) %d %d %d\n",i,j,win[1],win[2],K);
            }
        }

}

void print()
{
    int i,j;
    for(i=0;i<n;i++,puts(""))    
        for(j=0;j<n;j++)
            printf("%d ",table[i][j]);
}

main()
{
    int i,j,k,c,cases,T;
    char tmp[L][L];
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    
    scanf("%d",&T);
    for(cases=1;cases<=T;cases++)
    {
        scanf("%d %d",&n,&K);
        for(i=0;i<n;i++)
            scanf("%s",tmp[i]);

        win[0]=0;
        win[1]=0;
        win[2]=0;

        for(i=0;i<n;i++)    
            for(j=0;j<n;j++)
            {
                if(tmp[i][j]=='R')
                    c=1;
                else if(tmp[i][j]=='B')
                    c=2;
                else
                    c=0;
                table[i][j]=c;
            }
        yiping();
//        print();
        for(i=0;i<n;i++)
            for(j=n-1;j>=0;j--)
            {
                if(table[i][j]==0)
                {
                    for(k=j;k>=0;k--)            
                        if(table[i][k])
                        {
                            table[i][j]=table[i][k];
                            table[i][k]=0;
                            break;
                        }
                }
            }
        yiping();
//        print();
        printf("Case #%d: ",cases);

        if(win[1] && win[2])
            puts("Both");
        else if(win[1])
            puts("Red");
        else if(win[2])
            puts("Blue");
        else
            puts("Neither");
        
    }
}
