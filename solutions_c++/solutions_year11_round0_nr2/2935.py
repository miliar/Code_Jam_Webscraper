#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    freopen("s.txt","w",stdout);
    int j,i,k,t,c,d,n,p,l;
    char c1[50][5],d1[50][5],n1[105],a[102];
    cin>>t;
    for(j=1;j<=t;j++)
    {
       cin>>c;
       if(c>0)
        for(i=0;i<c;i++)
         cin>>c1[i];
       cin>>d;
       if(d>0)
        for(i=0;i<d;i++) 
         cin>>d1[i];
       cin>>n;
       cin>>n1;
       for(i=0;i<n;i++)
         a[i]=n1[i];
       p=1;
       for(i=1;i<n;i++)
       {
          a[p]=n1[i];
          for(l=0;l<c;l++)
          {
           if(c>0 && (a[p-1]==c1[l][0]&&a[p]==c1[l][1]) || (a[p-1]==c1[l][1]&&a[p]==c1[l][0]) )
           {  
             a[p-1]=c1[l][2];
             a[p]='a';
             p--;
           }
          }
          for(l=0;l<d;l++)
          {
           if(d>0&& a[p]==d1[l][0] )
           {
             for(k=p-1;k>=0;k--)
                if(a[k]==d1[l][1])
                   p=-1;
           }
           else if(d>0&& a[p]==d1[l][1] )
           {
            for(k=p-1;k>=0;k--)
                if(a[k]==d1[l][0])
                   p=-1;
           }
          }
          p++;
       }
       if(p>0)
       {
       cout<<"Case #"<<j<<": [";
       for(i=0;i<p-1;i++)
          cout<<a[i]<<", ";
       cout<<a[p-1]<<"]"<<endl;
       }
       else
       cout<<"Case #"<<j<<": []"<<endl;
    }
    return 0;
}
