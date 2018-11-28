#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int TC = 1, T, NC = 1, N, C, CC, D, DC;
char com[9][9];
int opp[9][9];
char L[102];
char str[10]={};
//enum ele{'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'}ELE;

int ch2num(char ch)
{
	switch (ch)
	{
	case 'Q': return 0; break;
	case 'W': return 1; break;
	case 'E': return 2; break;
	case 'R': return 3; break;
	case 'A': return 4; break;
	case 'S': return 5; break;
	case 'D': return 6; break;
	case 'F': return 7; break;
	default:  return 8;
	}
}


int main ()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	for (cin>>T; TC <= T; TC++)
    {
		memset(com, ' ', 81*sizeof(char));
		memset(opp, 0, 81*sizeof(int));
		memset(L, 0, 102*sizeof(char));
		for (cin>>C, CC = 0; CC < C; CC++)
		{
			cin>>str;
			com[ch2num(str[0])][ch2num(str[1])] = str[2];
			com[ch2num(str[1])][ch2num(str[0])] = str[2];
		}
		for (cin>>D, DC = 0; DC < D; DC++)
		{	cin>>str;
			opp[ch2num(str[0])][ch2num(str[1])] = 1;
			opp[ch2num(str[1])][ch2num(str[0])] = 1;
		}
		char ch;
		memset(L, 0, 102*sizeof(char));
		cin>>N;
		getchar();cin>>L[0];
		for (NC = 1; NC < N; NC++)
		{
			cin>>ch;
			int i = ch2num(ch), j = ch2num(L[strlen(L)-1]);

			if (com[i][j]!=' ')
				L[strlen(L)-1] = com[i][j];
			else if (com[j][i]!=' ')
				L[strlen(L)-1] = com[j][i];
			else
			{
				int k = 0, flag = 1;
				while (k< strlen(L) && flag)
				{
					if (ch2num(L[k])!=-1)
						if (opp[i][ch2num(L[k])] == 1)
						{
							memset(L, 0, 102*sizeof(char));
							flag = 0;
						}
					k++;
				}
				if (flag)
					L[strlen(L)] = ch;
			}
		}


		printf ("Case #%d: [", TC);
		if (strlen(L))
			cout<<L[0];
		for (int k = 1; k<strlen(L);k++)
		{
			printf(", %c", L[k]);
		}
		printf ("]\n");
    }
	fclose(stdin);
	fclose(stdout);
    return 0;
}


