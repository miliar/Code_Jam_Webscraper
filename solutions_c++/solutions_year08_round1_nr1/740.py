#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <valarray>
#include <bitset>
#include <iostream>
#include <cctype>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()

int main()
{int n,i=1;
cin>>n;
while(n)
{	int num;
	cin>>num;
	vector <int> v1,v2;
	int num2=num;
	while(num)
	{int aux;
	cin>>aux;
		v1.push_back(aux);
	num--;
	}
	while(num2)
	{int aux2;
	cin>>aux2;
		v2.push_back(aux2);
	num2--;
	}
	sort(all(v1));
	sort(rall(v2));
	long long pro=0;
	for(int i=0;i<v1.size();i++)
	{
		pro+=(v1[i]*v2[i]);
	
	}
	cout<<"Case #"<<i<<": "<<pro<<endl;
	i++;


n--;
}


return 0;
}
