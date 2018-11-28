#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>

#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;


char G[128][128];
int N;
double res[128], WP[128], OWP[128], OOWP[128];
double wp(int i, int k)
{
    int x = 0, y = 0, j;
   for(j = 0; j < N; ++j)
	   if(j != k) {
		   {
			   if(G[i][j] != '.') {
				   ++x;
			   }
			   if(G[i][j] == '1') {
				   ++y;
			   }
		   }
	   }
   return y * 1.0 / x;    
}

void exec()
{
     int i, j, k;
     for(i = 0; i < N; ++i)
     {
           
         WP[i] = wp(i, -1); 
     }
     for(i = 0; i < N; ++i)
     {
         int t = 0;
         double sum = 0;
         for(j = 0; j < N; ++j) if(G[i][j] != '.')
		 {
             t++;
             sum += wp(j, i);
         }
         OWP[i] = sum / t;
     }
     for(i = 0; i < N; ++i)
     {
         int t = 0;
         double sum = 0;
         for(j = 0; j < N; ++j) if(G[i][j] != '.')
         {
             t++;
             sum += OWP[j];
         }
         OOWP[i] = sum / t;
     }
     for(i = 0; i < N; ++i)
     {
           res[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
     }
}


int main()
{
    freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
    int i, j, k;
    int T, c = 0;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &N);
		for(i = 0; i < N; ++i) {
            scanf("%s", G[i]);
		}
        exec();
        printf("Case #%d:\n", ++c);
        for(i = 0; i < N; ++i)
            printf("%.12lf\n", res[i]);
    }
	return 0;
}

