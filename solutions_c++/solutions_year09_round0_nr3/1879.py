#include <cstdio>
#include <cstring>

int search(const char str[], const char welcome[], int textlen, int wellen, int start = 0, int pos = 0)
{
	if (pos >= wellen)
		return 1;
	
	int sum = 0;
	for(int i=start;i<textlen;i++)
		if (welcome[pos] == str[i])
			sum += search(str, welcome, textlen, wellen, i + 1, pos + 1);
	
	if (sum > 9999)
		return sum % 10000;
	return sum;
}

int main(void)
{
	char welcome[] = "welcome to code jam";
	int n;
	scanf("%d\n", &n);
	
	for(int k=0;k<n;k++)
	{
		char str[512];
		fgets(str, 512, stdin);
		
		int wellen = strlen(welcome);
		char stripped[512];
		int pos = 0;
		for(int i=0;i<(int)strlen(str);i++)
		{
			for(int j=0;j<wellen;j++)
				if (welcome[j] == str[i])
				{
					stripped[pos] = str[i];
					pos++;
					break;
				}
		}
		stripped[pos] = '\0';
		
		printf("Case #%d: %04d\n", k+1, search(stripped, welcome, strlen(stripped), strlen(welcome)));
	}
	
	return 0;
}