#include <iostream>
#include <iomanip>

#include <fstream>

using namespace std;

double in[100000];

double max(double a, double b)
{
       return a > b? a: b;
       }
int main()
{
    ifstream cin("1.in");
    ofstream fout("1.out");    
    int N;
    cin >> N;
    
    for(int t = 1; t <= N; t++)
    {
            int n;
            cin >> n;        
            double sum = 0.0;
            
            double x;
            
            for(int i = 0; i < n; i++)
            {
                    cin >> in[i];
                    sum += in[i];
            }
            
            cout << sum << endl;
            
            fout << "Case #" << t << ":";
            for(int i = 0; i < n; i++)
            {
                    double min = 9999999.0;
                    double c = in[i];
                    
                    for(int j = 0; j < n; j++)
                    {
                           if(i != j) {
                                if(in[j] < min)
                                {
                                         min = in[j];
                                }
                           } 
                    }
                    
                   // double ans = (min + sum - c) / 2 / sum;
                   double minans = 999999;
                   for(int j = 1; j <= n ; j++)
                   {
                    double ans = (2 * sum - c -(j - 1) *c )/ j/ sum;
                    if(minans > ans) minans = ans;
                   }
                    fout <<  setprecision (8)  << " " << max(0 , minans * 100);
//                    printf(" %.5f", ans * 100);
//                      printf("
            }   
            fout << endl;    
    }
    getchar();
}

