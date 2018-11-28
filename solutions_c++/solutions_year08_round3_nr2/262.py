#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char s[100];
char o[100];
int l;
int cnt;

int isUgly()
{
	int i;
	__int64 sum = 0;
	__int64 temp = 0;
	int oper = 1;

	temp = s[0]-'0';

	for ( i = 1 ; i < l ; i++ )
	{
		if (o[i] == 0)
		{
			temp = temp*10 + (s[i]-'0');
		}
		else if (o[i] == 1)
		{
			if ( oper == 1 ) 
				sum+=temp;
			else
				sum-=temp;

			oper = 1;
			temp = (s[i]-'0');
		}
		else if (o[i] == 2)
		{
			if ( oper == 1 ) 
				sum+=temp;
			else
				sum-=temp;

			oper = 2;
			temp = (s[i]-'0');
		}
		else 
		{
			printf("error\n");
			exit(1);
		}
	}

	if ( oper == 1 )
		sum+=temp;
	else
		sum-=temp;

	if ( sum == 0
		|| (sum % 2 == 0)
		|| (sum % 3 == 0)
		|| (sum % 5 == 0)
		|| (sum % 7 == 0) )
		return 1;

	return 0;
}


int cal(int b)
{
	if (b == l) {
		if ( isUgly() )
			cnt++;
		return 0;
	}

	o[b] = 0;
	cal(b+1);

	o[b] = 1;
	cal(b+1);

	o[b] = 2;
	cal(b+1);

	return 0;
}


int main(){
	int T, Ti;

	scanf("%d", &T);

	for ( Ti = 0; Ti < T; Ti++ )
	{
		printf("Case #%d: ", Ti+1);

		scanf("%s", s);
		l = strlen(s);

		cnt = 0;
		memset(o, 0, sizeof(o));
		cal(1);
		
		printf("%d\n", cnt);
	}

	return 0;
}

