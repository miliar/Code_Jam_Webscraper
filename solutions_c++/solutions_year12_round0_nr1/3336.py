#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int tsts;
string a;
char M[26]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
int main()
{
	cin >> tsts;
	scanf("\n");
	for(int i=0;i<tsts;i++)
	{
		getline(cin,a);
		cout << "Case #" << i+1 << ": ";
		for(int i=0;i<a.size();i++)
			if(a[i]==' ')
				cout << " ";
			else
				for(int j=0;j<26;j++)
					if(M[j]==a[i])
						cout << char(j+'a');
		cout << endl;
	}
	return 0;
}
