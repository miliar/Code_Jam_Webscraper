/*
ID: rohamhe1
PROB: proximity
LANG: C++
*/
#include<iostream>
#include<cstring>
#include<iomanip>	
#include<vector>
#include<map>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<set>
#include<complex>
#include<queue>
#include<utility>

using namespace std;

//typedef complex<long double> point;
#define pb push_back
#define mk make_pair
#define x first
#define y second
#define error(x) cout << #x << " : " << (x) << endl;
typedef long long LL;
typedef long double LD;
//#define cin fin
//#define cout fout

LL n , m , k;
const int maxn = 30;
char array[maxn][maxn];
int main()
{
	int t;
	cin >> t;
	int T = 1;
	while(t--)
	{
		int D = 0;
		for(int i=0 ; i<4 ; i++)
			for(int j=0 ; j < 4 ; j++)
			{
				cin >> array[i][j];
				if(array[i][j] == '.') D++;
			}
		int O , X , dot;
		int ans = 0;
		for(int i=0 ; i<4 ; i++)
		{
			O=0;X=0;dot=0;
			for(int j=0 ; j<4 ; j++)
			{
				if(array[i][j] == 'O')
					O++;
				else if(array[i][j] == 'X')
					X++;
				else if(array[i][j] == '.')
					dot++;
			}
			if(dot == 0)
			{
				if(X==0 || O==0)
				{
					if(X > 0)
						ans = 1;
					else
						ans = 2;
				}
			}
		}
		for(int i=0 ; i<4 ; i++)
		{
			O=0;X=0;dot=0;
			for(int j=0 ; j<4 ; j++)
			{
				if(array[j][i] == 'O')
					O++;
				else if(array[j][i] == 'X')
					X++;
				else if(array[j][i] == '.')
					dot++;
			}
			if(dot == 0)
			{
				if(X==0 || O==0)
				{
					if(X > 0)
						ans = 1;
					else
						ans = 2;
				}
			}
		}
		O=0;X=0;dot=0;
		for(int j=0 ; j<4 ; j++)
		{
			if(array[j][j] == 'O')
				O++;
			else if(array[j][j] == 'X')
				X++;
			else if(array[j][j] == '.')
				dot++;
		}
		if(dot == 0)
		{
			if(X==0 || O==0)
			{
				if(X > 0)
					ans = 1;
				else
					ans = 2;
			}
		}
		O=0;X=0;dot=0;
		for(int j=0 ; j<4 ; j++)
		{
			if(array[j][3-j] == 'O')
				O++;
			else if(array[j][3-j] == 'X')
				X++;
			else if(array[j][3-j] == '.')
				dot++;
		}
		if(dot == 0)
		{
			if(X==0 || O==0)
			{
				if(X > 0)
					ans = 1;
				else
					ans = 2;
			}
		}
		if(ans == 0 && D > 0)
			ans = 3;
		if(ans == 1)
			cout << "Case #" << T << ": X won" << endl;
		else if(ans == 2)
			cout << "Case #" << T << ": O won" << endl;
		else if(ans == 3)
			cout << "Case #" << T << ": Game has not completed" << endl;
		else
			cout << "Case #" << T << ": Draw" << endl;
		T++;
	}
}
