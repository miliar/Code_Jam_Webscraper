#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int a[10][3];
char b[4][4];
int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    int t,i,k,m,count,j,flag;
    cin>>t;
    k=0;
    while(t--)
    {
        getchar();
        m=count=0;
        for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
            scanf("%c",&b[i][j]);
            getchar();
        }
        /*for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
            printf("%c ",b[i][j]);
            cout<<endl;
        }
        cout<<endl;*/
        memset(a,0,sizeof(a));
        for(i=0;i<4;++i)
        {
            
            for(j=0;j<4;++j)
            {
                if(b[i][j]=='X')
                ++a[m][0];
                else if(b[i][j]=='O')
                ++a[m][1];
                else if(b[i][j]=='T')
                ++a[m][2];
                else
                ++count;
            }
            ++m;
            
            for(j=0;j<4;++j)
            {
                if(b[j][i]=='X')
                ++a[m][0];
                else if(b[j][i]=='O')
                ++a[m][1];
                else if(b[j][i]=='T')
                ++a[m][2];
                else
                ++count;
            }
            ++m;
            
            if(b[i][i]=='X')
            ++a[8][0];
            else if(b[i][i]=='O')
            ++a[8][1];
            else if(b[i][i]=='T')
            ++a[8][2];
            else
            ++count;
        
            if(b[i][3-i]=='X')
            ++a[9][0];
            else if(b[i][3-i]=='O')
            ++a[9][1];
            else if(b[i][3-i]=='T')
            ++a[9][2];
            else
            ++count;
            
        }
        /*for(i=0;i<10;++i)
        {
            for(j=0;j<3;++j)
            cout<<a[i][j]<<" ";
            cout<<endl;
        }*/
        flag=0;
        for(i=0;i<10;++i)
        {
            if(a[i][0]+a[i][2]==4)
            {
               flag=1;
               printf("Case #%d: X won\n",++k);
               //cout<<i<<endl;
               break;
            }
            if(a[i][1]+a[i][2]==4)
            {
                flag=1;
                printf("Case #%d: O won\n",++k);
                //cout<<i<<endl;
                break;
            }
        } 
        if(flag==0)
        {
            if(count==0)
            printf("Case #%d: Draw\n",++k);
            else
            printf("Case #%d: Game has not completed\n",++k);
        }
    }    
    return 0;
}
