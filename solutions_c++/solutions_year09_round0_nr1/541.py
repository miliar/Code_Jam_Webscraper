#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
vector<string> wordsList;
vector<string> splitword;
int L,D,N;
bool split(string s)
{
	string res = "";
	bool flag = false;
	int count = 0;
	for(int i = 0;i < s.length();i++)
	{
		if(s[i] == '(') flag = true;
		else if(s[i] == ')')
		{
			flag = false;
			if(count >= L) return false;
			splitword[count] = res;
			count++;
			res = "";
		}
		else
		{
			if(flag) res += s[i];
			else {splitword[count] = s[i];count++;}
		}
	}
	return true;
}
int main()
{
	freopen("..\\s.in","r",stdin);
	freopen("..\\s.out","w",stdout);
	string s;
	scanf("%d%d%d",&L,&D,&N);
	for(int i = 0;i < L;i++) splitword.push_back("");
	for(int i = 0;i < D;i++)
	{
		cin>>s;
		wordsList.push_back(s);
	}
	for(int i = 1;i <= N;i++)
	{
		cin>>s;
		int res = 0;
		if(!split(s)) {printf("Case #%d: 0\n",i);return  0;}
		for(int j = 0;j < D;j++)
		{
			int flag = false;
			for(int k = 0;k < L;k++)
			{
				if(splitword[k].find(wordsList[j][k],0) == -1){flag = true;break;} 
			}
			if(!flag) res++;
		}
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}