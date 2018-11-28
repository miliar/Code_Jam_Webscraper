#include <iostream>
#include <string>

using namespace std;

int main() {
	int T, X;
	string S, G, a, b;
	char goolet[26];
	int lnum;
	//char a;

	int i;

	S = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz";
	G = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq";

	for(i = 0; i < 26; i++)
	{
		goolet[i] = i + 97;
	}

	for(i = 0; i < static_cast<int>(G.size()); i++)
	{
		if(G[i] == ' ')
			continue;
		lnum = static_cast<int>(G[i]) - 97;
		goolet[lnum] = static_cast<int>(S[i]);
	}

	cin >> T;
	cin.get();
	for(X = 1; X <= T; X++)
	{
		getline(cin, G);
		S.clear();

		for(i = 0; i < static_cast<int>(G.size()); i++)
		{
			if(G[i] == ' ')
				S.push_back(' ');
			else {
				lnum = static_cast<int>(G[i]) - 97;
				S.push_back(goolet[lnum]);
			}
		}

		cout << "Case #" << X << ": " << S << endl;
	}

}
