#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
int main()
{
   int tt;
   cin >> tt;
   for (int cc = 1; cc<= tt; cc++) {
      cout <<"Case #"<<cc<<":"<<endl;
      int h,w;
      cin >> h >> w;
      vector<string> VS;
      for (int i = 0 ; i < h; i++)
         {
            string tmp; cin >> tmp; VS.push_back(tmp);
         }
      for (int i = 0 ; i< h-1; i++)
        for (int j = 0 ; j< w-1; j++)
          if (VS[i][j]=='#') {
            if (VS[i][j] == VS[i][j+1] && VS[i+1][j] =='#' && VS[i+1][j+1] =='#') {
               VS[i][j] = VS[i+1][j+1] = '/';
               VS[i+1][j] = VS[i][j+1] = '\\';
            }
          }
     int flag = 0;
     for (int i = 0 ; i < h; i++)
       for (int j = 0 ; j < w; j++)
          flag += (VS[i][j]=='#');
     if (flag) cout <<"Impossible"<<endl; else {
       for (int i = 0 ; i <h; i++)
         cout << VS[i] << endl;
     } 
}
}
