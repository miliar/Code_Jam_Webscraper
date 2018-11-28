#include <iostream>
#include <string>
using namespace std;
char table[500] = {0};
void init()
{
	char st1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char gotit[] = "our language is impossible to understand";

	int sz = strlen(st1);
	for (int i = 0; i < sz; i++)
		table[st1[i]] = gotit[i];

	char st2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char gotit2[] = "there are twenty six factorial possibilities";

	sz = strlen(st2);
	for (int i = 0; i < sz; i++)
		table[st2[i]] = gotit2[i];

	char st3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char gotit3[] = "so it is okay if you want to just give up";

	sz = strlen(st3);
	for (int i = 0; i < sz; i++)
		table[st3[i]] = gotit3[i];

}
int main()
{
	init();
	table['q'] = 'z';
	table['z'] = 'q';
	freopen ("A-small-attempt1.in","r",stdin);
	freopen ("A-small-attempt1.out","w",stdout);
	int n;
	cin >> n;
	string a;
	getchar();
	for (int i = 0; i < n; i++)
	{
		getline(cin,a);
		printf ("Case #%d: ",i + 1);
		for (int i = 0; i < a.size(); i++)
		{
			printf ("%c",table[a[i]]);
		}
		printf ("\n");
	}
	return 0;
}