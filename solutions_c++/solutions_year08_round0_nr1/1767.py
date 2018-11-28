#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

char szEngine[100][105] = {0};
char szQuery[1000][105] = {0};
char enginhash[100];
int isFull;
int s, q, n;

int main()
{
	ifstream datain("A-large.in");
	ofstream dataout("A-large.out");
	int ci, cj, ck;
	int count;
	char temp[10];

	datain >> n;
	for(ci = 0; ci < n; ci++)
	{
		datain >> s;
		datain.getline(temp, 10);  // erase the enter char
		for(cj = 0; cj < s; cj++)
			datain.getline(szEngine[cj], 101);
		datain >> q;
		datain.getline(temp, 10);  // erase the enter char
		for(cj = 0; cj < q; cj++)
			datain.getline(szQuery[cj], 101);
		count = 0;
		cj = 0;
		memset(enginhash, 0, sizeof(enginhash));
		isFull = s;
		while(cj < q)
		{
			for(ck = 0; ck < s; ck++)
			{
				if(strcmp(szEngine[ck], szQuery[cj]) == 0)
				{
					if(enginhash[ck] == 0)
					{
						enginhash[ck] = 1;
						isFull--;
					}
					break;
				}
			}
			if(0 == isFull)
			{
				count++;
				isFull = s - 1;
				memset(enginhash, 0, sizeof(enginhash));
				enginhash[ck] = 1;
			}
			cj++;
		}
		dataout << "Case #" << ci + 1 << ": " << count << endl;
	}
	return 0;
}
