#include <string>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;
int main()
{
	int T;
	cin >> T;
	int CASE = 1;
	while(T--)
	{
		int C, D, N;
		cin >> C;
		string strC = "***";
		if( C == 1 )
			cin >> strC;
		string strD = "***";
		cin >> D;
		if( D == 1 )
			cin >> strD;
		cin >> N;
		string s;
		cin >> s;
		vector<char> L;
		for(int i = 0 ; i < N; i++)
		{
			if( L.size() == 0)
				L.push_back(s[i]);
			else
			{
				if( (L.back() == strC[0] && s[i] == strC[1]) || (L.back() == strC[1] && s[i] == strC[0]) )
				{
					L.pop_back();
					L.push_back(strC[2]);
				}
				else
				{
					L.push_back(s[i]);
				}
				bool op = false;
				for(int j = 0; j < L.size(); j++)
					for(int k = j + 1 ; k < L.size(); k++)
					{
						if( (L[k] == strD[0] && L[j] == strD[1]) || (L[k] == strD[1] && L[j] == strD[0]) )
							op = true;
					}
				if( op )
					L.clear();
			}
		}
		
		printf("Case #%d: [", CASE);

		for(int i = 0 ; i < L.size(); i++)
		{
			if( i == L.size() - 1 )
				cout<<L[i];
			else
			cout<<L[i]<<", ";
		}
		cout<<"]"<<endl;
		CASE++;
	}
}