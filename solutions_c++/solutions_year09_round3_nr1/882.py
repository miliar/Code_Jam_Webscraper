#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	//	freopen("A.in","r",stdin);
	freopen("A-small-attempt1.in","r",stdin);freopen("x2.txt","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	string str;
	getline(cin, str);
	int i,j;
	
	for(i=0;i<T;i++)
	{
		map<char, int> mp;
		map<char, bool> mpt;
		bool fg[10];
		for(int i1=0; i1<10;i1++) fg[i1]=false;

		getline(cin,str);
		int j=0;
		int len = str.length();
		vector<int> res;
		mp[str[j]]=1;
		mpt[str[j]] = true;
		res.push_back(1);
		fg[1] = true;
		j++;
		for(;j<len;j++)
		{
			if( mpt[str[j]] )
			{
				res.push_back( mp[str[j]] );
			//	fg[mp[str[j]]] = true;
			}
			else
			{
				if( fg[0]==false )
				{				
					mp[ str[j] ] = 0;
					mpt[ str[j] ] = true;
					fg[0] = true;
					res.push_back(0);
				}
				else
				{
					int mx=*max_element(res.begin(), res.end());
					mp[str[j]] = mx+1;
					mpt[str[j]] = true;
					res.push_back(mx+1);
				}
			}

		}
	/*	for(int k=0;k<len;k++)
			cout<<res[k];
		cout<<endl;  */
		int base=*max_element(res.begin(),res.end());
		base++;
	//	cout<<"base:"<<base<<endl;
		unsigned long long bse = 1;
		unsigned long long sec = 0;
		for(int i2=res.size()-1; i2>=0; i2--)
		{
			sec+=bse*res[i2];
			bse= bse*((unsigned long long)base);
		}
		printf("Case #%d: %u\n", i+1, sec);
	} 
    
	
}