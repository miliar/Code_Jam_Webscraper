#include<iostream>
using namespace std;
#define inf 100000

char cal(int i,int j,int a[200][200],char b[200][200],char &ch);
int main()
{
    int t,c1=1;
    cin>>t;
    while(t--)
    {
       int a[200][200]={0};
       char b[200][200]={0},ch='a'-1;
       int i,j,h,w;
       cin>>h>>w;
       for(i=0;i<=w+1;i++) {a[0][i]=inf;a[h+1][i]=inf;}
       for(j=0;j<h+1;j++)  {a[j][0]=inf;a[j][w+1]=inf;}
       for(i=1;i<=h;i++)
         {for(j=1;j<=w;j++)
            {cin>>a[i][j];}
          }  
       for(i=1;i<=h;i++)
         for(j=1;j<=w;j++)
            if(b[i][j]) continue;
            else b[i][j]=cal(i,j,a,b,ch);
      cout<<"Case #"<<c1<<":"<<endl; c1++;
       for(i=1;i<=h;i++)
         {for(j=1;j<=w;j++)
           cout<<b[i][j]<<" ";
          cout<<endl;
         }
    }
    return 0;
}
char cal(int i,int j,int a[200][200],char b[200][200],char &ch)
{
     int v[4]={0},r[4]={0},c[4]={0},p[4]={0};
     v[0]=a[i-1][j];r[0]=i-1;c[0]=j;p[0]=0;
     v[1]=a[i][j-1];r[1]=i;c[1]=j-1;p[1]=1;
     v[2]=a[i][j+1];r[2]=i;c[2]=j+1;p[2]=2;
     v[3]=a[i+1][j];r[3]=i+1;c[3]=j;p[3]=3;         
     int s=0,d;
     for(d=1;d<4;d++)
       if(v[s]>v[d] || (v[s]==v[d] && p[s]>p[d]))
                               {  swap(v[s],v[d]);
                                  swap(r[s],r[d]);
                                  swap(c[s],c[d]);
                                  swap(p[s],p[d]);
                               }
    if(a[i][j]>v[0] && b[r[0]][c[0]]) {b[i][j]= b[r[0]][c[0]];return b[i][j];}
    else if(a[i][j]>v[0] && !b[r[0]][c[0]]) {b[i][j]=(cal(r[0],c[0],a,b,ch));return b[i][j];}
    else {ch++;b[i][j]=ch;return b[i][j];}
}                                 
