#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int Mix[26][26];
int Clr[26][26];

vector<int> ClrList(vector<int> source)
{
	if(source.size() == 1) return source;
	vector<int> result;
	int lastNo = source.size()-1;
	for(int i=0;i<lastNo;i++)
	{
		//printf("%d %d\n",source[i]-'A',source[lastNo]-'A');
		int check = Clr[source[i]-'A'][source[lastNo]-'A'];
		if(check)
			return result;
	}
	return source;
}

vector<int> Tranform(vector<int> source)
{
	if(source.size() == 1) return source;
	int lastNo = source.size()-1;
	vector<int> result;
	for(int i=0;i<lastNo-1;i++)
	{
		result.push_back(source[i]);
	}
	int check = Mix[source[lastNo]-'A'][source[lastNo-1]-'A'];
	if(check != 0)
	{
		result.push_back(check);
	}
	else
	{
		result.push_back(source[lastNo-1]);
		result.push_back(source[lastNo]);
	}
	return result;
}

void clearAll()
{
	for(int i=0;i<26;i++)
		for(int j=0;j<26;j++)
		{
			Mix[i][j] = 0;
			Clr[i][j] = 0;
		}
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int round=1;round<=T;round++)
	{
		clearAll();
		//input
		int C,D;
		scanf("%d",&C);
		for(int i=0;i<C;i++)
		{
			char temp[5];
			scanf("%s",temp);
			Mix[temp[0]-'A'][temp[1]-'A'] = temp[2];
			Mix[temp[1]-'A'][temp[0]-'A'] = temp[2];
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++)
		{
			char temp[5];
			scanf("%s",temp);
			Clr[temp[0]-'A'][temp[1]-'A'] = 1;
			Clr[temp[1]-'A'][temp[0]-'A'] = 1;
			//printf("%d %d\n",temp[0],temp[1]);
		}
		//printf("-------");
		int N;
		char inputStr[200];
		scanf("%d %s",&N,inputStr);
		///////////////////////////////////////////
		vector<int> result;
		for(int i=0;i<N;i++)
		{
			result.push_back(inputStr[i]);
			int Csize = result.size();
			vector<int> resTemp = Tranform(result);
			resTemp = ClrList(resTemp);
			swap(resTemp,result);
		}
		printf("Case #%d: [",round);
		for(int i=0;i<result.size();i++)
			if(i == 0)
				printf("%c",result[i]);
			else
				printf(", %c",result[i]);
		printf("]\n");
	}
	return 0;
}
