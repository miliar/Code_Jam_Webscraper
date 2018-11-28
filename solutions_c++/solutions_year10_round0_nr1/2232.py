#include <iostream>
using namespace std;

int main()
{
	int T; 
	scanf("%d", &T);
	
	for(int t=1; t <= T; ++t)
	{
		bool isOn=true;

		int N,K;
		scanf("%d %d", &N, &K);

		for(int i=0; i < N; ++i)
			if( !(K & (1<<i)) )
				isOn=false;
		
		printf("Case #%d: %s\n", t, isOn==true ? "ON" : "OFF");
	}

	return 0;
}