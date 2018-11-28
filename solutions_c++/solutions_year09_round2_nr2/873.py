#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	char s[30], t[30];
	int n;
	int k=0;
	cin >> n;
	while(n--)
	{
		cin >> s;
		t[0] = '0';
		cout << "Case #" << ++k << ": ";
		strcpy(t+1, s);
		next_permutation(t, t+strlen(t));
		int i=0;
		while(t[i]=='0') i++;
		cout << t+i << endl;
	}
}
