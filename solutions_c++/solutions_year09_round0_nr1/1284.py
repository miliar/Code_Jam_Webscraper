//CODEJAM A

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	//vars
	ifstream cin ("A-small.in");
	ofstream cout ("A-large.out");
	int L,D,N,a,b,c,d,fox;
	char ch;
	string s;
	bool let[20][30];
	static int word[5005][20];
	//input dictionary
	cin >> L >> D >> N;
		for (a=0; a<D; a++)
			for (b=0; b<L; b++)
			{
				cin >> ch;
				word[a][b]=ch-'a';
			}
	//testcase loop
		for (a=1; a<=N; a++)
		{
			//input
			memset(let,0,sizeof(let));
			cin >> s;
			b=0;
			d=s.size();
				for (c=0; c<d; c++,b++)
					if (s[c]=='(')
					{
						c++;
							while (s[c]!=')')
								let[b][s[c++]-'a']=1;
					}
					else
						let[b][s[c]-'a']=1;
			//try each word
			fox=0;
				for (b=0; b<D; b++)
					for (c=0; c<=L; c++)
						if (c==L)
							fox++;
						else
						if (!let[c][word[b][c]])
							break;
			//output
			cout << "Case #" << a << ": " << fox << endl;
		}
	return(0);
}