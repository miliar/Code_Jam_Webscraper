#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int noc;
	cin >> noc;

	char arr[] = {'y',
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
			'q'};
	
	char garb;
		scanf("%c",&garb);
	int count = 0;
	while(noc--)
	{
		count ++;
		char line[1000];

		scanf("%[^\n]",line);
		scanf("%c",&garb);
		printf("Case #%d: ",count);
		for(int i=0;i<strlen(line);i++)
		{
			if(line[i] == ' ')
				cout << " ";
			else
				cout << arr[line[i] - 97];
		}
		cout << endl;
	}
	return 0;
}

