#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int main()
{
	freopen("tongue.in", "r", stdin); freopen("tongue.out","w",stdout);
	int i, j, n;
	string s;
	char ar[30];
	ar[24] = 'a';
	ar[13] = 'b';
	ar[5] = 'c';
	ar[8] = 'd';
	ar[2] = 'e';
	ar[22] = 'f';
	ar[11] = 'g';
	ar[1] = 'h';
	ar[10] = 'i';
	ar[20] = 'j';
	ar[14] = 'k';
	ar[12] = 'l';
	ar[23] = 'm';
	ar[18] = 'n';
	ar[4] = 'o';
	ar[21] = 'p';
	ar[25] = 'q';
	ar[15] = 'r';
	ar[3] = 's';
	ar[17] = 't';
	ar[9] = 'u';
	ar[6] = 'v';
	ar[19] = 'w';
	ar[7] = 'x';
	ar[0] = 'y';
	ar[16] = 'z';
	scanf("%d\n", &n);
	for (i = 0; i < n; i++)
	{
		getline(cin, s);
		for (j = 0; j < s.length(); j++) 
			if (s[j] != ' ') s[j] = ar[ int(s[j]-'a') ];
		cout << "Case #" << i+1 << ": " << s << endl;
	}
}