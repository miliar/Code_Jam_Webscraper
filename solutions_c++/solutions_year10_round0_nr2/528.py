#include <iostream>
#include <cstring>
#include <string>
#include <fstream>
using namespace std;

const int maxl = 60;

class verylongint
{
public:
	int shu[maxl + 1];
	verylongint()
	{
		memset(shu, 0, sizeof(shu));
	}
	verylongint(string s)
	{
		int l = s.size();
		memset(shu, 0, sizeof(shu));
		for (int i = 0; i < l; i++)
		{
			shu[maxl - (l - 1 - i)] = s[i] - '0';
		}
	}
	verylongint(verylongint &other)
	{
		int i;
		for (i = 1; i <= maxl; i++) shu[i] = other.shu[i];
	}
	void operator = (verylongint other)
	{
		int i;
		for (i = 1; i <= maxl; i++) shu[i] = other.shu[i];
	}
	bool operator == (verylongint other)
	{
		int i;
		for (i = 1; i <= maxl; i++) if (shu[i]!=other.shu[i]) return false;
		return true;
	}
	bool operator > (verylongint other)
	{
		int i;
		for (i = 1; i <= maxl; i++) if (shu[i] > other.shu[i]) return true;
		else if (shu[i] < other.shu[i]) return false;
		return false;
	}
	verylongint operator - (verylongint other)
	{
		verylongint res;
		int g = 0;
		for (int i = maxl; i >= 1; i--)
		{
			res.shu[i] = shu[i] - other.shu[i] - g;
			if (res.shu[i] < 0)
			{
				res.shu[i] += 10; g = 1;
			} else g = 0;
		}
		return res;
	}
	verylongint operator % (verylongint other)
	{
		verylongint res;
		int i, j;
		for (i = 1; i <= maxl; i++)
		{
			for (j = 2; j <= maxl; j++) res.shu[j - 1] = res.shu[j];
			res.shu[maxl] = shu[i];
			while (res > other || res == other)
			{
				res = res - other;
			}
		}
		return res;
	}
	friend ostream &operator << (ostream &output, verylongint other)
	{
		int i = 1;
		while (i < maxl && other.shu[i] == 0) i++;
		for (; i <= maxl; i++) output << other.shu[i];
		return output;
	}
};

int n;
verylongint num[1001];

verylongint gcd(verylongint x, verylongint y)
{
	if (y == verylongint("0")) return x; else return gcd(y, x % y);
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("Blarge.in");
	output.open("Blarge.out");
	int t, i, j, ca = 0;
	string s;
	verylongint max;
	input >> t;
	while (t > 0)
	{
		input >> n;
		for (i = 1; i <= n; i++)
		{
			input >> s;
			num[i] = verylongint(s);
		}

		for (i = 1; i < n; i++)
		{
			for (j = i + 1; j <= n; j++) if (num[j] > num[i])
			{
				verylongint temp = num[j]; num[j] = num[i]; num[i] = temp;
			}
		}
		max = num[1] - num[2];
		for (i = 3; i <= n; i++) max = gcd(max, num[i - 1] - num[i]);
		output << "Case #" << ++ca << ": ";
		if (max == verylongint("0") || num[1] % max == verylongint("0")) output << 0 << endl;
		else output << max - num[1] % max << endl;
		t--;
	}
	return 0;
}
