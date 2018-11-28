// CJ09R1BB.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int cases;
	cin>>cases;
	char buf[255];
		cin.getline(buf,255);

	for(int c=0;c<cases;++c){
		memset(buf,0,255);
		cin.getline(buf,255);

		string str(buf);
		while(str.size()>0 && str[0]=='0') str.erase(str.begin());

		if(!next_permutation(str.begin(),str.end())){
			prev_permutation(str.begin(),str.end());
			str.insert(str.begin(),'0');
			next_permutation(str.begin(),str.end());
		}

		while(str.size()>0 && str[0]=='0') str.erase(str.begin());
		cout<<"Case #"<<(c+1)<<": "<<str<<endl;
	
	}

	return 0;
}

