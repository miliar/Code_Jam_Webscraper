#include<iostream>
#include<vector>
using namespace std;

const int MAXN = 128;

struct fraction
{
       int wins;
       int total;
       
       void cut()
       {
            int gcd = __gcd(wins, total);
            wins /= gcd;
            total /= gcd;
       }
};
fraction wp[MAXN];
fraction owp[MAXN];
fraction oowp[MAXN];

char matrix[MAXN][MAXN];
int t,n;
vector<int> opp[MAXN];

void calc_owp()
{
     fraction temp;
     for(int i = 0; i < n; i++)
     {
      owp[i].total = 1;
      owp[i].wins = 0;
      for(int j = 0; j < opp[i].size(); j++)
         {
              temp = wp[opp[i][j]];
              temp.total--;
              if(matrix[i][opp[i][j]] == '0') temp.wins--;
              
              owp[i].wins = owp[i].wins * temp.total + temp.wins * owp[i].total;
              owp[i].total *= temp.total;
              
              owp[i].cut();
         }
        
      owp[i].total *= wp[i].total;
      owp[i].cut();
     }
}

void calc_oowp()
{
     for(int i = 0; i < n; i++)
     {
             oowp[i].total = 1;
             oowp[i].wins = 0;
             for(int j = 0; j < opp[i].size(); j++)
                 {
                     oowp[i].wins = oowp[i].wins * owp[opp[i][j]].total + oowp[i].total * owp[opp[i][j]].wins;
                     oowp[i].total *= owp[opp[i][j]].total;
                     oowp[i].cut();
                 }
             oowp[i].total *= wp[i].total;    
             oowp[i].cut();
     }
}

int main()
{  
    int test = 1;
    scanf("%d", &t);
    while(test <= t)
    {
             memset(wp, 0, sizeof(wp));
             memset(owp, 0, sizeof(owp));
             memset(oowp, 0, sizeof(oowp));
             memset(matrix, 0, sizeof(matrix));
             for(int i = 0; i < MAXN; i++)
             {
                     opp[i].clear();
             }
             
            scanf("%d", &n);
            for(int i = 0; i < n; i++)
             for(int j = 0; j < n; j++)
             {
               cin>>matrix[i][j];
               if(matrix[i][j] != '.')
               {
                  opp[i].push_back(j);
                  wp[i].total++;
                  if(matrix[i][j] == '1') wp[i].wins++;              
               }
             } 
            
            calc_owp();
            calc_oowp();
            
            printf("Case #%d:\n", test);
            for(int i = 0; i < n; i++)
            {
                    wp[i].total *= 4;
                    wp[i].cut();
                    owp[i].total *= 2;
                    owp[i].cut();
                    oowp[i].total *= 4;
                    oowp[i].cut();
                    
                    fraction rpi = wp[i];
                    
                    rpi.wins = rpi.wins * owp[i].total + rpi.total * owp[i].wins;
                    rpi.total *= owp[i].total;
                    rpi.cut();
                    
                    rpi.wins = rpi.wins * oowp[i].total + rpi.total * oowp[i].wins;
                    rpi.total *= oowp[i].total;
                    rpi.cut();
                    
                    double RPI = (double)rpi.wins / (double)rpi.total;
                    cout << RPI << endl;
            }
            test++;
    }
    return 0; 
}
