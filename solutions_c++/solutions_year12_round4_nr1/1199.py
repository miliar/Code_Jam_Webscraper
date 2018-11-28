#include <iostream>
#include <iomanip>

#include <fstream>

using namespace std;



       long long max(long long a, long long b)
       {
            if(a > b) return a;
            else return b;
        }
       
long long f[100001];
long long dist[100001];
long long length[100001];


bool DP(int n, int all)
{       
        //cout << n << " " << all << endl;
        memset(f, 0, sizeof(f));    
      f[0] = min(length[0],dist[0]);
       if ( 2*f[0] >= all ){
                       return true;
      }
    for(int i = 0; i < n; i++)
    {
      int j;
      for (j=i+1;j<n;j++)
      {
         if ( dist[i] + f[i] >= dist[j] )
         {
           int temp = min( dist[j] - dist[i] , length[j] );
           f[j] = max(f[j],temp);
           if ( f[j] + dist[j] >= all )
           {
             //ans = true;
             return true;
           }
         }
         else break;     
      }
    }   
    
    return false;
}


int main()
{
    ifstream cin("1.in");
    ofstream fout("1.out");    
    int N;
    cin >> N;
    
    for(int t = 1; t <= N; t++)
    {
            fout << "Case #"<< t <<": ";
            int n;
            cin >> n;
             int all = 0;
            for(int i = 0; i < n; i++)
            {
                    cin >> dist[i] >> length[i];

            }
            cin >> all;
                    
                    if(DP(n, all)) 
                    {
                     fout << "YES"<< endl;
                    }
                    else fout << "NO" << endl;


    }
    getchar();
}

