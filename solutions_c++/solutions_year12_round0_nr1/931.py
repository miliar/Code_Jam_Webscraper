#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main()
{
	char trans[] = "yhesocvxduiglbkrztnwjpfmaq";

	int T, caseNum;
	scanf("%d",&T);

	char str[256];
	gets(str);

	for(caseNum = 1; caseNum <= T; ++caseNum)
	{
		gets(str);
		printf("Case #%d: ", caseNum);
		for(int i=0; str[i]; ++i)
		{
			if(isalpha(str[i]))
				putchar(trans[str[i]-'a']);
			else
				putchar(str[i]);
		}
		putchar('\n');
	}
	return 0;
}

/*
�u�A���t�@�x�b�g���قȂ�A���t�@�x�b�g�ɒu������v�Í��������Ă���̂ŕ������Ă�
�T���v�����邾���ł����@�����ł���

�T���v���y�і�蕶���ɏo�Ă��Ȃ��̂�'q'�����ŁA���̕����͑S�ďo�Ă���̂�q��z�ɂȂ�̂��m�肵�܂�

*/
