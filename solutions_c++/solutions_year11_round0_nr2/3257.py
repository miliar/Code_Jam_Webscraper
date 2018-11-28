#include<iostream>
using namespace std;
char com[40][4];
char opp[30][3];
int main()
{
	freopen("A.txt", "w", stdout);
	int t , temp ,  c , d , n , l , k;
	char in[101];
	char result[101];
	cin >> t;
	for(temp = 0; temp < t ; temp++)
	{
		cin >> c;
		for(n = 0; n < c; n++)
			cin >> com[n];
		cin >> d;
		for(n = 0; n < d; n++)
			cin >> opp[n];
		cin >> l >> in;
		int top_r = 1 , flag = 1;
		result[0] = in[0];
		k = 1;
		while(k < l)
		{
			if(top_r == 0)
			{
				result[top_r++] = in[k++];
				continue;
			}
			flag = 1;
			for(int o = 0; o < c && flag == 1; o++)
			{
				if(com[o][0] == in[k])
				{
					if(com[o][1] == result[top_r - 1])
					{
						flag = 0;
						k++;
						result[top_r - 1] = com[o][2];
						break;
					}
				}
				else if(com[o][1] == in[k])
					if(com[o][0] == result[top_r - 1])
					{
						flag = 0;
						k++;
						result[top_r - 1] = com[o][2];
						break;
					}
			}
			for(int o = 0; o < d && flag == 1; o++)
			{
				if(opp[o][0] == in[k])
					for(int u = 0; u < top_r; u++)
					{
						if(opp[o][1] == result[u])
						{
							flag = 0;
							k++;
							top_r = 0;
							break;
						}
					}
				else if(opp[o][1] == in[k])
					for(int u = 0; u < top_r; u++)
					{
						if(opp[o][0] == result[u])
						{
							flag = 0;
							k++;
							top_r = 0;
							break;
						}
					}
			}
			if(flag == 1)
				result[top_r++] = in[k++];
		}
		cout << "Case #" << temp + 1 << ": [";
		if(top_r == 0)
			cout << "]" << endl;
		else
		{
			cout << result[0];
			for(int o = 1; o < top_r; o++)
				cout << ", " << result[o];
			cout << "]" << endl;
		}
	}
	return 0;
}