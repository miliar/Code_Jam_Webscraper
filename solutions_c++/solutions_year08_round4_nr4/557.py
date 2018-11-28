#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define SZ(a) (int)(a).size()
#define For(i, a, b) for(int i=(a); i<(b); ++i)

typedef long long ll;

int k, res;
string s;
int a[10];
bool fl[10];

string Convert()
{
	string res=s;
	For(i, 0, SZ(s)/k)
		For(j, 1, k+1)
			res[i*k+j-1]=s[i*k+a[j]-1];
	return res;
}

int Calc(string _s)
{
	int res=0;
	while (SZ(_s)>0)
	{
		++res; while (SZ(_s)>1 && _s[0]==_s[1]) _s=_s.substr(1);
		_s.erase(_s.begin());
	}
	return res;
}

void Rec(int nom)
{
	if (nom>k)
	{
		res=min(res, Calc(Convert()));
		return;
	}
	For(i, 1, k+1)
		if (!fl[i])
		{
			fl[i]=true;
			a[nom]=i;
			Rec(nom+1);
			fl[i]=false;
		}
}

void main()
{
	int tc;
	cin >> tc;
	For(_case, 1, tc+1)
	{
		cin >> k >> s;
		memset(fl, false, sizeof(fl));
		res=100000;
		Rec(1);
		cout << "Case #" << _case << ": " << res << endl;
	}
}