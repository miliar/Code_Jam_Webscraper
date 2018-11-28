#include<iostream>
#include<fstream>
using namespace std;
main()
{
    char a[101][101];
    int b[101];
    int i,j,t,n,k,l,p,x,y;
    int mv[4][2]={0,1,1,0,1,1,-1,1};
    bool u[2];
      ifstream in("a.txt");
      ofstream out("a.out");
      in>>t;
      for(int tt=1;tt<=t;tt++)
      {
            in>>n>>k;
            for(i=0;i<n;i++)
            {
                b[i]=-1;
                for(j=0;j<n;j++)
                {
                    in>>a[i][j];
                }
            }
            for(i=0;i<n;i++)
            {
                for(j=n-1;j>=0;j--)
                {
                    if(a[i][j]=='.' && b[i]==-1)
                    {
                        b[i]=j;
                    }
                    if(a[i][j]!='.' && b[i]>=0)
                    {
                        a[i][b[i]]=a[i][j];
                        a[i][j]='.';
                        b[i]--;
                    }
                }
            }
            u[0]=u[1]=false;
            for(i=0;i<n;i++)
            {
                for(j=0;j<n;j++)
                {
                    if(a[i][j]!='.')
                    for(l=0;l<4;l++)
                    {
                        p=1;
                        x=i;y=j;
                        while(a[x][y]==a[i][j])
                        {
                            x+=mv[l][0];y+=mv[l][1];
                            if(x>=0 && x<n && y>=0 && y<n)
                            {
                                if(a[x][y]==a[i][j])p++;
                                if(p>=k)break;
                            } else break;
                        }
                        if(p>=k)
                        {
                            if(a[i][j]=='R')u[0]=true;else u[1]=true;
                        }
                    }
                }
            }
            out<<"Case #"<<tt<<": ";
            if(u[0] && u[1])out<<"Both"<<endl;
            else
            {
                if(u[0])out<<"Red"<<endl;
                if(u[1])out<<"Blue"<<endl;
                if(!u[0] && !u[1])out<<"Neither"<<endl;
            }
      }
//      system("PAUSE");
}
