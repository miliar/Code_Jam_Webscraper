#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
   int TT;
   cin >> TT;
   for (int TTT = 1; TTT<=TT; TTT++) {
     cout << "Case #"<<TTT<<":"<< endl;
     int n;
     vector<string> VS;
     string T;
     cin >> n;
     for (int i = 0 ; i < n ; i++) {
       cin >> T;
       VS.push_back(T);
     }
     double WP[1000];
     int BB[1000];
     int DD[1000];
     double OWP[1000];
     double OOWP[1000];
     for (int i = 0 ; i<n ; i++)  {
       int A=0,B=0;
       for (int j = 0 ; j <n ; j++) {
         if (VS[i][j]=='1' || VS[i][j]=='0') A++;
         if (VS[i][j]=='1' ) B++;         
       }
       WP[i] = B*1.0/A; BB[i] = A; DD[i] = B;
     }
     for (int i = 0 ; i <n ;i++) {    
        double sum = 0.0;
        for (int j = 0 ; j<n; j++)
          if (VS[i][j]=='1' || VS[i][j]=='0')
            sum+=(DD[j]-(VS[j][i]-'0'))*1.0/(BB[j]-1);
          OWP[i] = sum/BB[i];
     }
     for (int i = 0 ; i <n ;i++) {    
        double sum = 0.0;
        for (int j = 0 ; j<n; j++)
          if (VS[i][j]=='1' || VS[i][j]=='0')
            sum+=OWP[j];
          OOWP[i] = sum/BB[i];
     }
     for (int i = 0 ; i <n ; i++)
     {
       printf("%.8lf\n",WP[i]*0.25+OWP[i]*0.5+OOWP[i]*0.25);
     }
   }
}
