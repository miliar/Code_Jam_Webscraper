#include <iostream>
#include <string>

using namespace std;

struct t
{
	t *n[256];
};

unsigned int search(t *n, string &w, int pos);

void main()
{
	string word;
	int L,D,N,a,b;
	t T, *n;
	unsigned char ch;
	memset(&T, 0, sizeof(t));

	cin >> L >> D >> N;
	for (a = 1; a <= D; a++)
	{
		n = &T;
		cin >> word;
		for (b = 0; b < L; b++)
		{
			ch = (unsigned char)word[b];
			if (n->n[ch] == NULL)
			{
				n->n[ch] = new t;
				memset(n->n[ch], 0, sizeof(t));
			}
			n = n->n[ch];
		}
	}
	for (a = 1; a <= N; a++)
	{
		cin >> word;
		cout << "Case #" << a << ": " << search(&T, word, 0) << endl;
	}
}

unsigned int search(t *n, string &w, int pos)
{
	unsigned int ret = 0;

	if (n != NULL)
	{
		if (w[pos] == '(')
		{
			string b;
			pos++;
			while (w[pos] != ')')
			{
				b += w[pos];
				pos++;
			}
			for (int a = 0; a < b.length(); a++)
			{
				ret += search(n->n[b[a]], w, pos+1);
			}
		}
		else if (w[pos] == 0)
		{
			ret = 1;
		}
		else
		{
			ret = search(n->n[w[pos]], w, pos+1);
		}
	}
	return ret;
}
