#include<iostream>
#include<algorithm>
#include<vector>
#include<sstream>
using namespace std;

int p3[14];
int yes ( long long k  )
{

    if( k <0 ) k*=-1;
      //  cout<<"Val = "<< k<<endl;
     return  ( k %2 == 0 ) ||             
             ( k %3 == 0 ) || 
             ( k %5 == 0 ) || 
             ( k %7 == 0 ) ;
}
int main ()
{
    p3[0] = 1;
    for (int i = 1; i<14; i++) p3[i] = 3*p3[i-1];
    int tc ; 
    cin>>tc;
    for( int cse = 1; cse <= tc; cse ++)
    {
         string a;
         cin>>a;
    
         int ans = 0;
         if( a.size() == 1 ) 
          {
             istringstream in (a); int k ; in>>k;
             ans |= yes(k);
          }
         else 
         {
              long long get[100][100];
              for( int len = 1; len <= (int)a.size(); len++)
              {
                   for( int i =0 ; i + len -1 < (int)a.size(); i++)     
                   {
                        istringstream in ( a.substr( i, len ));
                        in>>get[i][len];     
                      //  cout<<get[i][len]<<" "<<endl;
                   }
                  // cout<<endl;
              }
             for( int i = 0 ; i<p3[a.size()-1]; i++)   // 0 for space, 1 for + , 2 for -
             {
                  int last = 0; int sign = 1; long long x = 0; long long sum = 0;
                  for(int j = 0; j< (a.size()-1); j++)
                  {
                          if( (i / p3[j] )%3 ==0 ) continue;
                         
                          x = get[last][j - last + 1]; 
                       //   cout<<x<<" "<<a.substr(last, j-last+1);
                          sum += sign * x;
                          last = j+1;

                          if( (i / p3[j] )%3 ==1 )
                          {
                             sign = 1;                            
                          }
                          else if( (i / p3[j] )%3 ==2 )
                          {
                             sign = -1;
                          }
                       //   cout<< ( sign == 1 ? " + " : " - " );
                  }
                  x = get[ last][a.size() - last ]; 
                //  cout<<x<< " "<< a.substr( last, a.size()-last + 1 )<<endl;
                  sum += sign * x;
                  ans += yes ( sum );        
             }
          }
          cout<<"Case #"<<cse<<": "<<ans<<endl;
    }
return 0;    
}
