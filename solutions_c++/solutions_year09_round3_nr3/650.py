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
#define INF 1e+9
#define tr(i,s) for(typeof(s.begin()) i = s.begin(); i != s.end(); i++)
#define all(v) v.begin(), v.end()
 
VI remove(int index, VI arr)
{
	fe(i,index+1,arr.size())
	{
		if(arr[index]!=arr[i]) break;
		arr[i]++;
	}
	for(int i=index-1; i>=0; i--)
	{
		if(arr[index]!=arr[i]) break;
		arr[i]++;
	}
	return arr;
}

long long weight(VI arr)
{
	long long ret=0;
	fe(i,0,arr.size())
	{
		ret+=arr[i];
	}
	return ret;
}
 
int main()
{
	int c;
	cin >> c;
	string x;
	getline (cin,x);
	
	fe(i,0,c)
	{
		int ret=0;
		
		int P, Q;
		cin >> P >> Q;
		VI main;
		fe(j,0,P)
		{
			main.push_back(0);
		}
		int arr[Q];
		fe(j,0,Q)
		{
			int a;
			cin >> a;
			arr[j]=a;
		}
		long long mini=INF;
		do
		{
			VI temp = main;
			fe(j,0,Q)
			{
				temp=remove(arr[j]-1,temp);
			}
			fe(k,0,P)
			//cout<<temp[k]<< " ";
			mini=min(mini,weight(temp));
			//cout << mini << endl;
		}
		while(next_permutation(arr,arr+Q));
		
		if (i!=c-1)
  		   cout << "Case #" << i+1 << ": " << mini << endl;
		else
  		   cout << "Case #" << i+1 << ": " << mini;

	}
	return 0;
}
