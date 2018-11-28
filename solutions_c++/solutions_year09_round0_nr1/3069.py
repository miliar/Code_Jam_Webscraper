#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
bool word[15][26];
bool words[26][26][26][26][26];
int L, N, D,ans;
char in[500];
vector<string> lib;
vector<int> call;
vector<char> ind[15];
void back(char index,vector<int>& b)
{
	if ( index == L )
	{
		ans += b.size();
		return ;
	}
	if ( !b.size() )
		return;
	int j;
	vector<int> c;
	bool find = false;
	for (int i=0; i< ind[index].size();i++ )
	{
		if ( !word[index][ind[index][i]-'a'] )
			continue;
		c.clear();
		find = false;
		for ( j=0; j<b.size();j++ )
		{
			if ( lib[b[j]][index] == ind[index][i] )
			{
				if ( !find)
					find = true;
				c.push_back(b[j]);
			}
			else if  ( find )
			{
				break;
			}
		}
		back(index+1,c);
	}
}
void reading(int& j,int& dex)
{
	j++;
	while ( in[j] != ')' )
	{
		ind[dex].push_back(in[j]);
		j++;
	}
}
int main()
{
	int i,j,dex,len;
	scanf("%d%d%d",&L,&D,&N);
	gets(in);
	for ( i =0; i< D; i++ )
	{
		gets(in);
		for ( j =0; j<L; j++ )
		{
			if ( j == 4 )
			{
				words[in[0]-'a'][in[1]-'a'][in[2]-'a'][in[3]-'a'][in[4]-'a'] = 1;
			}
			word[j][in[j]-'a'] = 1;
		}
		lib.push_back(in);
		call.push_back(i);
	}
	sort(lib.begin(),lib.end());
	for ( i= 1; i<= N; i++ )
	{
		for ( j=0; j<L; j++ )
			ind[j].clear();
		ans = 0;
		gets(in);
		len = strlen(in);
		for ( dex = j=0; j<len; j++,dex++ )
		{
			
			if ( in[j] == '(' )
			{
				reading(j,dex);
			}
			else
			{
				ind[dex].push_back(in[j]);
			}
		}
		back(0,call);
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}