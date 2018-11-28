#include <iostream>
#include <string>
#include <memory.h>
using namespace std;

int N;
string s;
int mat[501][19];
string wel = "welcome to code jam";

int dyn(int x, int y)
{
	if(mat[x][y] != -1)
		return mat[x][y];
	if(y == 19) return 1;
	if(x == s.length()) return 0;
	mat[x][y] = 0;
	for(int i = x; i < s.length(); i++)
		if(s[i] == wel[y])
			mat[x][y] += dyn(i + 1, y + 1);
	return mat[x][y];
}

int main()
{
	cin>>N;
	getline(cin,s);
	for(int c = 1; c <= N; c++)
	{
		getline(cin,s);
		memset(mat, -1, sizeof mat);
		cout<<"Case #"<<c<<": ";
		int x = dyn(0,0);
		int xx = x;
		int n = 0;
		do
		{
			x /= 10;
			n++;
		}while(x);
		for(int i = 0; i < 4 - n; i++)
			cout<<0;
		cout<<xx<<endl;
	}

	return 0;
}
