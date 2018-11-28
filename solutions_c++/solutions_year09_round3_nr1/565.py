#include <cstdio>
#include <cstring>

char message[71], number[256];
int ntest, nsymbol, len;
long long mini;

long long toDecimal(int b)
{
	long long result=0, multiplier=1;  
	for(int i = len - 1;i >= 0;--i)
	{
    	result+=(long long)(message[i] - '0')*multiplier;
		multiplier*=(long long)b;
	}  
	return result;
}

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		scanf("%s", message);
		memset(number, -1, sizeof(number));
		nsymbol = 0;
		len = strlen(message);
		for(int i = 0;i < len;++i)
		{
			if(number[message[i]] == -1)
			{
				if(!nsymbol)
					number[message[i]] = '1';
				else if(nsymbol == 1)
					number[message[i]] = '0';
				else
					number[message[i]] = nsymbol + '0';
				++nsymbol;
			}
			message[i] = number[message[i]];
		}
		if(nsymbol == 1)
			++nsymbol;
		printf("Case #%d: %lld\n", test, toDecimal(nsymbol));
	}
	return 0;
}
