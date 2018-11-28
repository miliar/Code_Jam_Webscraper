#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstring>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;

int p10[9];

int rot(int num, int len)
{
	int dig = num%10;
	num /= 10;
	num += dig*p10[len-1];
	return num;
}

int getLen(int num)
{
	int len = 0;
	while(num>0)
		len++, num/=10;
	return len;
}

int rot(int num)
{
	return rot(num, getLen(num));
}


int calcRotations(int num, int A, int B)
{
	int ans = 0;
	int bck = num;
	int len = getLen(num);
	num = rot(num, len);
	for(int i=1; i<len ; i++, num=rot(num, len))
	{
		if(A<=num && num<=B && bck < num)
			ans++;
		if(bck == num)
			break;
	}
	return ans;
}

//*
ifstream fin("C-large.in");
#define cin fin
ofstream fout("C-large.out");
#define cout fout
//*/

int main()
{
	p10[0]=1;
	for(int i=1; i<9; i++)
		p10[i] = p10[i-1]*10;

	int tc;
	cin>>tc;
	for(int t=1; t<=tc; t++)
	{
		int A, B;
		cin>>A>>B;
		int ans = 0;
		for(int i=A; i<=B; i++)
		{
			ans += calcRotations(i, A, B);
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
