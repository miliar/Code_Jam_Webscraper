#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

#include <stdio.h>

int l , d , n , f , i , j , k , record[5500] , s[550] , ans[550] , t , old;
char dic[5500][20] , ques[550][500];



int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);

	cin >> l >> d >> n;
	f = 1;
	memset(ans , 0 , 550);
	for(i = 0 ; i < d ; i++)
	{
		cin >> dic[i];
		record[i] = 0;
	}
	for(i = 0 ; i < n ; i++)
	{
		cin >> ques[i];
		s[i] = 0;
		for(j = 0 ; j < strlen(ques[i]) ; j++)
		{
			if(ques[i][j] == '(')
			{
				s[i]++;
			}
		}
	}

	for(i = 0 ; i < n ; i++)
	{
		for(j = 0 ; j < d; j++)
		{
			t = 0;
			for(k = 0 ; k < l ; k++)
			{
				old = record[j];
				if(ques[i][t] == '(')
				{
					while(ques[i][t] != ')')
					{
						if(ques[i][t] == dic[j][k])
						{
							record[j]++;
							t++;
						}
						else
						{
							t++;
						}
					}
					t++;
				}
				else
				{
					if(ques[i][t] == dic[j][k])
					{
						record[j]++;
						t++;
					}
					else
					{
						t++;
					}
				}

				
				if(old == record[j])
				{
					break;
				}
			}
		}

		for(j = 0 ; j < d; j++)
		{
			if(record[j] == l)
			{
				ans[i]++;
				//cout << dic[j] << endl;
			}
		}
		//cout << "Case #" << f << ": "<<ans[i] << endl;
		printf("Case #%d: %d\n" , f , ans[i]);
		f++;
		memset(record , 0 ,5500);

	}

	return 0;
}


