#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <cctype>
#include <stack>
 
using namespace std;
 
#define fe(i,a,n) for(int i = a, __n = n; i < __n; i++)
#define fi(i,a,n) for(int i = a, __n = n; i <= __n; i++)
#define LL long long
#define ULL unsigned long long
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define SI stack<int>
#define SS stack<string>
#define SD stack<double>
#define ERRO 1e-10
#define INF 1e+99
#define tr(i,s) for(typeof(s.begin()) i = s.begin(); i != s.end(); i++)
#define all(v) v.begin(), v.end()

int main()
{
	int a,b,c;
	cin >> c;
	string x;
	getline (cin,x);
	
	fe(i,0,c)
	{
		string y;
		getline (cin,y);
		
		stringstream ss (stringstream::in | stringstream::out);
		ss << y;
		char buffer[1000];
		char buffer2[1000];
		char *ret;
		ss >> buffer;
		//itoa(val,buffer,10);
		int length=0;
		while(buffer[length]!='\0') length++;
		if (next_permutation (buffer,buffer+length)==false)
		{
			while (buffer[0]=='0') next_permutation (buffer,buffer+length);
			buffer2[0]=buffer[0];
			buffer2[1]='0';
			fe(j,0,length)
				buffer2[j+2]=buffer[j+1];
			ret= buffer2;
		}
		else
		    ret= buffer;
		
		if (i!=c-1)
  		   cout << "Case #" << i+1 << ": " << ret << endl;
		else
  		   cout << "Case #" << i+1 << ": " << ret;
	}
	return 0;
}
