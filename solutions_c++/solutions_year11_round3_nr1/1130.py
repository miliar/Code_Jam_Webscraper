#include<stdio.h>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

vector<string> A;
int h,w;
int m;
void convertor(int y,int x)
{
	A[y][x] = '/';
	if(y + 1 < h)
	{
		if(A[y + 1][x] == '#') A[y + 1][x] = '\\';
		else m = 0;
	}
	else m = 0;
	if(x + 1 < w)
	{
		if(A[y][x + 1] == '#') A[y][x + 1] = '\\';
		else m = 0;
	}
	else m = 0;
	if(m == 1)
	{
		if(A[y + 1][x + 1] == '#') A[y + 1][x + 1] = '/';
		else m = 0;
	}
}

int main()
{
	string s;
	int ncase,ccase;
	int x,y,z;
	
	cin >> ncase;
	for(ccase = 1;ccase <= ncase;ccase++)
	{
		cin >> h >> w;
		
		A.clear();
		getline(cin,s);
		for(x = 0;x < h;x++)
		{
			getline(cin,s);
			A.push_back(s);
		}
		
		m = 1;
		for(y = 0;y < h;y++)
		{
			for(x = 0;x < w;x++)
			{
				if(A[y][x] == '#') convertor(y,x);
				if(m == 0) break;
			}
			if(m == 0) break;
		}
		cout << "Case #" << ccase << ":" << endl;
		if(m == 0) cout << "Impossible" << endl;
		else
		{
			for(x = 0;x < h;x++)
			{
				cout << A[x] << endl;
			}
		}
	}

    while(getchar()!=EOF);
    return 0;
}
