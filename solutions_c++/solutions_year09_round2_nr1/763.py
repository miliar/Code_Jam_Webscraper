#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <sstream>

using namespace std;

struct t
{
	double w;
	string f;
	t *n1;
	t *n2;
};

void build(t *n, istringstream &sb);
double search(t *n, map<string,bool> &mA, double w);
void del(t *n);

void main()
{
	int N,L,A,n,a,b,c;
	t T;
	string tmp;
	char line[513];

	cout << fixed;
	cin >> N;
	for (a = 1; a <= N; a++)
	{
		cin >> L;
		cin.getline(line, 512);
		tmp = "";
		for (b = 0; b < L; b++)
		{
			cin.getline(line, 512);
			tmp += line;
			tmp += " ";
		}
		istringstream sb;
		tmp = tmp.substr(tmp.find("(") + 1);
		sb.str(tmp);
		build(&T, sb);
		cin >> A;
		cout << "Case #" << a << ":" << endl;
		for (b = 0; b < A; b++)
		{
			map<string,bool> mA;
			mA.clear();
			cin >> tmp >> n;
			for (c = 0; c < n; c++)
			{
				cin >> tmp;
				mA[tmp] = true;
			}
			cout << setprecision(7) << search(&T, mA, 1) << endl;
		}
		del(&T);
	}
}

void build(t *n, istringstream &sb)
{
	char ch;

	n->n1 = NULL;
	n->n2 = NULL;
	sb >> n->w;
	sb >> ch;
	while (ch != ')')
	{
		if (ch != ' ' && ch != '\n')
		{
			n->f = ch;
			sb >> ch;
			while (ch != ' ' && ch != '\n' && ch != '(')
			{
				n->f += ch;
				sb >> ch;
			}
			while (ch != '(')
			{
				sb >> ch;
			}
			n->n1 = new t;
			n->n2 = new t;
			build(n->n1, sb);
			sb >> ch;
			while (ch != '(')
			{
				sb >> ch;
			}
			build(n->n2, sb);
		}
		sb >> ch;
	}
}

double search(t *n, map<string,bool> &mA, double w)
{
	if (n != NULL)
	{
		w *= n->w;
		if (mA.find(n->f) == mA.end())
		{
			return search(n->n2, mA, w);
		}
		else
		{
			return search(n->n1, mA, w);
		}
	}
	return w;
}

void del(t *n)
{
	if (n != NULL)
	{
		if (n->n1 != NULL)
		{
			del(n->n1);
			delete n->n1;
			n->n2 = NULL;
		}
		if (n->n2 != NULL)
		{
			del(n->n2);
			delete n->n2;
			n->n2 = NULL;
		}
	}
}
