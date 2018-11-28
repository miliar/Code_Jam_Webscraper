#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>
#include <set>
using namespace std;


struct Node
{
	string s;
	long double w;
	int l;
	int r;
	Node()
	{
		l = r = -1;
		s = "";
	}
};

vector <Node> arr;
		set <string> pr;


void ReadNode(int n)
{
	char c=' ';
	while (c != '(')
		scanf("%c", &c);
	scanf("%Lf", &arr[n].w);
	c = ' ';
	while (c == ' ' || c == '\n')
		scanf("%c", &c);
	if (c == ')')
		return;
	while (isalpha(c))
	{
		arr[n].s += c;
		scanf("%c", &c);
	}
	if (c == '(')
		ungetc(c,stdin);
	arr.push_back(Node());
	arr[n].l = arr.size()-1;
	arr.push_back(Node());
	arr[n].r = arr.size()-1;
	ReadNode(arr[n].l);
	ReadNode(arr[n].r);
	c = ' ';
	while (c != ')')
		scanf("%c", &c);
}

long double Calc(int n, long double p)
{
	if (n == -1)
		return p;
	p *= arr[n].w;
	if (pr.find(arr[n].s) != pr.end())
		return Calc(arr[n].l, p);
	else
		return  Calc(arr[n].r, p);
}

int main()
{
	freopen("test3.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int t;
	int len,num;
	string name;
	int n;
	cin >> t;
	for (int k = 1; k <= t; k ++)
	{
		cout << "Case #" << k << ":" << endl; 
		arr.clear();
		arr.push_back(Node());
		cin >> len;
		ReadNode(0);
		cin >> num;

		for (int i = 0; i < num; i ++)
		{
			cin >> name >> n;
			pr.clear();

			for (int j = 0;j < n;j ++)
			{
				string s;
				cin >> s;
				pr.insert(s);

			}
			printf("%.7Lf\n", Calc(0,1));
		}

	}
	return 0;
}