#include <iostream>
using namespace std;

string A[] = {
	"ejp mysljylc kd kxveddknmc re jsicpdry",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

string B[] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};

char M[256];

int main()
{
	int k = 0;
	for(int i = 0; i < 3; ++i)
		for(int j = 0; j < A[i].size(); ++j)
			M[A[i][j]] = B[i][j];
	M['z'] = 'q';
	M['q'] = 'z';
	
	int z;
	string s;
	
	cin >> z;
	getline(cin, s);
	for(int t = 1; t <= z; ++t)
	{
		cout << "Case #" << t << ": ";
		string s;
		getline(cin, s);
		for(int i = 0; i < s.size(); ++i)
			cout << M[s[i]];
		cout << endl;
	}
	return 0;
}
