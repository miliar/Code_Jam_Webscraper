/*
 *  quick.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 07/02/15.
 *  Copyright 2007 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
//#include <cmath>
using namespace std;

#include <set>
#include <vector>
#include <map>
#include <algorithm>

#include <iterator>

int main()
{
	int T, C, D, N;
	
	cin>>T;
	
	for(int i=0; i<T; ++i)
	{
		vector<set<int> > opposite_list(26);
		vector<map<int, int> > combo_list(26);
		
		//cout<<"here?"<<endl;
		
		
		cin>>C;
		
		for (int j=0; j<C; ++j) {
			
			char base1, base2, result;
			
			cin>>base1>>base2>>result;
			
			//cout<<"here?"<<endl;
			
			combo_list[base1 - 'A'][base2 - 'A'] = (result - 'A');
			combo_list[base2 - 'A'][base1 - 'A'] = (result - 'A');
			
		}
		
		cin>>D;
		
		for (int j=0; j<D; ++j) {
			
			//cout<<j<<endl;
			//cout<<"here?"<<endl;
			
			
			char base1, base2;
			
			cin>>base1>>base2;
			
			opposite_list[base1 - 'A'].insert(base2 - 'A');
			opposite_list[base2 - 'A'].insert(base1 - 'A');
			
		}
		
		cin>>N;
		
		vector<int> result;
		multiset<int> bomb_list;
		
		map<int,int>::iterator it;
		
		char temp;
		/*
		for (int k=0; k<26; ++k) {
			copy(opposite_list[k].begin(), opposite_list[k].end(), ostream_iterator<int>(cout, " ")); cout<<endl;
		}
		*/
		for (int j=0; j<N; ++j) {
			
			cin>>temp;
			
			int ele = temp - 'A';
			
			/*
			for (int j=0; j<result.size(); ++j) {
				cout<<char('A'+ result[j])<<", ";
			}		
			cout<<endl;
			
			cout<<"add "<<temp<<endl;
			*/
			
			if(result.empty())
			{
				result.push_back(ele);//if(!opposite_list[ele].empty())
				bomb_list.insert(opposite_list[ele].begin(), opposite_list[ele].end());
			}
			else
			{
				int last = result.back();
				
				it = combo_list[last].find(ele);
				
				if(it != combo_list[last].end())
				{
					//last combines with ele to make (*it).second
					result.pop_back();
					
					
					multiset<int> temp;
					set_difference(bomb_list.begin(),bomb_list.end(),opposite_list[last].begin(),opposite_list[last].end(),inserter(temp,temp.end()));
					bomb_list = temp;
					//bomb_list.erase(opposite_list[last].begin(), opposite_list[last].end());
					
					result.push_back((*it).second);
				}
				else if(bomb_list.count(ele))
				{
					result.clear();
					bomb_list.clear();
				}
				else
				{
					result.push_back(ele);//if(!opposite_list[ele].empty()) 
					
					//cout<<"here..."<<endl;
					
					bomb_list.insert(opposite_list[ele].begin(), opposite_list[ele].end());
					
					//cout<<"not here..."<<endl;
				}
				
			}
			
		}
		
		cout<<"Case #"<<i+1<<": [";
		
		//cout<<result.size();
		
		if(!result.empty())
		{
			for (int j=0; j<(result.size() - 1); ++j) {
				cout<<char('A'+ result[j])<<", ";
			}
			
			cout<<char('A'+ result.back());
		}
		
		cout<<']'<<endl;
		
		//result.clear();
		//bomb_list.clear();
		//cout<<"here?"<<endl;
		
	}
	
	return 0;
}
