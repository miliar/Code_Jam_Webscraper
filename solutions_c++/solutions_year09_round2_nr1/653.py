#include <vector>
#include <queue>
#include <string>
#include <stdio.h>

using namespace std;

string s;
vector <string> fe;

struct node
{
	string cecha; // cecha
	double weight;
	node *left, *right;
};

node *root;

int read_feature(int pos, string &str)
{
	string r = "";
	while (s[pos]==' ') pos++;
	
	while (1)
	{
		if (s[pos]==' ') break;
		if (s[pos]=='(') break;

		r += s[pos];
		pos++;
	}
	str = r;
	return pos+1;
}

int read_number(int pos, double &num)
{
	double pot = 0.1;
	num = 0.0;
	while (s[pos]==' ') pos++;
	if (s[pos] == '1') num = 1.0;
	pos++;

	while (1)
	{
		if (s[pos]==' ') 
		{
			pos++;
			break;
		}
		if (s[pos]==')') break;
		if (s[pos]=='.') 
		{
			pos++;
			continue;
		}
		else 
		{
			num += (s[pos]-'0') * pot;
			pot *= 0.1;
		}
		pos++;
	}
	return pos;
}


void read_node(node *cn, int &pos)
{
	cn->weight = -1.0f;
	cn->cecha = "";
	cn->left = 0;
	cn->right = 0;

	string ss;
	double w;

	while (s[pos]==' ') pos++;
	if (s[pos]=='(')
	{
		//printf("\nnode... [%d]", pos);
		pos = read_number(pos+1, w);
		//printf("\n   w = %lf [%d]", w, pos);
		cn->weight = w;

		while (s[pos]==' ') pos++;
		if (s[pos]==')') // koniec, to byl wezel
		{
			pos++;
		}
		else 
		{
			//printf("\n zacz: %c", s[pos]);
			pos = read_feature(pos, ss);
			//printf("\n   f = '%s' [%d]", ss.c_str(), pos);
			cn->cecha = ss;

			cn->left = new node();
			cn->right = new node();

			read_node(cn->left, pos);
			read_node(cn->right, pos);

			while (s[pos]==' ') pos++;
			if (s[pos]==')') pos++;
		}
	}
	else pos++;
}

void go()
{
	int pos = 0;
	root = new node();
	read_node(root, pos);
}

string get_name()
{
	string str = "";
	char c;

	while (1)
	{
		if (scanf("%c", &c) == EOF) break;
		if (c == ' ') break;
		if (c == '\n') break;
		str = str + c;
	}
	return str;
}

void print(node *n, string sp)
{
	if (n != 0)
	{
		printf("\n%s%lf", sp.c_str(), n->weight);
		if (n->cecha != "")
		{
			printf("%s", n->cecha.c_str());
			print(n->left, sp+' ');
			print(n->right, sp+' ');
		}

	}
}

double check(node *n)
{
	double pr = n->weight;

	if (n->cecha != "")
	{
		bool ok = false;
		for (int i=0; i<fe.size(); i++) if (fe[i] == n->cecha) ok = true;
		if (ok) pr *= check(n->left);
		else pr *= check(n->right);
	}
	
	return pr;
}

int main()
{
	int i,l,k,j;
	int T, L;
	char c;
	int x, y;
	double ans;
	string cecha;


	scanf("%d", &T);
	for (k=0; k<T; k++)
	{
		scanf("%d", &L);
		scanf("%c", &c);
		s = "";
		while (L)
		{
			if (scanf("%c", &c) == EOF) break;
			if (c=='\n') L--;
			else s += c;
		}

		go();
		//print(root, "");

		printf("Case #%d:\n", k+1);

		scanf("%d", &L);
		scanf("%c", &c);

		//printf("\nilosc = %d", L);
		for (i=0; i<L; i++) // dla kazdego zwierzaka
		{
			fe.clear();
			get_name();
			scanf("%d", &j);
			scanf("%c", &c);
			for (l=0; l<j; l++) // dla kazdej cechy
			{
				cecha = get_name();
				fe.push_back(cecha);
				//printf("[%s]", cecha.c_str());
			}

			ans = check(root);
			printf("%lf\n", ans);

		}
	}
	return 0;
}
