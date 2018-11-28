#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int o = 1,b = 1,t = 0, oCanGo = 0, bCanGo = 0;
    int T, N;
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    cin>>T;
    char name;
    int place;
    int step;
    int i;
    for(i = 1; i <= T; i++)
    {
            cin>>N;
            while(N > 0)
            {
              cin>>name>>place;
              if(name == 'O'){
                      step = abs(place - o);
                      if(step > oCanGo){
                              step -= oCanGo;
                              t += step;
                      }
                      else
                          step = 0;
                      t += 1;
                      bCanGo += (step + 1);
                      oCanGo = 0;
                      o = place;
              }
              else{
                   step = abs(place - b);
                   if(step > bCanGo){
                           step -= bCanGo;
                           t += step;
                   }
                   else
                       step = 0;
                   t += 1;
                   oCanGo += (step + 1);
                   bCanGo = 0;
                   b = place;
              }
              N--;      
            }
            cout<<"Case #"<<i<<": "<<t<<endl;
            t = 0;
            o = 1;
            b = 1;
            oCanGo = 0;
            bCanGo = 0;
    }
    return 0;
}
