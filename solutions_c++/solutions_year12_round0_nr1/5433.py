#include<iostream>
#include<string>
#include<cstdio>
using namespace std;

int main()
{
	char str[27] = {'y','h','e','s','o','c','v','x',
		'd','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int n;
	cin >> n;
	getchar();
	for(int i=1; i<=n; ++i) {
		string word;
		getline(cin,word);
		cout << "Case #" << i << ": ";
		for(int i=0; i<word.size(); ++i) {
			if(word[i] == ' ') printf(" ");
			else printf("%c", str[word[i]-'a']);
		}
		cout << endl;
	}
	return 0;
}
