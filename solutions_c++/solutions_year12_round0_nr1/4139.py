#include<iostream>
#include<string>
using namespace std;

char wrong_map[30] = "ynficwlbkuomxsevzpdrjgthaq";
char map[30] = "yhesocvxduiglbkrztnwjpfmaq";
char str[110];
/*int map[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 
			 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
			 '', '', '', '', '', '', '', 
			 '', '', '', '', ''};*/

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	
	int i, j, k;
	int T;
	int ncase = 1;
	cin >> T;
	getchar();
	for(i=0; i<T; i++)
	{
		printf("Case #%d: ", ncase++);
		memset(str, 0, sizeof(str));
		gets(str);
		int len = strlen(str);
		for(j=0; j<len; j++)
		{
			if(str[j] >= 'a' && str[j] <= 'z')
			{
				printf("%c", map[str[j]-'a']);
			}
			else
				printf(" ");
		}
		printf("\n");
	}
	
	//system("pause");
	return 0;
}
