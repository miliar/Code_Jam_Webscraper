#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin >>n;
	char c;
	cin.get(c);
	char m[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char s[100][101];
	for (int i=0; i<n; ++i)
		cin.getline(s[i],101);
	for (int i=0; i<n; ++i){
		cout <<"Case #" <<i+1 <<": ";
		for (int j=0; s[i][j]!='\0'; ++j)
			if (s[i][j]!=' ')
				cout <<m[s[i][j]-'a'];
			else
				cout <<" ";
		cout <<endl;
	}
	return 0;
}