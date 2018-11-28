#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

class str
{
public:
	double weight;
	string feature;
	str* has;
	str* nothas;
};

char next()
{
	char c;
	do
	{
		scanf("%c", &c);
	}
	while (c == ' ' || c == 10 || c == 13);

	return c;
}


str* read()
{
	str *rc = new str();

	char c;

//	c = next(); // (
	double num = next() - '0';
	c = next();
	if (c == '.')
	{
		c = next();
		double pow = 1;
		while (c >= '0' && c <= '9')
		{
			pow *= 0.1;
			num += pow * (c - '0');
			c = next();
		}
	}
	// now c points to feature name or )
	if (c == ')')
	{
		rc->has = NULL;
		rc->nothas = NULL;
		rc->weight = num;
		rc->feature = "";
	}
	else
	{
		string feat = "";
		do
		{
			feat += c;
			c = next();
		}
		while (c != '(');

		rc->feature = feat;
		rc->weight = num;
		rc->has = read();
		next(); // (
		rc->nothas = read();
		next();
	}


	return rc;
}

string f[1000];

double process(str *tree, double p, int n)
{
	if (tree->has == NULL)
	{
		return p * tree->weight;
	}
	else
	{
		for (int i = 0; i < n; i++)
		{
			if (f[i] == tree->feature)
			{
				return process(tree->has, p * tree->weight, n);
			}
		}

		return process(tree->nothas, p * tree->weight, n);
	}
}


int main()
{
	freopen("C:\\a2.txt", "r" ,stdin);
	freopen("C:\\a2out.txt", "w" ,stdout);
	
	int tn;
	scanf("%d", &tn);
	for (int t = 1; t <= tn; t++)
	{
		int temp;
		scanf("%d", &temp);

		next();
		str *tree = read();

		int a;
		scanf("%d", &a);

		printf("Case #%d:\n", t);

		for (int i = 0; i < a; i++)
		{
			char name[100];
			char fiicha[100];
			int n;
			scanf("%s %d", &name, &n);
			for (int j = 0; j < n; j++)
			{
				scanf("%s", fiicha);
				f[j].assign(fiicha);
			}

			double pr = process(tree, 1.0, n);
			printf("%.10lf\n", pr);
		}




	}

	return 0;
}
