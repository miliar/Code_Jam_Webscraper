#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define f(i,n) for((i)=0;(i)<(int)(n);(i)++)


int main()
{
	int T;
	cin>>T;
	int N,M;
	set<string> exist;
		
	int it;
	f(it,T)
	{
		int ans=0;
		exist.clear();
		
		cin>>N>>M;
		for(int in=0;in<N;in++)
		{
			string s;
			cin>>s;
			
			int found=s.find("/");
			while(found<s.size())
			{
				//add all in s
				//cout<<found<<" "<<s.substr(0,found);
				exist.insert(s.substr(0,found));
				found=s.find("/",found+1,1);				
			}
			exist.insert(s);
		}
		exist.insert("/");
		exist.insert("");
//		cout<<"print"<<endl;
//		for(set<string>::iterator it1=exist.begin();it1!=exist.end();it1++)
//		{
//			cout<<*it1<<endl;
//		}
		for(int im=0;im<M;im++)
		{
			string s;
			cin>>s;
			if(exist.find(s)==exist.end())
			{
				int found=s.find("/");
				while(found<s.size())
				{
					//add all in s
					//cout<<found<<" "<<s.substr(0,found);
					if( (exist.insert(s.substr(0,found))).second == true){
					 	ans++;
					 }
					found=s.find("/",found+1,1);	
				}
				if( (exist.insert(s)).second == true) ans++;			
			}
		}
		
		
		cout<<"Case #"<<it+1<<": "<<ans<<endl;
	}
	
	return 0;
}
