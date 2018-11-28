//najprostsza palowa...
#include <iostream>
#include<string>
using namespace std;

#define MR 5010
#define MS 20
int l, d, n;
string tab[MR], s;
bool spr[MR][MS];

void go(char z, int pos)
{
	for(int c = 0; c < d; c++)
		if(!pos)
		{
			if(tab[c][pos] == z)
				spr[c][pos] = 1;
		}
		else
		{
			if(spr[c][pos-1] && tab[c][pos] == z)
				spr[c][pos] = 1;
		}
}//

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> l >> d >> n;
	for(int c = 0; c < d; c++)
		cin >> tab[c];
	for(int c = 0; c < n; c++)
	{
		int pos = 0; bool nawias = false;
		cin >> s;
		for(int i = 0; i < s.length(); i++)
		{
			if(s[i] == '(')			
				nawias = true;			
			else if(s[i] == ')')
				nawias = false;
			else
				go(s[i], pos);
			if(!nawias)
				pos++;
		}
		int ile = 0;
		for(int i = 0; i < l; i++)
			for(int j = 0; j < d; j++)
			{
				if(i == l-1 && spr[j][i])
					ile++;
				spr[j][i] = 0;
			}
		cout << "Case #" << c+1 <<": " << ile << "\n";
	}
	return 0;
}