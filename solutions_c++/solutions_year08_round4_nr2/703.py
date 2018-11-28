#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

int factorizable(long long k, long long N, long long M, long long* t1, long long* t2)
{
	
	long long R = N;

	if( M < N) { R = M;}

	long long t;

	for(t=1; t <= N; t++)
	{
		if(k%t == 0)
		{
			if(k/t <= M) { *t1 = t; *t2 = k/t; return 1; }
		}
	}

	return 0;
	
}

int main()
{
	int num_cases;
	int i;

	cin >> num_cases;

	for(i=0;i< num_cases;i++)
	{
		long long A;
		long long N,M;
		long long x2,x3,y2,y3;

		cin >> N;
		cin >> M;
		cin >> A;
		
		long long k;
		int possible = 0;

		if( A >= N*M)
		{

	   for(k = 0; k <= (A - N*M) ; k++)
		{
			if(A + k > N*M) { break;}
			else
			{
				if((factorizable(k,N,M,&x2,&y3 ) && (factorizable(A+k,N,M,&x3,&y2))))
				{
				possible = 1;
				break;
				}

			}

			

		}
		}
		else
		{
	   for(k = 0; k <= (N*M) ; k++)
		{
			if(A + k > N*M) { break;}
			else
			{
				if((factorizable(k,N,M,&x2,&y3 ) && (factorizable(A+k,N,M,&x3,&y2))))
				{
				possible = 1;
				break;
				}

			}

			

		}



		}

	if(possible)
	 cout << "Case #"<<i+1<<": "<<"0 0 "<<x2<<" "<< y2 <<" "<< x3 <<" "<<y3<<endl;
	else
	 cout << "Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;

	}
}
