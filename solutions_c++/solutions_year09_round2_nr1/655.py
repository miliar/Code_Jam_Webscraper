#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;

string total;
string trait[110];
int num;

bool istrait(string s)
{
	for (int x=0; x<num; x++)
		if (trait[x] == s)
			return true;

	return false;
}

void parse()
{
	string temp = "";
	for (int x=0; x<total.size(); x++)
	{
		if (total[x] >= 'a' && total[x] <= 'z')
			temp += total[x];

		if (total[x] >= '0' && total[x] <= '9' || total[x] == '.')
			temp += total[x];

		if (total[x] == '(')
			temp += "( ";

		if (total[x] == ')')
		{
			if (temp[temp.size()-1] == ' ')
				temp += ")";
			else
				temp += " )";
		}

		if (total[x] == ' ')
			if (temp[temp.size()-1] != ' ')
				temp += ' ';
	}

	total = temp;
}

double solve(string tree)
{
	int x;

	int val = 0;
	int pos = tree.find('.');
	int div = 1;
	for (x=pos+1; tree[x] != ' '; x++)
	{
		val = val*10 + tree[x]-'0';
		div *= 10;
	}

	double ret;
	if (tree[2] == '1')
		ret = 1;
	else
		ret = val / double(div);

	x++;
	if (tree[x] == ')')
		return ret;

	string name = "";
	while (tree[x] != ' ')
		name += tree[x++];

	if (istrait(name))
	{
		int brck[2] = {1, 0};
		int y = x+2;
		while (brck[0] != brck[1])
		{
			if (tree[y] == '(')
				brck[0]++;
			if (tree[y] == ')')
				brck[1]++;
			y++;
		}

		return ret * solve(tree.substr(x+1, y-x-1));
	}
	else
	{
		int brck[2] = {0, 1};
		int y = tree.size()-4;
		while (brck[0] != brck[1])
		{
			if (tree[y] == '(')
				brck[0]++;
			if (tree[y] == ')')
				brck[1]++;
			y--;
		}

		return ret * solve(tree.substr(y+1, tree.size()-2-y-1));
	}
}

void work()
{
	double ans = solve(total);
	printf("%0.7f\n", ans);
}

int main()
{
	freopen("lol2.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int N;
	int L, A;
	cin >> N;
	for (int x=0; x<N; x++)
	{
		total = "";
		scanf("%d\n", &L);
		for (int a=0; a<L; a++)
		{
			string s;
			getline(cin, s);
			total += s;
		}

		parse();

		printf("Case #%d:\n", x+1);
		scanf("%d\n", &A);
		for (int a=0; a<A; a++)
		{
			string name; cin >> name;
			cin >> num;
			for (int b=0; b<num; b++)
				cin >> trait[b];

			work();
		}
	}
}
