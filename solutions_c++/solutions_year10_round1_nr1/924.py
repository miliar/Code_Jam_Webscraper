#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<bitset>


using namespace std;

int t,n,k;
char a[50][50],b[50][50];

void display(char te[50][50])
{
     for(int i=0;i<n;i++)
     {
             for(int j=0;j<n;j++)
             cout<<te[i][j]<<" ";
             cout<<endl;
     }
     cout<<endl<<endl;
}


void rotate()
{
     for(int i=0;i<n;i++)
     {
             for(int j=0;j<n;j++)
             b[j][n-1-i]=a[i][j];
     }
     //display(b);
}

void gravity()
{
     int i;
     for(int j=0;j<n;j++)
     {
             int k=n-1;
             int done=0;
             for(i=n-1;i>=0;i--)
             {
                                while(b[i][j]!='.' && !done)
                                i--;
                                if(!done)
                                k=i;
                                done=1;
                                if(b[i][j]!='.')
                                {
                                             
                                             while(b[i][j]!='.' && i!=-1)
                                             {
                                                 
                                                 b[k][j]=b[i][j];
                                                 b[i][j]='.';
                                                 k--;i--;
                                             }
                                }
                                
                                
                                
             }   
             
             
             
     }
     //display(b);
}


int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   char temp[50];
   scanf("%d",&t);
   int see;
   for(int prob=0;prob<t;prob++)
   {
           scanf("%d %d",&n,&k);
           //scanf("%s",temp);
           //cout<<n<<" "<<k<<endl;
           for(int i=0;i<n;i++)
           {
                   scanf("%s",temp);
                   for(int j=0;j<n;j++)
                   {a[i][j]=temp[j];}//cout<<a[i][j]<<endl;}
                   
           }
           //display(a);
           rotate();
           gravity();
           //cout<<k<<endl;
           int bd=0,r=0;
           for(int i=0;i<n;i++)
           {
                   for(int j=0;j<n;j++)
                   {
                           if(b[i][j]=='R' && !r)
                           {
                                            for(see=0;see<k && j+k<=n;see++)
                                            if(b[i][j+see]!='R')
                                            break;
                                            if(see==k)
                                            r=1;
                                            
                                            for(see=0;see<k && i+k<=n;see++)
                                            if(b[i+see][j]!='R')
                                            break;
                                            if(see==k)
                                            r=1;
                                            
                                            for(see=0;see<k && i+k<=n && j+k<=n;see++)
                                            if(b[i+see][j+see]!='R')
                                            break;
                                            if(see==k)
                                            r=1;
                                            
                                            for(see=0;see<k && i+k<=n && j-k+2>0;see++)
                                            if(b[i+see][j-see]!='R')
                                            break;
                                            if(see==k)
                                            r=1;
                           }
                           else if(b[i][j]=='B' && !bd)
                           {
                                            //cout<<i<<" "<<j<<endl;
                                            for(see=0;see<k && j+k<=n;see++)
                                            if(b[i][j+see]!='B')
                                            break;
                                            if(see==k && j+k<=n)
                                            bd=1;
                                            
                                            for(see=0;see<k && i+k<=n;see++)
                                            if(b[i+see][j]!='B')
                                            break;
                                            if(see==k && i+k<=n)
                                            bd=1;
                                            
                                            for(see=0;see<k && i+k<=n && j+k<=n;see++)
                                            if(b[i+see][j+see]!='B')
                                            break;
                                            if(see==k && i+k<=n && j+k<=n)
                                            bd=1;
                                            
                                            for(see=0;see<k && i+k<=n && j-k+2>0;see++)
                                            if(b[i+see][j-see]!='B')
                                            break;
                                            if(see==k && i-k+2>0 && j-k+2>0)
                                            bd=1;
                           }
                   }
           }
           
           if(bd && r)
           printf("Case #%d: Both\n",prob+1);
           else if(bd==0 && r==1)
           printf("Case #%d: Red\n",prob+1);
           else if(bd==1 && r==0)
           printf("Case #%d: Blue\n",prob+1);
           else
           printf("Case #%d: Neither\n",prob+1);
                                            
                           
   }

   //system("pause");
   return 0;

}
