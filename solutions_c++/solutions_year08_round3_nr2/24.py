#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "in.txt"
#define OUTPUT "out.txt"

char str[44];
long long wsum = 0;

void DFS(char p, long long sum, long long curnum, char sign)
{
	if (p==strlen(str)) {
		sum += curnum*sign;
		if (sum % 2 == 0 || sum%3 == 0 || sum % 5 ==0 || sum % 7 == 0)
			wsum++;
		return ;
	}
	// -
	DFS(p+1, sum + curnum*sign, str[p]-'0', -1);
	// +
	DFS(p+1, sum + curnum*sign, str[p]-'0', 1);
	// Nothing
	DFS(p+1, sum, curnum*10+str[p]-'0', sign);
}

int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	for (int i=0; i<t; i++) {
		cin >> str; wsum=0;
		DFS(1, 0, str[0]-'0',1);
		cout << "Case #" << i+1 << ": " << wsum << endl;
	}

	return 0;
}