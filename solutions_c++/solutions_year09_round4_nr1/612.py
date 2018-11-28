#include <vector>
#include <queue>
#include <string>
#include <stdio.h>

using namespace std;


int main()
{
	int i,l,k,j,t,tmp;
	int T, N;
	char c;

	scanf("%d", &T);
	for (t=0; t<T; t++)
	{
		vector <int> v;
		scanf("%d", &N);
		for (i=0; i<N; i++)
		{
			k = 0;
			scanf("%c", &c);
			for (l=0; l<N; l++) 
			{
				scanf("%c", &c);
				if (c == '1') k = l;
				//printf("[%c]", c);
			}
			v.push_back(k);
		}
			
		int koszt = 0;
		for (i=0; i<N; i++)
		{

			//printf("\nv: ");
			//for (l=0; l<v.size(); l++) printf("%d ", v[l]);

			// szukamy pierwszej liczby ktora pasuje do wiersza 'i'
			for (l=i; l<N; l++) if (v[l] <= i)
			{
				// przesuwamy posrednie
				tmp = v[l];
				for (j=l; j>i; j--) v[j] = v[j-1];
				v[i] = tmp;
				koszt += l - i;
				break;
			}
		}
			
		printf("Case #%d: %d\n", t+1, koszt);
	}

	//scanf("%c", &c);
	//scanf("%d", &i);
	return 0;
}
