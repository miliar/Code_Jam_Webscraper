#include<iostream>
#include <fstream>
using namespace std;
void main()
{
     int a[2][11],i,j,h,k,t,n;
     ifstream myfile ("A-small-attempt1.in");
     ofstream output ("A-small.output");
     if (myfile.is_open())
     {
       do
       {
       myfile>>t;
       for(h=0;h<t;h++)
       {
          myfile>>n;
          myfile>>k;
          for(i=0;i<2;i++)
          {
              for(j=0;j<n;j++)
              {
                  a[i][j]=0;
              }
          }
          a[0][0]=1;
          for(i=1;i<=k;i++)
          {
               for( j=0;j<n;j++)
               {
                       if(a[0][j]==1)
                       {
                                     if(a[1][j]==1)
                                     {
                                                   a[1][j]=0;
                                     }
                                     else a[1][j]=1;
                       }
                       if(j!=0)
                       {
                               if(a[1][j-1]==1 && a[0][j-1]==1)
                               a[0][j]=1;
                               else a[0][j]=0;
                       }
               }
          }
          if(a[0][n-1]==1 && a[1][n-1]==1)
          output<<"Case #"<<h+1<<": ON"<<endl;
          else output<<"Case #"<<h+1<<": OFF"<<endl;
     }
     }while (! myfile.eof() );
    myfile.close();
    output.close();
  }

  else cout << "Unable to open file"; 
     
}
     
