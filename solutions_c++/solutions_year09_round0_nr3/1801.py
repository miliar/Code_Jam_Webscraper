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
#define MAX 501

using namespace std;
stringstream stream;




int main()
{
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);

	int Case=0;
	int i=0,j=0,k=0;
	int N=0;
	string s;

	getline(cin,s);
	stream<<s;
	stream>>N;
	cout<<setfill('0');
	while(Case<N)
	{
		string target="welcome to code jam";
		string query="";
		getline(cin,s);
		
		for(i=0;i<s.size();i++)
		{
			for(j=0;j<target.size();j++)
			{
				if(s[i]==target[j])
					break;
			}
			if(j!=target.size())
			{
				query=query+s.substr(i,1);
			}
			
		}

		int res[MAX][20];
		int length=query.size();
			

		for(i=0;i<MAX;i++)
			for(j=0;j<20;j++)
				res[i][j]=0;
		if(query[0]==target[0])
			res[0][0]=1;
		for(i=1;i<length;i++)
		{	
			res[i][0]=res[i-1][0];
			if(query[i]==target[0])
				res[i][0]+=1;
						
		}
		
		for(i=1;i<length;i++)
		{
			for(j=1;j<19;j++)
			{
				res[i][j]=res[i-1][j];
				if(query[i]==target[j])
				{
					res[i][j]=(res[i-1][j-1]+res[i][j])%100000;
				}
			}
		}


		Case++;
		cout<<"Case #"<<Case<<": ";
		if(length>0)
		{
			res[length-1][18]=res[length-1][18]%10000;
			cout<<setw(4)<<res[length-1][18]<<endl;
	
		}
		else 
			cout<<setw(4)<<0<<endl;
	}
	return 0;
}