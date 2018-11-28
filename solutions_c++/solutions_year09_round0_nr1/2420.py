/*
 *  uni.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 08/07/17.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int L,D,N;
	
	cin>> L>>D>>N;
	
	vector<string> dict(D);
	
	for(int i=0; i<D; ++i)
		cin>>dict[i];
	
	for(int case_number=0; case_number<N; ++case_number)
	{
		vector<vector<char> > pattern(L);
		
		char c;
		
		int locus=0;
		
		while (locus < L) {
			
			cin >> c;
			
			//cout<<c<<endl;
			
			if(c=='(')
			{
				while (true) {
					
					cin >> c;
					
					
					//cout<<c<<endl;
					
					if(c!=')')
						pattern[locus].push_back(c);
					else {
						break;
					}

				}
			}
			else
				pattern[locus].push_back(c);
			
			++locus;
		}
		
		int count=0;
		
		for(int i=0; i<D; ++i)
		{
			//cout << dict[i]<<endl;
			
			bool matched = true;
			
			for(int j=0; j<L; ++j)
			{
				bool char_found = false;
				
				for(int k=0; k<pattern[j].size();++k)
				{
					if(dict[i][j] == pattern[j][k])
					{
						char_found = true; break;
					}
				}
				
				if(!char_found)
				{
					matched = false; break;
				}
			}
			
			if(matched)
				++count;
		}
		
		cout << "Case #"<<case_number+1<<": "<<count<<endl;
				
	}

}

