#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <memory.h>

using namespace std;
__int64 doit(string s)
{
//	string temp;
	int i,j;
	char last = '\n';
	int times=0;
	int base;
	int array[2][256]; //用一个2维数组记录每一个字符代表的数字；
	for(i=0;i<2;i++)
		for(j=0;j<256;j++)
			array[i][j] = 0;

	  //string::iterator j;
	  vector<int> number;
	 // vector<int>::iterator numIter;
	  vector<char> temp;
	  vector<char> sourceBackup;
	  const char* source = new char[s.size()+1];
	  source = s.c_str();
	  for (i=0;i<s.size();i++)
	  {
		temp.push_back(source[i]);
	  }
	  sourceBackup = temp;
	  sort(temp.begin(),temp.end());
	  //第一位可以为0；
	  for(i=0;i<s.size();i++)
	  {
		if(temp[i]!=last)
		{
				last = temp[i];
				times++; //进制
		}
		
	  }
  //先保存进制
	  base = times;
	  if(1 == times )
		  base =2; //不存在1进制
  
  times =1;
  //记录每个字符代表的含义
   //第一位总是为1
  //第二位总是为0
  for(i=0;i<s.size();i++)
  {
	  if(array[1][sourceBackup[i]]==0)
	  {
	  	array[1][sourceBackup[i]] = times;
		times++;
	  }
	 // else
	//	  array[1][sourceBackup[i]] = times;

  }
	//还需要对每个字符的意义进行调整
//  array[1][sourceBackup[0]] = 1
  if(1 == s.size())
  {
	number.push_back(1);
  }
  if(2<=s.size() )
  {
	  number.push_back(1);
	  for(i=1;i<s.size();i++)
	  {
		number.push_back(array[1][sourceBackup[i]]);
	  }
  }
  //将==2的数==0，〉2的数减1
	for (i=0;i<number.size();i++)
	{
		if(2 == number[i])
			number[i] =0;
		if(number[i]>2)
			number[i]=number[i]-1;
	}
	//将这一数转为10进制数
  __int64 total =0;
  __int64 k = 1;
  for(i=number.size()-1;i>=0;i--)
  {
	total += number[i]*k;
	k=k*base;
  }
  
  return total;

}

int main(int argc, char **argv){
	  int T;
	  string s;
	  
	  __int64 num;
	  cin>>T;
	  for(int I=1; I<=T; I++) {
		
		cin>>s;
		num = doit(s);
		//cout << "Case #"<<I<<": "<<num<<endl;
		printf("Case #%d: %I64d\n",I,num);
		
	  }
	  return 1;
	}