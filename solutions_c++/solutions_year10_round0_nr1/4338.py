#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
using namespace std;

void read(char *a)		{	freopen(a,"r",stdin);	}
void write(char *a)		{	freopen(a,"w",stdout);	}
//-----------------------------------------------------------------

int main()
{
    int T;
    //read("A-small-attempt3.in");
    //write("A-small-attempt3.out");
    while(cin >> T)
    {
              int i = 1 ;
              //while(T--)
              for(i = 1 ; i <= T ; i++)
              {
                  int N ,K , f = 0 ;
                  cin >> N >> K ;
                  cout << "Case #" << i << ": " ;
                  int sum = (1 << N) ;
                  if(sum > K + 1)
                  {
                      cout << "OFF" << endl;
                      f = 1 ;
                  }
                  else
                  {
                      for(int k = 1 ;  k < 500000 ; k++)
                      {    
                          if(k * sum - 1 == K )
                          {
                               cout << "ON" << endl;
                               f = 1 ;   
                               break ;
                          }
                      }
                  }
                  if(!f)
                  {
                          cout << "OFF" << endl;
                  }          
              }          
    }
    return 0;
}
