#include <iostream>

using namespace std;

#define LL long long

int main()
{
	int C;
	scanf("%d" , &C);
	
	for(int cnum = 1 ; cnum <= C ; cnum ++)
	{
		LL N , K , X;
		scanf("%Ld %Ld" , &N , &K);
		
		X = 1 << N;
		if(K % X == X - 1)
			printf("Case #%d: ON\n" , cnum);
			
		else
			printf("Case #%d: OFF\n" , cnum);
	}
	
	return 0;
}
