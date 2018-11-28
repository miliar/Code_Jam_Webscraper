#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int t, n1, n2, n3;
int main()
{
	scanf("%d",&t);
	char comb[100][5];
	char del[100][100];
	char str[1000];
	for(int i = 0; i < t; i++)
	{
		scanf("%d",&n1);
		for(int j = 0; j < n1; j++)
		{
			scanf("%s",comb[j]);
		}
		scanf("%d",&n2);
		for(int j = 0; j < n2; j++)
		{
			scanf("%s",del[j]);
		}
		scanf("%d",&n3);
		scanf("%s",str);
		printf("Case #%d: ",i+1);
		for(int j = 0; j < n1; j++)
		{
			comb[j+n1][0] = comb[j][1];
			comb[j+n1][1] = comb[j][0];
			comb[j+n1][2] = comb[j][2];
		}
		for(int j = 0; j < n2; j++)
		{
			del[j+n2][0] = del[j][1];
			del[j+n2][1] = del[j][0];
			del[j+n2][2] = del[j][2];
			del[j+n2][3] = '\0';
		}
		n2 *= 2;
		n1 *= 2;
		int delativo[1000];
		memset(delativo, -1, sizeof(delativo));
		char saida[1000];
		int ssaida[1000];
		int cor = 0;
		for(int j = 0; str[j]; j++)
		{
			bool varc = false;
			for(int k = 0; k < n2; k++)
			{
				if(str[j] == del[k][1] && delativo[k] != -1)
				{
					cor = 0;
					memset(delativo, -1, sizeof(delativo));
					varc = true;
					break;
				}
			}
			if(varc)
				continue;
			for(int k = 0; k < n1; k++)
			{
				if(comb[k][0] == str[j] && comb[k][1] == str[j+1])
				{
					ssaida[cor] = j;
					saida[cor++] = comb[k][2];
					j++;
					varc = true;
					break;
				}
			}
			if(varc)
				continue;
			for(int k = 0; k < n2; k++)
			{
				if(del[k][0] == str[j] && delativo[k] == -1)
				{
					delativo[k] = j;
				}
			}
			ssaida[cor] = j;
			saida[cor++] = str[j];
		}
		if(cor)
			printf("[%c",saida[0]);
		else
			printf("[");
		for(int j = 1; j < cor; j++)
		{
			printf(", %c",saida[j]);
		}
		printf("]\n");
		fflush(stdout);
	}
	return 0;
}
