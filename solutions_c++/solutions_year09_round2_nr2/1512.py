//Decision Tree - Round 1B

#include <iostream> 
#include <cmath> 
#include <vector> 
#include <string> 
#include <map> 
#include <iomanip>

using namespace std;

char number[30];
char temp[30];

bool sortt(char a, char b)
{
	if(a == '0') return false;
	if(b == '0') return true;
	return a <= b;
}

int main()
{
	int n;
	scanf("%i\n", &n);
	int first;
	
	for(int i = 0; i < n; i++)
	{
		scanf("%s\n", number);
		strcpy(temp,number);
		next_permutation(number, number+strlen(number));
		if(atoi(number) <= atoi(temp))
		{
			if(atoi(number) < 10)
			{
				temp[strlen(temp)+1] = '\0';	
				temp[strlen(temp)] = '0';
			}
			else
			{
				sort(temp,temp+strlen(temp),sortt);
				temp[strlen(temp)+1] = '\0';
				for(int j = strlen(temp); j > 1; j--)
				{
					temp[j] = temp[j-1];
				}
				temp[1] = '0';
				first = strlen(temp) - 1;
				for(int k = strlen(temp) - 1; k > 1; k--)
				{
					for(int j = k; j > 1; j--)
					{
						if(temp[j] != '0')
						{
							swap(temp[j], temp[k]);
							break;
						}	
					}
				}
			}
//			865300 356800 3056800 3056008
			strcpy(number,temp);
		}
		
		printf("Case #%i: %s\n", i+1, number);
	}
}
