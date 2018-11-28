#include <iostream>
#include <string>
using namespace std;

const int sen[19] = {22,4,11,2,14,12,4,26,19,14,26,2,14,3,4,26,9,0,12};
int n,level;
int pos[27][501],e[501];
string str;
char ch,ch0;
int tot;

void shorty(string & str)
{
	int temp1 = 0, temp2 = -1;
	string st = "";
	while (temp1 < str.length())
	{
		if (temp1 == 0 || str[temp1] != str[temp1-1])
		{	
			st += str[temp1];
			e[++temp2] = 1;
		}
		else
		{
			++e[temp2];
		}
		++temp1;
	}
	str = st;
}

void calcu(string str)
{
	for (int i = 0; i < 27; ++i)
		pos[i][0] = 0;
	for (int i = 0; i < 26; ++i)
	{
		char ch = 'a' + i;
		for (int j = 0; j < str.length(); ++j)
		{
//			cout << str[j];
			if (str[j] == ch)
			{
				++pos[i][0];
				pos[i][pos[i][0]] = j;
			}
		}
	}
	for (int j = 0; j < str.length(); ++ j)
	{
		char ch = ' ';
		if (str[j] == ch)
		{
			++ pos[26][0];
			pos[26][pos[26][0]] = j;	
		}
	}
}

void eval(int posi, int level, int & tot, int expo)
{
	if (level == 19)
	{
		tot = (tot + expo) % 10000;
	}
	else
	{
		int left = 18 - level;
		for (int i = 1; i <= pos[sen[left]][0]; ++i)
		{
//			cout << str[pos[sen[left]][i]];
			if (pos[sen[left]][i] >= posi)
				break;
			if (pos[sen[left]][i] + level >= 18)
			{
				eval(pos[sen[left]][i],level+1, tot, expo * e[pos[sen[left]][i]] % 10000);
			}
		}
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	cin >> n;
//	cin >> ch;
	getline(cin,str);
	for (int i = 0; i < n; ++i)
	{
		tot = 0;
		getline(cin,str);
		shorty(str);
		calcu(str);
		for (int j = 1; j <= pos[12][0]; ++j)
			eval(pos[12][j],1,tot,e[pos[12][j]]);
		printf("Case #%.d: ",i+1);
		if (tot >= 10000)
			printf("%.d",tot % 10000);
		else if (tot >= 1000)
			printf("%.d",tot);
		else if (tot >= 100)
			printf("0%.d",tot);
		else if (tot >= 10)
			printf("00%.d",tot);
		else if (tot > 0)
			printf("000%.d",tot);
		else printf("0000");
		printf("\n");
	}
	
//	cin >> n;
	return 0;
}
