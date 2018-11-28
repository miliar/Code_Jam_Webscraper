#include<iostream>
#include<queue>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
char str[10024];
vector<int>Base;
void init()
{
	int i , j;
	Base.clear();
	int len = strlen(str);
	str[len] = ' ';
	bool f = false;
	int sum =0;
	for(i = 0 ; i <= len ; i++)
	{
		if(str[i] >='0' && str[i] <= '9')
		{
			sum *= 10;
			sum += str[i] - '0';
		}
		else
		{
			Base.push_back(sum);
			sum =0;
		
		}
	}
}
int temp1[10024],temp2[10024];
bool biaoji[10000];
int change(int t)
{
	int Sum = 0;
	if(t==0)
		return 0;
	while(t > 0)
	{
		int tt = t%10;
		Sum = Sum + tt*tt;
		t/=10;
	}
	return Sum;
}
bool judge(int num , int base)
{
	int L = 0;
	while(num > 0)
	{
		temp1[L++] = num%base;
		num /= base;
	}
	//reverse(temp1 , temp1+L);
	memset(biaoji , 0 , sizeof(biaoji));
	int i , S =0;

	while(1)
	{
		S = 0;
		for(i = 0 ; i < L ; i++)
			S = S + temp1[i]*temp1[i];
		if(S == 1)
			return true;
		if(biaoji[S])
			break;
		biaoji[S] = true;
		L = 0;
		while(S > 0)
		{
			temp1[L++] = S%base;
			S/=base;
		}

	}
	return false;
}
bool check(int num)
{
	int i , l = Base.size();
	for(i =0 ; i < Base.size() ; i++)
	{
		if(!judge(num , Base[i]))
			break;
	}
	if(i == l)
		return true;
	return false;
}
int main()
{
	freopen("A-small-attempt0.in" , "r" , stdin);
	freopen("ans.out" , "w" , stdout);
	int T;
	scanf("%d" , &T);
	getchar();
	int CC = 0;
	while(T--)
	{
		CC++;
		gets(str);
		init();
		int i;
		for(i = 2 ; ; i++)
		{
			if(check(i))
			{
				printf("Case #%d: %d\n" , CC , i);
				break;
			}
		}
	}
	return 0;
}