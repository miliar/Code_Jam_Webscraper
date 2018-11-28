#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define MAX 15

long long count1 = 0;
char ch[MAX*2];
int len = 0;

void sep(int low, long long);
bool isUgly(long long num);

void main()
{
	int N;
	long long re = 0;
	ifstream in("in.txt");
	ofstream out("out.txt");
	in>>N;
	for(int i = 0; i < N; ++ i)
	{
		count1 = 0;
		for(len = 0; len < MAX; ch[len++] = '\0');
		in>>ch;
	//	cin>>ch;
		for(len = 0; ch[len] != '\0'; ++ len);
		sep(0, 0);

		out<<"Case #"<<i+1<<": "<<count1<<endl;
		cout<<"Case #"<<i+1<<": "<<count1<<endl;

	}
	out.close();
	in.close();
	system("pause");
}

void sep(int low, long long num)
{
	if(low == len) 
	{
		if(isUgly(num)) ++ count1;
		return ;
	}
	for(int i = 1; i <= len - low; ++ i)
	{	
		int j = 0;
		long long t = 0;
		while(j < i)
		{
			t = t * 10 + ch[low + j] - '0';
			++ j;
		}
		sep(low + i, t + num);
		if(low != 0)
			sep(low + i, -t + num);
	}
}

bool isUgly(long long num)
{
	if(num == 0) return true;
	if(num % 2 == 0) return true;
	if(num % 3 == 0) return true;
	if(num % 5 == 0) return true;
	if(num % 7 == 0) return true;
	return false;
}