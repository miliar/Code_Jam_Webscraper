#include<fstream>
#include<string.h>
#include<iostream>
using namespace std;
main()
{
      fstream fout;
      fout.open("barsha.txt");
      int t,n,i,j,a[105],s,p, maxp, minp,count,flag;
      scanf("%d", &t);
      for(j=1;j<=t;j++)
      {
         count=0;
         flag=0;
         fout<<"Case #"<<j<<": ";
         scanf("%d", &n);          
         scanf("%d", &s);          
         scanf("%d", &p);
         for(i=0;i<n;i++)          
            scanf("%d", &a[i]);
         maxp=p+ max(p-1, 0)*2;
         minp=p+ max(p-2, 0)*2;
         for(i=0;i<n;i++) 
            {
            if(a[i]>=maxp) count++;
            else if(a[i]>=minp) flag++;
            }
         count=count+min(s,flag);
         fout<<count<<"\n";
      }
}
