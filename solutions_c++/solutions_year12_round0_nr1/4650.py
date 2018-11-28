#include <iostream>
using namespace std;

const int g_size = 101;

char g_mapping[] = {
	'y',
	'h', 
	'e', 
	's', 
	'o', 
	'c', 
	'v', 
	'x', 
	'd', 
	'u', 
	'i', 
	'g', 
	'l', 
	'b', 
	'k', 
	'r', 
	'z', 
	't',
	'n', 
	'w', 
	'j', 
	'p', 
	'f', 
	'm', 
	'a', 
	'q'
};

void translate(int caseNum)
{
	char string[g_size];
	cin.getline(string, g_size, '\n');
	
	int i=0;
	for( ; i<g_size && string[i] != '\n'; ++i)
	{
		int mapIndex = string[i] - 'a';
		if (mapIndex >= 0 && mapIndex < 26)
		{
			string[i] = g_mapping[ mapIndex ];
		}
	}
	printf("Case #%d: %s\n", caseNum, string);
}

int main()
{
	int n = 0;
	scanf("%d\n", &n);
	
	for(int i=1; i<=n; ++i) 
		translate(i);
	
	return 0;
}