#include<iostream>
#include<string>
using namespace std;
int main()
{
	int L, D, N, k = 0, s=0, count, case_count[10], i, j, l, f, check, c;
	char words[25][11], cases[10][3001], temp[10][100], t;
	cin >> L >> D >> N;
	for(i = 0; i<D; i++)
	{
		cin >> words[i];
	}
	for(i =0; i<N; i++)
	{
		cin >> cases[i];
	}
	for(i =0; i<N; i++)
	{
		case_count[i]=0;
		s=0;
		k=0;
		temp[s][0] = NULL;
		l = strlen(cases[i]);
		check = 0;
		for (j = 0; j <= l; j++)
		{
			if(cases[i][j] == '(')
			{
				check = 1;
			}
			else
				if(cases[i][j] == ')')
				{
					check = 0;
					k = 0;
					s++;
					temp[s][0] = NULL;
				}
			if(check == 1 && cases[i][j] != '(' && cases[i][j] != ')')
			{
				temp[s][k] = cases[i][j];
				k++;
				temp[s][k] = NULL;
			}
			else
				if(cases[i][j] != '(' && cases[i][j] != ')')
				{
					temp[s][k] = cases[i][j];
					temp[s][k+1] = NULL;
					s++;
					temp[s][0] = NULL;
				}
		}
		for(j = 0; j< D; j++)
		{
			count =0;
			for(k = 0; k< L; k++)
			{
				t = words[j][k];
				if(strlen(temp[k]) == 1)
				{
					if(t == temp[k][0])
					{
						count++;
					}
				}
				else
					if(strlen(temp[k]) >= 1)
					{
						for (c =0; c <= strlen(temp[k]); c++)
						{
							if(t == temp[k][c])
							{
								count++;
							}
						}
					}
				if(count == L)
				{
					case_count[i]++;
					count = 0;
				}
			}
		}
		cout<<"\nCase #" << i+1 <<": " << case_count[i];
	}
}