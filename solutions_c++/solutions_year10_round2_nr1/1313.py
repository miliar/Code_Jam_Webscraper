#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
using namespace std;

int main()
	{
		int T,N,M_1,x=1;
		for(cin>>T;T>0;T--)
		{
			cin>>N>>M_1;
			map<string,int> M;
			for(int i=0;i<N;i++)
			{
				string s;
				cin>>s;
				for(int j=0;j<s.size();j++) if(s[j]=='/') s[j]=' ';
				stringstream ss(s);
				string tmp,ret="";
				while(ss>>tmp)
				{
					ret+=tmp;
					M[ret]=1;
				}
			}	
			int r=0;;
			for(int i=0;i<M_1;i++)
				{
					string s;
					cin>>s;
					for(int j=0;j<s.size();j++) if(s[j]=='/')s[j]=' ';
					stringstream ss(s);
					string tmp,ret="";
					int cnt=0;
					while(ss>>tmp)
					{
						ret+=tmp;
						if(M.find(ret)==M.end())cnt++;
						M[ret]=1;
						//cout<<ret<<" "<<cnt<<endl;
					}
					r+=cnt;
				}	

				cout<<"Case #"<<x++<<": "<<r<<endl;		
			
		}				
	}
