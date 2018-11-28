#include<stdio.h>
#include<map>
#include<vector>
#include<string>
#include<iostream>

using namespace std;

int main()
{
	int ncase,ccase;
	int x,y,z;
	map<char,int> btb;
	map<int,char> itb;
	int A[8][8],B[8][8];
	string s;
	int it;
	string El;
	char temp;
	
	cin >> ncase;
	for(ccase = 1;ccase <= ncase;ccase++)
	{
	
		btb.clear();
		btb['Q'] = 0;
		btb['W'] = 1;
		btb['E'] = 2;
		btb['R'] = 3;
		btb['A'] = 4;
		btb['S'] = 5;
		btb['D'] = 6;
		btb['F'] = 7;
		
		for(x = 0;x < 8;x++)
		{
			for(y = 0;y < 8;y++)
			{
				A[x][y] = 0;
				B[x][y] = 0;
			}
		}
		
		it = 8;
		cin >> x;
		for(y = 0;y < x;y++)
		{
			cin >> s;
			itb[it] = s[2];
			A[btb[s[0]]][btb[s[1]]] = it;
			A[btb[s[1]]][btb[s[0]]] = it;
			btb[s[2]] = it;
			it++;
		}
		
		cin >> x;
		for(y = 0;y < x;y++)
		{
			cin >> s;
			B[btb[s[0]]][btb[s[1]]] = -1;
			B[btb[s[1]]][btb[s[0]]] = -1;
		}
		
		cin >> x >> s;
		El.clear();
		for(y = 0;y < x;y++)
		{
			El += s[y];
			if(El.size() > 1)
			{
				if(btb[El[El.size() - 1]] < 8 && btb[El[El.size() - 2]] < 8)
				{
					if(A[btb[El[El.size() - 1]]][btb[El[El.size() - 2]]] > 7)
					{
						temp = itb[A[btb[El[El.size() - 1]]][btb[El[El.size() - 2]]]];
						El = El.substr(0,El.size() - 2) + temp;
					}
				}
			}
			
			for(z = El.size() - 2;z >= 0;z--)
			{
				if(btb[El[El.size() - 1]] < 8 && btb[El[z]] < 8)
				{
					if(B[btb[El[El.size() - 1]]][btb[El[z]]] == -1)
					{
						El = "";
					}
				}
			}
		}
		
		cout << "Case #" << ccase << ": [";
		for(x = 0;x < El.size();x++)
		{
			cout << El[x];
			if(x < El.size() - 1) cout << ", ";
		}
		cout << "]" << endl;
	}

    while(getchar()!=EOF);
    return 0;
}
