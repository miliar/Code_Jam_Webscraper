using namespace std;
#include<iostream>
#include<cstdio>

    int main()
    {
        int n,t=0 ;
        cin>>n;
        while(n--)
        {
        t++;
        int i ,j ,l,m,flag=0;
        char a[4][4],b[4][4],c[4][4];
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
               cin>>a[i][j];
            }
        }

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
              b[i][j]=c[i][j]=a[i][j];
            }
        }

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(b[i][j]=='T')b[i][j]='X';
                if(c[i][j]=='T')c[i][j]='O';
            }
        }


        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(b[i][j]=='X')
                {
                    l=i;m=j;
                    if(((b[(l+1)%4][m]=='X')&&(b[(l+2)%4][m]=='X')&&(b[(l+3)%4][m]=='X'))||((b[l][(m+1)%4]=='X') &&(b[l][(m+2)%4]=='X') && (b[l][(m+3)%4]=='X') ) )
                    {
                        cout<<"Case #"<<t<<": X won"<<endl;
                     //   printf("Case #%d: X won\n",t);
                        flag=1;
                        break;
                    }
                    if(i==j)
                    {
                        if((b[(i+1)%4][(j+1)%4]=='X' && b[(i+2)%4][(j+2)%4]=='X'&&b[(i+3)%4][(j+3)%4]=='X') )
                       {
                           cout<<"Case #"<<t<<": X won"<<endl;
                           //printf("Case #%d: X won\n",t);
                        flag=1;
                        break;

                       }
                    }
                    if(i+j==3)
                    {
                      if((b[(i-1)%4][(j+1)%4]=='X' && b[(i-2)%4][(j+2)%4]=='X'&&b[(i-3)%4][(j+3)%4]=='X'))
                    {
                        cout<<"Case #"<<t<<": X won"<<endl;
                         //printf("Case #%d: X won\n",t);
                        flag=1;
                        break;

                    }
                    }


            }
             if(c[i][j]=='O')
                {
                    l=i;m=j;
                    if(((c[(l+1)%4][m]=='O')&&(c[(l+2)%4][m]=='O')&&(c[(l+3)%4][m]=='O'))||((c[l][(m+1)%4]=='O') &&(c[l][(m+2)%4]=='O') && (c[l][(m+3)%4]=='O') ) )
                    {
                        cout<<"Case #"<<t<<": O won"<<endl;
                        //printf("Case #%d: O won\n",t);
                        flag=1;
                        break;
                    }
                    if(i==j)
                    {
                        if((c[(i+1)%4][(j+1)%4]=='O' && c[(i+2)%4][(j+2)%4]=='O'&&c[(i+3)%4][(j+3)%4]=='O') )
                       {
                           cout<<"Case #"<<t<<": O won"<<endl;
                             //printf("Case #%d: O won\n",t);

                        flag=1;
                        break;

                       }
                    }
                    if(i+j==3)
                    {
                      if((c[(i-1)%4][(j+1)%4]=='O' && c[(i-2)%4][(j+2)%4]=='O'&&c[(i-3)%4][(j+3)%4]=='O'))
                    {
                        cout<<"Case #"<<t<<": O won"<<endl;
                        //printf("Case #%d: O won\n",t);
                        flag=1;
                        break;

                    }
                    }

            }
          }  if(flag==1)break;
        }
        if(flag!=1)
        {


        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='.'){cout<<"Case #"<<t<<": Game has not completed"<<endl;flag=1;break;}
            }
            if(flag==1)break;
        }
        }
        if(flag==0)cout<<"Case #"<<t<<": Draw"<<endl;

        }

        return 0 ;
    }
