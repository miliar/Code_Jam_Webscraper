#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char map[105][105];
double wp[105];
double owp[105];
double oowp[105];
int sum[105];
int num[105];

double RPI[105];
void cal(int test)
{
     int n,i,j;
     int d;
     double s;
     double dnum, dsum;
     scanf ("%d", &n);
     for (i = 0; i < n; i++)
     {
         scanf ("%s", map[i]);
     }
     //wp
     for (i = 0; i < n; i++)
     {
         num[i] = 0; sum[i] = 0;
         for (j = 0; j< n; j++)
         {
             if (map[i][j]!='.')
             {
                 sum[i]++;
                 if (map[i][j] == '1')
                 num[i]++;
             }  
         }
         wp[i] = (num[i] * 1.0)/ (sum[i] *1.0);
     }
     //owp
     for (i = 0; i < n; i++)
     {
         s =0;
         for (j = 0; j< n; j++)
         {
              if (map[i][j]!='.')
             {
                 d = num[j];
                 if (map[j][i] == '1')
                 {
                     s += (d - 1.0) * 1.0 / ((sum[j] -1.0)*1.0);
                 }
                 else
                 {
                     s += d * 1.0 /((sum[j]-1.0) * 1.0);
                 }
                 
                 
             }  
         }
         owp[i] = s/(sum[i] * 1.0); 
     }
     //oowp
     for (i = 0; i < n; i++)
     {
         s = 0;
         for (j = 0; j < n; j++)
         {
             if (map[i][j] != '.')
             {
                 s += owp[j];
             }
         }
         oowp[i] = s/ (sum[i] * 1.0) ; 
     }
     
     //RPI
     for (i = 0; i < n; i++)
     {
         RPI[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
     }
     printf ("Case #%d:\n", test);
    for (i = 0; i< n; i++)
     {
         printf ("%.15lf\n", RPI[i]);
     }
    
  
   
     
}

int main()
{
   int T,i;
   freopen("A-large.in", "r", stdin);
     freopen("A-large.out", "w", stdout);
     scanf("%d", &T);
    for (i = 1; i<= T; i++)
    {
       cal(i);
    }
  
   // system("pause");
    return 0;
}
