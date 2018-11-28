#include <iostream>

using namespace std;

int word[5000][15];
bool token[15][26];

int l, d, n;

void init()
{
	char s[100];
	for (int i=0;i<d;i++)
	{
		cin>>s;
		for (int j=0;j<l;j++)
			word[i][j]=s[j]-'a';
	}
}
void init_token()
{
	char c;
	memset(token,false,sizeof(token));
	for (int i=0;i<l;i++)
	{
		cin>>c;
		if (c=='(')
		{
			while (cin>>c && c!=')')
				token[i][c-'a']=true;
		}
		else token[i][c-'a']=true;
	}
}
int calc()
{
	int ans = 0;
	for (int i=0;i<d;i++)
	{
        int j = 0;
		for (j=0;j<l;j++)
			if (!token[j][word[i][j]]) break;
		if (j==l) ans++;
	}
	return ans;
}
int main()
{
	cin>>l>>d>>n;
	init();
	for (int i=0;i<n;i++)
	{
		init_token();
		cout<<"Case #"<<i+1<<": "<<calc()<<endl;
	}
}
