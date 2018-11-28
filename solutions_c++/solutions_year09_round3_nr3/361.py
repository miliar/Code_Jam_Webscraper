#include<iostream>
using namespace std;
main()
{
    int i,j,k,l,c,b[1000],in,d[1000],n,q;
    cin>>n;
    for(q=1;q<=n;q++)
    {
     int a[200][200]={0};
     int t[1000]={0};
     cin>>l>>c;
     d[0]=0;
     for(i=0;i<c;i++)
     {
     cin>>b[i];
     d[i+1]=b[i];
     }
     b[c]=l;
     for(i=1;i<=c;i++)
     {
      for(j=0;j<=c-i;j++)
      {
        in=0;
        for(k=j;k<i+j;k++)
        {
          t[in++]=(a[j][k]+a[k+1][i+j]);
        }
        if(b[j+i]==l)
        a[j][j+i]=t[min_element(t,t+in)-t]+b[j+i]-d[j]-1;
        else
        a[j][j+i]=t[min_element(t,t+in)-t]+b[j+i]-d[j]-2;
      }
     }
     cout<<"Case #"<<q<<": "<<a[0][c]<<"\n";
     }
     }
