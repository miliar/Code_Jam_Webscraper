#include <iostream>
#include <algorithm>
#include <stdlib.h>
# include <string.h>
#include <math.h>

using namespace std;

int main()
{
    int aa,c=1;
    string b;
    char ss[50],sss[50]="0";
    string s="0";
    cin>>aa;
   // 
    for(int t=0;t<aa;t++)
    {
            int a[21]={-1},bb[21]={-1};
            int f=0;
            bb[0]=0;
            cin >> s;
            for( int i=0 ;i< s.size() ; i++)
            {
                      a[f]=((int)s[i]-48);
                      bb[f+1]=((int)s[i]-48);
                      f++; 
                              
            }
            if( next_permutation(a,a+f))
            {
                cout<<"Case #"<<c<<": ";
                          
                   for(int j=0;j<f;j++)
                   {
                            cout<<a[j];
                           }
                           cout<<"\n";
                           c++;
                      
            }
           else
           {
           
               next_permutation(bb,bb+f+1);
                cout<<"Case #"<<c<<": ";
                for(int j=0;j<=f;j++)
                   {
                           cout<<bb[j];
                    }
                           cout<<"\n";
                           c++;
              
           }
    }
}

