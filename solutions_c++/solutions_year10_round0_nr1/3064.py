#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

#define ULL unsigned long long

ULL power2[] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824 };

int main()
{
    int T, Case = 0;
    int N;
    long K;
    string s;
    ULL i,t;
    
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("2.out","w",stdout);

    freopen("A-large.in","r",stdin);
    freopen("large.out","w",stdout);

    
    cin >> T;
    while(Case < T)
    {
              cin >> N >> K;
              if(K == 0)
                   s = "OFF";
              else
              {
                  if( (K+1) == power2[N] )
                      s = "ON";
		  else if( (K+1) < power2[N] )
		       s = "OFF";
                  else
		  {
			for(s = "OFF",i = 2,t = power2[N]; t <= (K + 1);i++)
			{
				t = i * power2[N];
				if( t > (K + 1) )
				{
					s = "OFF";
					break;
				}
				else if( t == (K+1) )
				{
					s = "ON";
					break;
				}
			}
		  }
             }
	     cout << "Case #" << ++Case << ": " <<  s << endl;
    }    
    return 0;    
}
