#include<fstream>
using namespace std;

int main()
{
    ifstream fin("A.in");
    ofstream fout("A.out");
    
    int t,n,k,j,l,pos;
    char c[50][50];
    
    fin>>t;
    
    for(int i=1;i<=t;i++)
    {
         fin>>n;
         fin>>k;
    
         for(j=0;j<n;j++)
         {
             for(l=0;l<n;l++)
             {
                 fin>>c[j][l];
             }
         }
    
         for(j=n-1;j>=0;j--)
         {
             pos=n-1;
             for(l=n-1;l>=0;l--)
             {
                if(c[j][l]!='.')
                 {
                     c[j][pos]=c[j][l];
                     pos--;
                 }
             }
    
             for(;pos>=0;pos--)
                 c[j][pos]='.';
         }
         
         bool flag,b=false,r=false;
         int m,x,y;
         for(j=n-1;j>=0;j--)
         {
             for(l=0;l<n;l++)
             {
                 if(c[j][l]=='B'&&!b)
                 {
                     if(j>=k-1 && c[j-1][l]=='B')
                     {
                         x=j-2;
                         y=l;
                         flag=true;
                         for(m=2;m<k;m++)
                         {
                             if(c[x][y]!='B')
                             {
                                 flag=false;
                                 break;
                             }
                             x--;
                         }
                         if(flag)
                         {
                             b=true;
                             continue;
                         }
                     }
                     if(l+k<=n && c[j][l+1]=='B')
                     {
                         x=j;
                         y=l+2;
                         flag=true;
                         for(m=2;m<k;m++)
                         {
                             if(c[x][y]!='B')
                             {
                                 flag=false;
                                 break;
                             }
                             y++;
                         }
                         if(flag)
                         {
                             b=true;
                             continue;
                         }                                       
                     }
                     if(j-k+1>=0 && l-k+1>=0 && c[j-1][l-1]=='B')
                     {
                         x=j-2;
                         y=l-2;
                         flag=true;
                         for(m=2;m<k;m++)
                         {
                             if(c[x][y]!='B')
                             {
                                 flag=false;
                                 break;
                             }
                             x--;
                             y--;
                         }
                         if(flag)
                         {
                             b=true;
                             continue;
                         }
                     }
                     if(j-k+1>=0 && l+k<=n && c[j-1][l+1]=='B')
                     {
                         x=j-2;
                         y=l+2;
                         flag=true;
                         for(m=2;m<k;m++)
                         {
                             if(c[x][y]!='B')
                             {
                                 flag=false;
                                 break;
                             }
                             x--;
                             y++;
                         }
                         if(flag)
                         {
                             b=true;
                             continue;
                         }
                     }
                 }
                 else if(c[j][l]=='R'&&!r)
                 {
                     if(j>=k-1 && c[j-1][l]=='R')
                     {
                         x=j-2;
                         y=l;
                         flag=true;
                         for(m=2;m<k;m++)
                         {
                             if(c[x][y]!='R')
                             {
                                 flag=false;
                                 break;
                             }
                             x--;
                         }
                         if(flag)
                         {
                             r=true;
                             continue;
                         }
                     }
                     if(l+k<=n && c[j][l+1]=='R')
                     {
                         x=j;
                         y=l+2;
                         flag=true;
                         for(m=2;m<k;m++)
                         {
                             if(c[x][y]!='R')
                             {
                                 flag=false;
                                 break;
                             }
                             y++;
                         }
                         if(flag)
                         {
                             r=true;
                             continue;
                         }                                       
                     }
                     if(j-k+1>=0 && l-k+1>=0 && c[j-1][l-1]=='R')
                     {
                         x=j-2;
                         y=l-2;
                         flag=true;
                         for(m=2;m<k;m++)
                         {
                             if(c[x][y]!='R')
                             {
                                 flag=false;
                                 break;
                             }
                             x--;
                             y--;
                         }
                         if(flag)
                         {
                             r=true;
                             continue;
                         }
                     }
                     if(j-k+1>=0 && l+k<=n && c[j-1][l+1]=='R')
                     {
                         x=j-2;
                         y=l+2;
                         flag=true;
                         for(m=2;m<k;m++)
                         {
                             if(c[x][y]!='R')
                             {
                                 flag=false;
                                 break;
                             }
                             x--;
                             y++;
                         }
                         if(flag)
                         {
                             r=true;
                             continue;
                         }
                     }
                 }
             }
         }
         fout<<"Case #"<<i<<": ";
         if(!r&&!b)
             fout<<"Neither"<<endl;
         else if(b&&r)
             fout<<"Both"<<endl;
         else if(r)
             fout<<"Red"<<endl;
         else
             fout<<"Blue"<<endl;
    }
}
