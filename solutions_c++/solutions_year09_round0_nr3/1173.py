#include <iostream>
using namespace std;
const int mod = 10000;
char pat[] = "welcome to code jam";
int f[40];
bool check(char a)
{
	if(a == ' ') return true;
	if(a <= 'z' && a >= 'a') return true;
	return false;
}
int main()
{
	int n;
	cin >> n;
	for(int i=1; i<=n; i++)
	{
		char s[550];
		if(i == 1) cin.getline(s,5);
		cin.getline(s, 550);
		//cout << s << endl;
		for(int k=0; k<30; k++) f[k] = 0;
		f[0] = 1;
		for(int j=0; check(s[j]); j++)
		{
			for(int k=19; k>0; k--) if(pat[k-1] == s[j]) f[k] = (f[k] + f[k-1]) %mod;
			//for(int k=0; k<20; k++) cout << f[k] << " ";
			//cout << endl;
		}
		cout << "Case #" << i << ": ";
		printf("%04d", f[19]);
		cout << endl;
	}
	return 0;
}
