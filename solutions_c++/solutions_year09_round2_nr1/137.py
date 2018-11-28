#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

#define cin fin
#define cout fout

char inputs[50000];
char name[1000];

char feature[200][20];
int k;

struct Tnode {
	double weight;
	char fea[20];
	int left, right;
};

Tnode dtree[50000];
int total;

void build(int head, int tail, int now)
{
	dtree[now].weight = 0;
	dtree[now].left = dtree[now].right = -1;

	if (head > tail) return;

	long double ten = 10;
	int newleft, newright;

	for (int i = head; i <= tail; i++)
		if (inputs[i] == '(') {newleft = i+1; break;}
	for (int j = tail; j >= newleft; j--)
		if (inputs[j] == ')') {newright = j-1; break;}

	
	int i = newleft;
	bool points = false;
	long double w = 0.0;

	while (i <= newright)
	{
		if (inputs[i] == '.') points = true;
		if (inputs[i] >= '0' && inputs[i] <= '9' && points == false)
		{
			w = inputs[i] - '0';
		}

		if (inputs[i] >= '0' && inputs[i] <= '9' && points == true)
		{
			w += (inputs[i] - '0') / ten;
			ten *= 10.0;
		}
		
		if (inputs[i] >= 'a' && inputs[i] <= 'z') 
			break;

		i++;
	}	

	dtree[now].weight = w;	

	if (i > newright) return;

	memset(dtree[now].fea, 0, sizeof(dtree[now].fea));

	int len = 0;
	while (i <= newright && inputs[i] >= 'a' && inputs[i] <= 'z')
	{
		dtree[now].fea[len] = inputs[i];
		len++;
		i++;
	}

	bool flag = false;
	int t = 0;
	int left1 = i;
	int right1;
	
	for (int j = left1; j <= newright; j++)
	{
		if (inputs[j] == '(') flag = true;
		if (inputs[j] == '(') t++;
		if (inputs[j] == ')') t--;
		if (t == 0 && flag == true) 
		{
			right1 = j;
			break;
		}
	}

	total++;
	dtree[now].left = total;
	build(left1, right1, total);

	total++;
	dtree[now].right = total;
	build(right1+1, newright, total);
}

long double process(int now, long double ans)
{
	ans = ans * dtree[now].weight;
	if (dtree[now].left == -1 && dtree[now].right == -1)
		return ans;

	bool flag = false;
	for (int i = 0; i < k; i++)
		if (strcmp(feature[i], dtree[now].fea) == 0)
		{
			flag = true;
			break;
		}

	if (flag)
		return process(dtree[now].left, ans);
	else
		return process(dtree[now].right, ans);
}

int main()
{
	int n;

	cout.precision(7);
	cout.flags(ios::fixed);

	cin >> n;
	for (int cases = 1; cases <= n; cases++)
	{
		char s[1000];
		int l;

		cin >> l;
		cin.getline(s, 1000);
		memset(inputs, 0, sizeof(inputs));

		for (int i = 0; i < l; i++)
		{
			cin.getline(s, 1000);
			strcat(inputs, s);
		}

		total = 0;

		build(0, strlen(inputs)-1, 0);

		int m;
		cin >> m;
		cout << "Case #" << cases << ":" << endl;

		for (int i = 0; i < m; i++)
		{
			cin >> name >> k;
			for (int j = 0; j < k; j++)
				cin >> feature[j];

			cout << process(0, 1.0) << endl;
		}
	}
	return 0;
}