#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T,N;
	char c;
	char line[200];

	char M[27] = "yhesocvxduiglbkrztnwjpfmaq";

	//freopen("D:\\VC2005\\GoogleCodeJam\\2012\\Q1\\in.txt","r",stdin);
	//freopen("D:\\VC2005\\GoogleCodeJam\\2012\\Q1\\small.txt","w",stdout);


	scanf("%d\n", &T);

	for(int i=1;i<=T;++i)
	{
		gets(line);
		printf("Case #%d: ", i); 
		for(int j=0, len=strlen(line); j < len; ++j) {
			c = line[j];
			if ('a' <= c && c <= 'z')
				printf("%c", M[c-'a']);
			else
				printf("%c", c);
		}
		printf("\n");
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
