#include <iostream>

using namespace std;
int main ()
{
	int i, j, n; 
    char c[200], g[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	cin>>n;
	cin.getline(c, 200, '\n');
	for (i=0;i<n;i++)
	{
        cin.getline(c, 200, '\n');
		cout<<"Case #"<<i+1<<": ";
		for (j=0;j<strlen(c);j++)
		{
			if (isalpha(c[j]))
				cout<<g[((int)(c[j])) % 97];
			else
				cout<<c[j];
		}
		cout<<endl;
	}
	return 0;
}
