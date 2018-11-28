#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int te;
	cin >> te;
	for(int t=1 ; t<=te ; t++)
	{
		int base,opposed,N,k=0;
		char B[256][256] = {0}, L[500];
		char O[256] = {0};

		cin >> base;
		string str;
		for(int i=0 ; i<base ; i++)
		{
			cin >> str;
			B[str[0]][str[1]] = str[2];
			B[str[1]][str[0]] = str[2];
		}

		cin >> opposed;
		for(int i=0 ; i<opposed ; i++)
		{
			cin >> str;
			O[str[0]] = str[1];
			O[str[1]] = str[0];
		}

		cin >> N;
		cin >> str;
		
		k = 0;
		L[0] = str[0];
		for(int i=1 ; i<str.size() ; i++)
		{
			L[++k] = str[i];
			while(k > 0 && B[L[k]][L[k-1]])
			{
				char a = L[k--];
				char b = L[k--];
				L[++k] = B[a][b];
			}	
			if(k > 0)
			{
				for(int i=0 ; i<k  ; i++)
					if(O[L[k]] == L[i])
						k = -1;
			}
		}
		cout << "Case #" << t << ": ";
		cout << "[";
		string sep = "";
		for(int i=0 ; i<=k ; i++)
		{
			cout << sep << L[i];
			sep = ", ";
		}
		cout << "]\n";
	}
}
