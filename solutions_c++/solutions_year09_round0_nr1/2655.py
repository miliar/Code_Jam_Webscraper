#include <iostream>
#include <vector>
#include <string> 

using namespace std;

int main()
{
	int L,D,N;
	scanf("%d %d %d",&L,&D,&N);
	vector<string> words(D);
	char word[20];
	for(int i=0;i<D;i++)
	{
		scanf("%s",word);
		words[i] = word;
	}
	bool P[L][27];
	int casen = 1;
	while(N--)
	{
		char wordl[1000];
		scanf("%s",wordl);
		string t = wordl;
		for(int i=0;i<L;i++) for(int j=0;j<27;j++) P[i][j] = 0;
		int ctr = 0;
		bool paren = false;
		for(int i=0;i<t.length();i++)
		{
			if(t[i]=='(') paren = true;
			else if(t[i]==')') {ctr++;paren=false;}
			else {P[ctr][t[i]-97] = 1; if(!paren) ctr++; }
		}
		int ans = 0;
		for(int i=0;i<D;i++)
		{
			bool f = true;
			for(int j=0;j<L && f;j++)
				f = P[j][words[i][j]-97];
			if(f) ans++;
		}
		printf("Case #%d: %d\n",casen++,ans);
	}
}
