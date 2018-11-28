#include<iostream>
#include<cstdlib>

using namespace std;

int main(){
    int test, n, s, p;
    
    cin>>test;
    
    for(int t=1; t<=test; t++)
    {
              cin>>n>>s>>p;
              int puntos;
              int y=0, sorpr=0;
              
              for ( int i=0; i<n; i++)
              {
                  cin>>puntos;
                  if (puntos%3 == 0)
                  {
                     if (puntos/3 >=p)
                        y++;
                     else if(puntos/3 +1 >=p && puntos/3 >0 && sorpr<s)
                     {
                          sorpr++;
                          y++;
                     }
                  }
                  else if (puntos%3 == 1)
                  {
                     if (puntos/3 >=p || puntos/3 +1 >=p)
                        y++;
                  }
                  else if (puntos%3 == 2)
                  {
                     if (puntos/3 >=p || puntos/3 +1 >=p)
                        y++;
    
                     else if(puntos/3 +1+1 >=p && puntos/3+1 >0 && sorpr<s)
                     {
                          sorpr++;
                          y++;
                     }
                  }
              }
       cout<<"Case #"<<t<<": "<<y<<endl;       
    }
    
    
    return 0;
}
