#include<stdio.h>
#include<string.h>
int main()
{
	char googlemapping[127];
	char inputsentence[105],enter;
	int T,sentence,count=0;

	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout); //프로젝트 어딧어 뭐가문제야? 병태형이 내줬는대 안대서..

	scanf_s("%d\n",&T);

	googlemapping[97] = 'y'; googlemapping[98] = 'h'; googlemapping[99] = 'e';
	googlemapping[100] = 's';googlemapping[101] = 'o';googlemapping[102] = 'c';
	googlemapping[103] = 'v';googlemapping[104] = 'x';googlemapping[105] = 'd';
	googlemapping[106] = 'u';googlemapping[107] = 'i';googlemapping[108] = 'g';
	googlemapping[109] = 'l';googlemapping[110] = 'b';googlemapping[111] = 'k';
	googlemapping[112] = 'r';googlemapping[113] = 'z';googlemapping[114] = 't';
	googlemapping[115] = 'n';googlemapping[116] = 'w';googlemapping[117] = 'j';
	googlemapping[118] = 'p';googlemapping[119] = 'f';googlemapping[120] = 'm';
	googlemapping[121] = 'a';googlemapping[122] = 'q';

	while(T--)
	{
		gets(inputsentence);
		sentence = strlen(inputsentence);
		printf("Case #%d: ",++count);
		for(int i=0;i<sentence;i++)
		{
			if(inputsentence[i] == ' ')
				printf(" " );
			else
				printf("%c",googlemapping[inputsentence[i]]);
		}
		printf("\n");
	}
	return 0;
}