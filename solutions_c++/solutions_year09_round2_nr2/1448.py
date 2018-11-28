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

int cnt[10],digit[22];

ll t,c,num,index,ans,cur;

void solve(int range)
{
	int i,cn = range - 1,minV;
	for(i = 0;i <= range - 1;i++) if(digit[i] > digit[range]) {minV = i;break;}
	cnt[digit[minV]]--;
	for(i = 0;i <= range;i++)
	{
		cnt[digit[i]]++;
	}
	digit[range] = digit[minV];
	for(i = 0;i <= 9;i++)
	{
		while(cnt[i] > 0)
		{
			digit[cn--] = i,cnt[i]--;
		}
	}
}

void solve2()
{
	int i,minV = 10,cn = index - 1;
	for(i = 0;i < index;i++) 
	{
		cnt[digit[i]]++;
		if(digit[i] > 0) minV = min(digit[i],minV);
	}
	cnt[minV]--,digit[index] = minV,cnt[0]++;
	for(i = 0;i <= 9;i++)
	{
		while(cnt[i] > 0)
		{
			digit[cn--] = i,cnt[i]--;
		}
		if(cn == -1) break;
	}
}

int main()
{
	freopen("D:\\VC project\\ForTest\\Debug\\input.in","r",stdin);
	freopen("D:\\VC project\\ForTest\\Debug\\out.txt","w",stdout);
	ll i,j;
	cin >> t;
	for(c = 1;c <= t;c++)
	{
		cin >> num;
		memset(cnt,0,sizeof(cnt));
		i = num,index = 0;
		while(i != 0)
		{
			j = i % 10,digit[index++] = j;
			i /= 10;
		}
		cur = -1;
		for(i = 1;i < index;i++) if(digit[i] < digit[i - 1]) {cur = i;break;}
		if(cur != -1)
		{
			solve(cur);
			ans = 0;
			for(i = 0;i < index;i++) ans += (int)pow(10.0,(double)i) * digit[i];
		}
		else
		{
			solve2();
			ans = 0;
			for(i = 0;i <= index;i++) ans += (int)pow(10.0,(double)i) * digit[i];
		}
		
		cout << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}