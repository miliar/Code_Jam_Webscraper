#include <iostream>
#include <string>

using namespace std;

int arr[100000], r, i;
string masiv[30];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	masiv[' ']=" ";
	masiv['e']="o";
    masiv['j']="u";
	masiv['p']="r";
	masiv['m']="l";
	masiv['y']="a";
	masiv['s']="n";
	masiv['l']="g";
	masiv['c']="e";
	masiv['k']="i";
	masiv['d']="s";
	masiv['x']="m";
	masiv['v']="p";
	masiv['n']="b";
	masiv['r']="t";
	masiv['i']="d";
	masiv['b']="h";
	masiv['t']="w";
	masiv['a']="y";
	masiv['h']="x";
	masiv['w']="f";
	masiv['f']="c";
	masiv['o']="k";
	masiv['u']="j";
	masiv['g']="v";
	masiv['z']="q";
	masiv['q']="z";
	int n, j;
	cin>>n;

	for (i=0; i<=n; i++)
	{
		getline(cin, masiv[i]);
	}
	for (i=1; i<=n; i++)
	{
		cout<<"Case #"<<i<<": ";
		for (j=0; j<masiv[i].length(); j++)
		{
			cout<<masiv[masiv[i][j]];
		}
		cout<<endl;
	}
}