#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <vector>
#include <stack>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include <queue>
#include <map>
#include <numeric>
#include <fstream>
#include <bitset>

using namespace std;

class Test
{
public:
	static void test()
	{
		int L=3,D=5,N=4;
		vector<string> a;
		vector<string> b;
		
		bitset<5000> flag;		
		ifstream is("a.in");
		ofstream os("A-small-attempt0.out");
		string str;
		is>>L;
		is>>D;
		is>>N;
		while(true)
		{
			for(int i=0;i<D;++i)
			{
				is>>str;
				a.push_back(str);
			}
			for(int i=0;i<N;++i)
			{
				is>>str;
				b.push_back(str);
			}
			break;
		}

		
		for(int i=0;i<b.size();++i)
		{
			
			flag.reset();

			int j=0;
			int count=0;
			while(j<b[i].size())
			{
				if(b[i][j]=='(')
				{
					string::size_type stop=b[i].find(')',j);
					string tmp=b[i].substr(j+1,stop-j-1);
					j=stop+1;				
					for(int k=0;k<a.size();++k)
						if(tmp.find(a[k][count])==string::npos)
							flag[k]=1;							
					count++;
				}
				else 
				{	
					for(int k=0;k<a.size();++k)
						if(a[k][count]!=b[i][j])
							flag[k]=1;						
					++j;
					count++;
				}
			}			

			int num=0;
			for(int i=0;i<a.size();++i)
				if(flag[i]==0)
					num++;
			char output[32]={0};
			sprintf(output,"Case #%d: %d\n",i,num);
			os<<output;
		}
		
		
	}
};