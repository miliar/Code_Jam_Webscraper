#include <iostream>
#include<cstdio>
#include<string>
using namespace std;

int main()
{
    freopen("A-large (1).in","r", stdin);
    freopen("output.in","w", stdout);

    int t,i,it,j;
    string s[5];
    scanf("%d",&t);
    for(it=1; it<=t; it++)
    {
        printf("Case #%d: ",it);
        char a[17][5];
        int k=0;
        for(i=0; i<4; i++)
        {
            cin>>s[i];
            for(j=0; j<4; j++) a[k][j]=s[i][j];
            k++;
        }
        getchar();
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                a[k][j]=s[j][i];
            }
            k++;
        }
        for(i=0,j=0; i<4; i++,j++)
        {
            a[k][i]=s[i][j];
        }
        k++;
        for(i=3,j=0; i>=0; i--,j++)
        {
            a[k][j]=s[i][j];
        }
        k++;
        /*for(i=0;i<k;i++)
        {string str="";
            for(j=0;j<4;j++)
        str=str+a[i][j];
        cout<<str<<endl;
        }*/
        bool x=false,y=false,z=false;
        for(i=0; i<k; i++)
        {
            string str="";
            for(j=0; j<4; j++)
                str=str+a[i][j];
            if(str=="XXXT"||str=="XTXX"||str=="XXTX"||str=="TXXX"||str=="XXXX") x=true;
            else if(str=="OOOT"||str=="OOTO"||str=="OTOO"||str=="TOOO"||str=="OOOO") y=true;
            else
            {
                for(j=0; j<4; j++) if(a[i][j]=='.') z=true;
            }

        }
        if(x==true)
            printf("X won");
        else if(y==true)
            printf("O won");
        else if(z==true)
        {
            printf("Game has not completed");
        }
        else printf("Draw");
        printf("\n");
    }

    return 0;
}
