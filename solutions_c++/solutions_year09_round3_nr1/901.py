#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <memory>
#include <sstream>

using namespace std;

typedef long long ll;

char input[62];

int isVisited[36],result[62];

int ans[30],tmpAns[30],digit;

int t,c,len,index,maxV,start,totalDigit;

int getIndex(char a)
{
	if(a >= 'a' && a <= 'z') return a - 'a';
	else return a - '0' + 26;
}

void multiply(int num)
{
	int value,add = 0;
	for(int i = 0;i < digit;i++)
	{
		value = tmpAns[i] * num + add;
		add = value / 10;
		tmpAns[i] = value % 10;
	}
	if(add > 0) tmpAns[digit++] = add;
}

int main()
{
	freopen("D:\\VC project\\ForTest\\Debug\\input.in","r",stdin);
	freopen("D:\\VC project\\ForTest\\Debug\\out.txt","w",stdout);
	int i,j;
	int tmp[30];
	cin >> t;
	c = 0;
	while(++c <= t)
	{
		scanf("%s",input);
		len = strlen(input);
		memset(isVisited,-1,sizeof(isVisited));
		isVisited[getIndex(input[0])] = 1;
		totalDigit = 0;
		result[0] = 1;
		maxV = 1;
		for(i = 1;i < len;i++) 
		{
			if(input[i] != input[0]) {isVisited[getIndex(input[i])] = 0;start = i + 1;result[i] = 0;break;}
			else result[i] = 1;
		}
		for(i = start;i < len;i++)
		{
			index = getIndex(input[i]);
			if(isVisited[index] != -1) {result[i] = isVisited[index];continue;}
			isVisited[index] = ++maxV,result[i] = maxV;
		}
		memset(ans,0,sizeof(ans));
		totalDigit = 0;
		for(i = 0;i < len;i++) 
		{
			memset(tmpAns,0,sizeof(tmpAns));
			tmpAns[0] = result[len - 1 - i];
			digit = 1;
			for(j = 0;j < i;j++)
			{
				multiply(maxV + 1);
			}
			if(totalDigit < digit) totalDigit = digit;
			int add = 0,value;
			for(j = 0;j < totalDigit;j++)
			{
				value = ans[j] + tmpAns[j] + add;
				add = value / 10;
				ans[j] = value % 10;		
			}
			if(add > 0) ans[totalDigit++] = add;
		}
		cout << "Case #" << c << ": ";
		for(i = totalDigit - 1;i >= 0;i--)
		{
			cout << ans[i];
		}
		cout << endl;
	}
//	while(1);
	return 0;
}