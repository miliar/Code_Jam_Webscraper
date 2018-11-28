#include <iostream>
#include <vector>
using namespace std;

int m[30];
string gs = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string vld = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

string trans(char str[], int len)
{
	string ret = "";
	for (int i=0; i<len; i++)
	{
		if(str[i]==' ') ret+=' ';
		else ret += char(m[str[i]-'a']);
	}
	return ret;
}

int main()
{
	freopen("A-small-attempt5.in", "r", stdin);
	freopen("A-small-attempt5.out", "w", stdout);
	int i, j, icase, nCase;
	char str[105];

	int len = gs.length();
	int flag[1000];
	memset(m, -1, sizeof(m));
	memset(flag, -1, sizeof(flag));

	m['y'-'a'] = 'a';
	m['e'-'a'] = 'o';
	m['q'-'a'] = 'z';
	flag['a'] = flag['o'] = flag['e'] = 1;
	for (i=0; i<len; i++)
	{
		if(gs[i]==' ') continue;
		else
		{
			m[gs[i]-'a'] = vld[i];
			flag[vld[i]] = 1;
		}
	}

	for (i=0; i<26; i++)
	{
		if(m[i]==-1)
		{
			for (j=0; j<26; j++)
			{
				if(flag['a'+j]==-1)
				{
					m[i] = 'a'+j;
					break;
				}
			}
			break;
		}
	}

// 	for (i=0; i<26; i++)
// 	{
// 		cout<<char(m[i]);
// 	}
// 	cout<<endl;
	scanf("%d", &nCase);
	gets(str);
//	cin>>nCase;
	for (icase=1; icase<=nCase; icase++)
	{
		memset(str, '\0', sizeof(str));
		gets(str);
		printf("Case #%d: %s\n", icase, trans(str, strlen(str)).c_str());
	}

	return 0;
}
