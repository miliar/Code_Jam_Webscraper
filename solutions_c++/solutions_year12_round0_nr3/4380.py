/*
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define MAXDIC 60

char dic[MAXDIC][20] = {
"the", "our", "is", "it", "so", "if", "you", "to", "are", "up",
"our", "language", "impossible", "understand", "there", "twenty", "factorial", "possibilities", "okay", " want",
"just", "give", "zoo", "google", "end", "test", "problem", "we", "have", "come",
"with", "best", "possible", "language", "at", "text", "message", "and", "each", "letter"
"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
};

char * downlang(char lang[50])
{
int i;

for(i = 0; i < 26; i++)
{
if(lang[i] >=65 && lang[i] <= 90)
lang[i] += 32;
}
return lang;
}

int main(void)
{
int i, j, t, count;
char *token, input[5000], lang[100][50], transTable[26];

scanf("%d ", &t);
for(i = 0; i < t; i++)
{
count = 0;
fgets(input, 5000, stdin);

// token whitespace to language
token = strtok(input, " ");
strcpy(lang[0], token);
for(j = 1; token = strtok(NULL, " "); j++)
{
strcpy(lang[j], token);
count++;
}

// find same string lengh
for(j = 0; j < MAXDIC; j++)
for(k = 0; k < count; k++)
if(strlen(dic[j]) == strlen(lang[k])
{
for(l = 0; l < strlen(lang[k]); l++)
{
transTable[lang[k]
}
}
}
return 0;
}*/
/*
#include<stdio.h>
#include<string.h>

char match[27] = "ynficwlbkuomxsevzpdrjgthaq";

char trans(char ch)
{
int i;

for(i = 0; i < strlen(match); i++)
if(match[i] == ch)
return i+97;
}

int main(void)
{
int i, j, t;
char input[5000], output[5000];

freopen("in.txt", "r", stdin);
freopen("out.txt", "w", stdout);

scanf("%d ", &t);
for(i = 0; i < t; i++)
{
fgets(input, 5000, stdin);

for(j = 0; input[j] != NULL; j++)
{
if(input[j] == ' ')
output[j] = ' ';
else
output[j] = trans(input[j]);
}
output[j-1] = 0;

printf("Case #%d: %s\n", i+1, output);
}

return 0;
}
*/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define MAXSAMPLE 2000000

char oriNumber[8], cmpNumber[8], flag[8]="";
char chk[MAXSAMPLE];
int sizeNumber, count, start, end;

void proc(int set)
{
	int cmp, ori;

	if(sizeNumber > set)
	{
		for(int i = 0; i < sizeNumber; i++)
		{
			// 숫자가 사용된거면 건너뛰기
			if(flag[i]) continue;

			// 지정된 위치에 특정 값 넣어서 스왑
			cmpNumber[set] = oriNumber[i];

			// 사용됬다고 표시
			flag[i] = 1;

			// 그 다음 처리
			proc(set + 1);

			// 사용 해제
			flag[i] = 0;
		}
	} else {
		// 마지막이면 비교할 숫자 완성
		cmp = atoi(cmpNumber);
		ori = atoi(oriNumber);
		// start와 end의 사이값이고 원래값과 다르고 체크가 안된거면
		if(cmp >= start && cmp <= end && cmp != ori && !(chk[cmp] || chk[ori]))
		{
			chk[cmp] = 1;
			chk[ori] = 1;
			count++;
			printf("origin : %s, cmp : %s\n",oriNumber, cmpNumber);
		}
	}
}

int main(void)
{
	int i, j, k, l, m, t, index;
	char *token, cmp1[8], cmp2[8];

	scanf("%d", &t);

	for(i = 0; i < t; i++)
	{
		memset(chk, 0, MAXSAMPLE);
		count = 0;

		scanf("%d %d", &start, &end);
		for(j = start; j <= end; j++)
		{
			// 숫자를 문자열로
			sprintf(oriNumber, "%d", j);
			sizeNumber = strlen(oriNumber);

			// 일의자리는 break;
			if(sizeNumber == 1) break;

			for(k = 1; k < sizeNumber; k++)
			{
				for(index = 0, l = 0; l < k; l++)
				{
					cmp1[index++] = oriNumber[l];
				}
				cmp1[index] = 0;
				for(index = 0, l = k; l < sizeNumber; l++)
				{
					cmp2[index++] = oriNumber[l];
				}
				cmp2[index] = 0;
			}

			//proc(0);

		}

		// 결과 출력
		//printf("Case #%d: %d\n", i+1, count);

	}
}