#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <fstream>
using namespace std;



bool IsUgly(long long n){
	if (n%2==0 || n%3==0 || n%5==0 || n%7==0)
	{
		return true;
	}
	else{
		return false;
	}
}
//long long test(string str){
//	long long ret=0;
//	for (int i=0;i<str.length();++i)
//	{
//		ret*=10;
//		ret+=(str[i]-'0');
//	}
//	if (IsUgly(ret))
//	{
//		++ans;
//	}
//	for (int i=1;i<=str.length();++i)
//	{
//		long long tmp=test(str.substr(0,i))+test(str.substr(i,str.length()-i));
//
//	}
//
//}
char command[50];
int digitlength;
string input;
long long ans=0;


void Generator(int i){
	if (i==digitlength)
	{
		long long left=0;
		long long right=input[0]-'0';
		char c='+';
		for (int j=0;j<digitlength;++j)
		{
			if (command[j]==' ')
			{
				right=right*10+input[j+1]-'0';
				continue;
			}
			switch(c)
			{
			case '+':
				left=left+right;
				right=0;
				break;
			case '-':
				left=left-right;
				right=0;
				break;
			/*case ' ':
				right=right*10+input[j+1]-'0';
				break;*/
			}
			right=input[j+1]-'0';
			c=command[j];
		}
		switch(c)
		{
		case '+':
			left=left+right;
			right=0;
			break;
		case '-':
			left=left-right;
			right=0;
			break;
	/*	case ' ':
			right=right*10+input[j+1]-'0';
			break;*/
		}
		if (IsUgly(left))
		{
			++ans;
		}
		return ;

	}
		command[i]='+';
		Generator(i+1);
		command[i]='-';
		Generator(i+1);
		command[i]=' ';
		Generator(i+1);
}
int main()
{
	ifstream fin("in.in");
	ofstream fout("out.out");
	int N;
	fin>>N;
	for (int cc=1;cc<=N;++cc)
	{
		fin>>input;
		digitlength=input.length()-1;
		ans=0;
		if (input.length()>0){
			Generator(0);
		}
		fout<<"Case #"<<cc<<": "<<ans<<endl;
	}

	return 0;
}

