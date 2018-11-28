#include <cstdio>

using namespace std;


int main()
{
	freopen("truc.in", "r", stdin);
	freopen("truc.out", "w", stdout);
	char txt1[128] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char txt2[128] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

    char conv[256];
	conv['a'] = 'y';
	conv['q'] = 'z';
	conv['z'] = 'q';



    for (int i = 0; i < 128; i++)
		conv[txt1[i]] = txt2[i];


	int nbCas;
	scanf("%d", &nbCas);
	getchar();

	int c =' ';
	for (int cur = 1; cur <= nbCas; cur++)
	{
		c = getchar();
		printf("Case #%d: ", cur);
		while (c != '\n')
		{
			putchar(conv[c]);
			c = getchar();
		}
		putchar('\n');
	}
    return 0;
}
