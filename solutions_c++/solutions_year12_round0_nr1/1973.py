#include <stdio.h>

char sprav[]  = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
//	freopen("A.in", "rt", stdin);

	char s[256];
	char in[40000];
	
	for(int i=0; i<256; ++i)
		s[i] = ' ';

	int N;

	for(unsigned char i='a'; i<='z'; ++i)
		s[i] = sprav[i-'a'];

	scanf("%d", &N);
	gets(in);

	for(int i=0; i<N; ++i)
	{
		gets(in);

		int j = 0;
		while(in[j])
		{
			in[j] = s[(unsigned char)in[j]];
			++j;
		}

		printf("Case #%d: %s\n", i+1, in);
	}

	return 0;
}