#include <iostream>
#include <string>

using namespace std;

void oneCase();

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ": ";
		oneCase();
		cout << endl;
	}

	return 0;
}

struct pairType
{
	bool combine;
	bool opposed;
	char nonBase;
};

void oneCase()
{
	pairType pairs[26][26];

	for (int i = 0; i < 26; i++)
	{
		for (int j = 0; j < 26; j++)
		{
			pairs[i][j].combine = false;
			pairs[i][j].opposed = false;
		}
	}

	int C;
	cin >> C;
	char a, b, c;
	for (int i = 0; i < C; i++)
	{
		cin >> a >> b >> c;
		pairType* p = &pairs[a-'A'][b-'A'];
		p->combine = true;
		p->nonBase = c;
		p = &pairs[b-'A'][a-'A'];
		p->combine = true;
		p->nonBase = c;
		p = nullptr;
	}

	int D;
	cin >> D;
	for (int i = 0; i < D; i++)
	{
		cin >> a >> b;
		pairType* p = &pairs[a-'A'][b-'A'];
		p->opposed = true;
		p = &pairs[b-'A'][a-'A'];
		p->opposed = true;
		p = nullptr;
	}

	int N;
	cin >> N;
	string inv;
	for (int i = 0; i < N; i++)
	{
		cin >> a;
		inv += a;

		bool done = false;
		while (!done)
		{
			int len = inv.length();
			if (len < 2)
			{
				done = true;
			}
			else
			{
				pairType* p = &pairs[inv[len-1]-'A'][inv[len-2]-'A'];
				if (p->combine)
				{
					inv = inv.substr(0,len-2) + p->nonBase;
				}
				else
				{
					done = true;
					for (int j = len-2; j >= 0; j--)
					{
						if (pairs[inv[len-1]-'A'][inv[j]-'A'].opposed)
						{
							inv = "";
							break;
						}
					}
				}
				p = nullptr;
			}
		}
	}

	cout << "[";
	int len = inv.length();
	for (int i = 0; i < len; i++)
	{
		if (i > 0) cout << ", ";
		cout << inv[i];
	}
	cout << "]";
}