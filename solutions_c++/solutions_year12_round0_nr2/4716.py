#include<iostream>
#include<conio.h>

using namespace std;

main()
{
     int T,S[100],p[100],N[100], scr [100][100],cnt=0,sup,pos[3],t,i,j;
     cin>>T;
     for ( i=0; i<T;++i){
         cin>>N[i];
         cin>>S[i];
         cin>>p[i];
         for ( j=0;j<N[i];++j)
             cin>>scr[i][j];
     }
     
     for(i=0;i<T;++i){
         cnt=0;     
         for(j=0;j<N[i];++j)
         {
              t=scr[i][j]-p[i];
              if (p[i]!=0 && scr[i][j]==0) continue;
              if ((2*p[i]-4)>t)
              {
                 continue;
              }
              else if ((2*p[i]-3 == t || 2*p[i]-4 == t)){
                   if (S[i]>0){
                       ++cnt;
                       --S[i];                        
                       }
                   }
              else 
                   ++cnt;
                   }
         cout<<"Case #"<<i+1<<": "<<cnt<<endl;
         }
}
