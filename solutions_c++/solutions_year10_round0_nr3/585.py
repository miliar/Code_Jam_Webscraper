#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;
const int MAXN = 1000;

int main()
{
	int iTests;
	scanf("%d", &iTests);
	ll grupy[ MAXN ], ileMozeZabrac[ MAXN ], nowyPoczatek[ MAXN ], prevZebral[ MAXN ];
	ll dlugosc[ MAXN ];

	for(int iTestCnt=1; iTestCnt<=iTests; iTestCnt++)
	{
		ll R,k,N;
		scanf("%lld%lld%lld", &R,&k,&N);
		for(int i=0;i<N;i++)
			scanf("%lld", &grupy[i]);

		for(int iPocz=0; iPocz<N; iPocz++)
		{
			ileMozeZabrac[ iPocz ] = grupy[ iPocz ]; // z zalozenia grupy[ iPocz ] <= k
			int iNext = (iPocz+1)%N;

			while( iNext != iPocz && ileMozeZabrac[ iPocz ] + grupy[ iNext ] <= k )
			{
				ileMozeZabrac[ iPocz ] += grupy[ iNext ];
				iNext = (iNext+1)%N;

			}
			nowyPoczatek[ iPocz ] = iNext;
			//printf("ileMozeZabrac: %lld\n", ileMozeZabrac[iPocz]);
		}

		for(int iPocz=0; iPocz<N; iPocz++)
		{
			prevZebral[ iPocz ] = ileMozeZabrac[ iPocz ];
			dlugosc[ iPocz ] = 1;
			int iNext = nowyPoczatek[ iPocz ];

			while( iNext != iPocz )
			{
				prevZebral[ iPocz ] += ileMozeZabrac[ iNext ];
				iNext = nowyPoczatek[ iNext ];
				dlugosc[ iPocz ]++;
				if( dlugosc[ iPocz ] > N )
					break;
			}
		}

		ll llEuros = 0;
		int pocz = 0;
		while( dlugosc[pocz] > N && R )
		{
			llEuros += ileMozeZabrac[ pocz ];
			pocz = nowyPoczatek[ pocz ];
                        R--;
		}
		llEuros += R/dlugosc[pocz]*prevZebral[pocz];
		for(int i=0; i<R%dlugosc[pocz]; i++)
		{
			llEuros += ileMozeZabrac[pocz];
			pocz = nowyPoczatek[ pocz ];
		}

		printf("Case #%d: %lld\n", iTestCnt, llEuros);

	}
	return 0;
}
