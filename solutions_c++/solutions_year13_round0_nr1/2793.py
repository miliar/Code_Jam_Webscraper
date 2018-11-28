#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int t,m,status;
char a[10][10];
main()
{
        freopen("inb1.txt","r",stdin);
        freopen("outb1.txt","w",stdout);
        scanf("%d",&t);
        for(int r=1;r<=t;r++)
        {
                status = 0;
                for(int i=0;i<4;i++)
                {
                        scanf("%s",a[i]);
                }
                //if O wins
                for(int i=0;i<4;i++)
                {
                        m=0;
                        for(int j=0;j<4;j++)
                        {
                                if(a[i][j]!='O' && a[i][j]!='T')
                                {
                                        m=1;
                                        break;
                                }
                        }
                        if(!m)
                        {
                                status=1;
                                break;
                        }
                }
                for(int i=0;i<4;i++)
                {
                        m=0;
                        for(int j=0;j<4;j++)
                        {
                                if(a[j][i]!='O' && a[j][i]!='T')
                                {
                                        m=1;
                                        break;
                                }
                        }
                        if(!m)
                        {
                                status=1;
                                break;
                        }
                }
                m=0;
                for(int i=0;i<4;i++)
                {
                        if(a[i][i]!='O' && a[i][i]!='T')
                        {
                                m=1;
                                break;
                        }
                }
                if(!m)
                {
                        status=1;
                }m=0;
                for(int i=0;i<4;i++)
                {
                        if(a[i][3-i]!='O' && a[i][3-i]!='T')
                        {
                                m=1;
                                break;
                        }
                }
                if(!m)
                {
                        status=1;
                }
                //if X wins
                for(int i=0;i<4;i++)
                {
                        m=0;
                        for(int j=0;j<4;j++)
                        {
                                if(a[i][j]!='X' && a[i][j]!='T')
                                {
                                        m=1;
                                        break;
                                }
                        }
                        if(!m)
                        {
                                status=2;
                                break;
                        }
                }
                for(int i=0;i<4;i++)
                {
                        m=0;
                        for(int j=0;j<4;j++)
                        {
                                if(a[j][i]!='X' && a[j][i]!='T')
                                {
                                        m=1;
                                        break;
                                }
                        }
                        if(!m)
                        {
                                status=2;
                                break;
                        }
                }
                m=0;
                for(int i=0;i<4;i++)
                {
                        if(a[i][i]!='X' && a[i][i]!='T')
                        {
                                m=1;
                                break;
                        }
                }
                if(!m)
                {
                        status=2;
                }m=0;
                for(int i=0;i<4;i++)
                {
                        if(a[i][3-i]!='X' && a[i][3-i]!='T')
                        {
                                m=1;
                                break;
                        }
                }
                if(!m)
                {
                        status=2;
                }
                //if draw
                if(!status)
                {
                        m=0;
                        for(int i=0;i<4;i++)
                        {
                                for(int j=0;j<4;j++)
                                {
                                        if(a[i][j]=='.')
                                        {
                                                m=1;
                                                break;
                                        }
                                }
                                if(m) break;
                        }
                        if(m)
                        {
                                status=3;
                        }
                        else
                        {
                                status=4;
                        }
                }
                
                printf("Case #%d: ",r);
                switch(status) {
                        case 1 : printf("O won\n"); break;
                        case 2 : printf("X won\n"); break;
                        case 3 : printf("Game has not completed\n"); break;
                        case 4 : printf("Draw\n"); break;
                }       
        }
        //system("pause");
}
