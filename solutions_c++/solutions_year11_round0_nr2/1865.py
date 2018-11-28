#include <iostream>
#include <string>
#include <map>

using namespace std;

struct info
{
	char a;
	char b;
	char c;
	info(){}
	info(char a, char b, char c)
	{
		this->a = a;
		this->b = b;
		this->c = c;
	}
};

struct info1
{
	char a, b;
	info1() {};
	info1(char a, char b)
	{
		this->a = a;
		this->b = b;
	}
};

const int N = 100;

info comb[N];
info1 oppose[N];

string s, ans;
int cnt;
int c, d, n;

int find1(char s1, char s2)
{
	for (int i = 0; i < c; i++)
		if (comb[i].a == s1 && comb[i].b == s2 || comb[i].a == s2 && comb[i].b == s1)
			return comb[i].c;
	return 0;
}

bool find2()
{
	for (int i = 0; i < cnt - 1; i++)
	{
		for (int j = 0; j < d; j++)
			if (oppose[j].a == ans[cnt-1] && oppose[j].b == ans[i] || oppose[j].b == ans[cnt-1] && oppose[j].a == ans[i] )
				return true;
	}
	return false;
}

void check()
{
	if (cnt == 0 || cnt == 1)
		return;

	char res = find1(ans[cnt-2], ans[cnt-1]);
	if (res)
	{		
		ans[cnt-2] = res;
		cnt -= 2;
		cnt++;
		return;
    }

	if (find2())
	{
		cnt = 0;
	}		
}


int main()
{
	int cases;
	int num = 0;

	freopen("C:\\Users\\Haojian\\Desktop\\B-small-attempt4.in", "r", stdin);
	freopen("C:\\Users\\Haojian\\Desktop\\output.txt", "w", stdout);
	//freopen("C:\\Users\\Haojian\\Desktop\\test.txt", "r", stdin);
	cin >> cases;

	while (cases--)
	{
		cin >> c;
		info tmp;
		for (int i = 0; i < c; i++)
		{
			cin >> s;
			comb[i].a = s[0];
			comb[i].b = s[1];
			comb[i].c = s[2];
		}

		cin >> d;
		
		for (int i = 0; i < d; i++)
		{
			cin >> s;
			oppose[i].a = s[0];
			oppose[i].b = s[1];
		}

	/*
			sort(comb, comb+c. cmp1);
				sort(oppose, oppose+d, cmp2);*/
		

		cin >> n;
		cin >> s;
		ans = s;

		cnt = 1;

		for (int i = 1; i < s.size(); i++)
		{
			ans[cnt] = s[i];
			cnt++;
			check();
		}

		num++;
		printf("Case #%d: [", num);
		for (int i = 0; i < cnt-1; i++)
		{
			cout << ans[i] << ", ";
		}
		if (cnt > 0)
		   cout << ans[cnt-1];

		cout << "]" << endl;
	}
	return 0;
}