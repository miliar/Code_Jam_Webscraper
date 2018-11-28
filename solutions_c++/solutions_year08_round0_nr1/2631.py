/*
 *  uni.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 08/07/17.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 */

#include <set>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int N;
	cin>>N;
	
		
	for(int i=0; i<N; ++i)
	{
		int S;
		cin>>S;
		
		cin.ignore(256,'\n');
		
		set <string> engines;
		char name[101];
		
		for(int j=0; j<S; ++j)
		{
			cin.getline(name,101);
			
			engines.insert(string(name));
		}
	
		int Q;
		cin>>Q;
		
		set <string> e;
		string curr;
		
		int ans=0;
		int j;
		
		cin.ignore(256,'\n');
		
		for(j=0; j<Q; ++j)
		{
			cin.getline(name,101);
			string str(name);
			
			e.insert(str);
			//cout<<name<<' '<<e.size()<<endl;
			
			if(e.size() == S)
			{
				curr = str;
				++ans;
				e.clear();
				
				break;
			}
		}
		
		int S_1 = S-1;
		
		for(++j; j<Q; ++j)
		{
			cin.getline(name,101);
			string str(name);
			
			if(str != curr)
			{
				e.insert(str);
				//cout<<name<<' '<<e.size()<<endl;
			
				
				if(e.size() == S_1)
				{
					curr = str;
					++ans;
					e.clear();
				}
			}
		}
		
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		
	}
	
}

