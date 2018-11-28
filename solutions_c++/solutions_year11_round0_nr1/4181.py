#include <string>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;
int abs(int n)
{
	return n < 0 ? -n : n;
}
int main()
{
	int T;
	cin >> T;
	int CASE = 1;
	int N;
	char tmp1;
	int tmp2;
	while(T--)
	{
		vector<char> color;
		vector<int> button;
		cin >> N;
		for(int i = 0 ; i < N; i++)
		{
			cin >> tmp1 >> tmp2;
			color.push_back(tmp1);
			button.push_back(tmp2);
		}
		int C = 0;
		int pos_orange = 1;
		int pos_blue = 1;
		int saved_orange = 0;
		int saved_blue = 0;
		for(int i = 0 ; i < color.size(); i++)
		{
			if( color[i] == 'O' ){

					int diff = max( 0, abs(button[i] - pos_orange ) - saved_orange );
					C += diff + 1;
					saved_blue += diff + 1;
					pos_orange = button[i];	
					saved_orange = 0;
			}
			else
			{
				int diff = max( 0, abs(button[i] - pos_blue ) - saved_blue );
				C += diff + 1;
				saved_orange += diff + 1;
				pos_blue = button[i];
				saved_blue = 0;
			}
		}
		printf("Case #%d: %d\n", CASE, C);
		CASE++;
	}
}