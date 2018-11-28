#include<iostream>
using namespace std;
#define see(x) cout<<#x<<" "<<x<<endl
#define sp system("pause")
int map[110][110];
void display()
{
    for(int j=1;j<=6;j++)
        {
                for(int i=1;i<=6;i++)
                {
                    cout<<map[i][j];
                }
                cout<<endl;
        }
    //sp;
    cout<<endl;    
}
int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int cas,T,n,i,j,k,x1,x2,y1,y2,tim;
    scanf("%d",&T);
    for(cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        memset(map,0,sizeof(map));
        for(k=0;k<n;k++)
        {
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for(j=y1;j<=y2;j++)
                for(i=x1;i<=x2;i++)
                {
                    map[i][j]=1;
                }
        }
        //display();
        bool flag;
        for(tim=1;;tim++)
        {
            flag=false;
            for(i=1;i<=100;i++)
                for(j=1;j<=100;j++)
                {
                    if(map[i][j]==1)
                    {
                        if((map[i-1][j]>=1) || (map[i][j-1]>=1))
                        {
                            map[i][j]=1;
                        }
                        else
                        {
                            map[i][j]=2;
                        }
                        //see(i);
                        //see(j);
                        //see(map[i-1][j]);
                        //see(map[i][j-1]);
                        //see(map[i][j]);
                        flag=true;
                    }
                    else
                    {
                        if((map[i-1][j]>=1) && (map[i][j-1]>=1))
                            map[i][j]=-1;
                    }
                }
            for(i=1;i<100;i++)
                for(j=1;j<=100;j++)
                    if(map[i][j]==-1)
                        map[i][j]=1;
                    else if(map[i][j]==2)
                        map[i][j]=0;
            //display();    
            if(!flag)
                break;
        }
        printf("Case #%d: %d\n",cas,tim-1);
    }
}
