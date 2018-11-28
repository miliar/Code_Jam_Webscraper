#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
	//freopen("A-small-attempt3.in", "r", stdin);
	//freopen("A-small-attempt3.out", "w", stdout);
	int T;
	bool estado[12];
	bool alterna[12];
	
	
	scanf("%d", &T);
	for (int caso = 0; caso < T; ++caso)
	{
		
		int N, K;
		memset(estado, 0, sizeof(estado));
		memset(alterna, 0, sizeof(alterna));
		alterna[0]=true;
		scanf("%d %d", &N, &K);	

		
		for (int y = 0; y < K; ++y)
		{
			estado[0] = !estado[0];
			for (int s = 1; s < N; ++s)
			{
				bool tmp = estado[s];
				if (estado[s-1]!=alterna[s])
				{
					alterna[s]=!alterna[s];
					if (!alterna[s]) 
						estado[s] = !estado[s];
				}else if (!estado[s]) break;
				
				
				
			}
			

		}
		bool b = true;
		for (int i = 0; i < N; ++i)
		{
			if (!estado[i])
			{
				b = false; break;
			}
		}

		if (b) printf("Case #%d: ON\n",caso+1);
		else printf("Case #%d: OFF\n",caso+1);
		
	}
	return 0;
}