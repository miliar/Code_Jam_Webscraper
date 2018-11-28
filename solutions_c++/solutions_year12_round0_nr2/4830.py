#include<iostream>
#include<conio.h>

using namespace std;

main()
{
     int T,S[100],p[100],N[100], score [100][100],count=0,sup,pos[3],tsc,i,j;
     cin>>T;
     for ( i=0; i<T;++i)
     {
         cin>>N[i];
         cin>>S[i];
         cin>>p[i];
         //int i=0,j;
         for ( j=0;j<N[i];++j)
             cin>>score[i][j];
     }
     //sup=S;
     for ( i=0;i<T;++i)
     {
         count=0;     
         for ( j=0;j<N[i];++j)
         {
              tsc=score[i][j]-p[i];
              if ( p[i]!=0 && score[i][j]==0)
                 continue;
              if ( (2*p[i]-4)>tsc )
              {
                  // cout<<p[i];
                 continue;
              }
              else if ( (2*p[i]-3 == tsc || 2*p[i]-4 == tsc ) )
              {
                   if ( S[i]>0 )
                   {
                        ++count;
                        --S[i];                        
                   }
              }
              else //if ( 2 * p[i] - 2 == tsc || 2 * p[i] == tsc || 2 * p[i] - 1 == tsc)
                   ++count;
         }
         cout<<"Case #"<<i+1<<": "<<count<<endl;
     }
//     cout<<count;
     //getch();
}
