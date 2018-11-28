#include <iostream>
using namespace std;

string mmap = "yhesocvxduiglbkrztnwjpfmaq";

int main (void)
{
	freopen ("test.in", "r", stdin);
	freopen ("output.txt", "w", stdout);
	int t;
	char s[200];
	scanf ("%d\n", &t);
	for (int x=1; x <= t; x++)
	{
		cout << "Case #" << x << ": ";
		gets (s);
//		cout << s << endl;
		for (int i=0; i<(int) strlen(s); i++)
		{
			if (s[i] == ' ') 
			{
				cout << ' ';
				continue;
			}
			cout << mmap[s[i] - 'a'];
		}
		cout << endl;
	}
    return 0;
}
