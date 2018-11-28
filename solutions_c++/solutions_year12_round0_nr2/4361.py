
#include <iostream>
#include <fstream>
#include <math.h>
#include<vector>
#include<map>
#include<list>
// #include <conio.h>

using namespace std;

const int MAX = 100;

int main()
{
    ifstream cin("in.in");
    ofstream cout("out.out");
        
    int t;
    cin >> t;
    for (int ind = 1; ind <= t; ind++) {
    
        int N,S,p,g, result = 0;
        int g_div, g_mod;
        cin >> N >> S >> p;
        
        for(int i = 0; i < N; i++) {
                cin >> g;
                g_div = g/3;
                g_mod = g%3;
                if(g_div >= p) {
                    result++;
                } else {
                   if(g_mod == 1) {
                       if(g_div + 1>= p) {
                                result++;
                       }
                   } else if(g_mod == 2) {
                      if(g_div + 1>= p) {
                                result++;
                      } else if(S > 0 && g_div + 2 >= p) {
                                  result++;
                                  S--;
                      }
                   } else {
                        if(S > 0 && g_div + 1>= p && g_div > 0) {
                             result++;
                             S--;
                        }
                   }
                }
        }
            
        cout << "Case #" << ind << ": " << result << endl;
    }
    
   // getch();
    return 0;
}
