#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <math.h>

using namespace std;





int main()
{
	int L, D, N;
	cin >> L >> D >> N;
		
	vector<string> words; 
	for(int i = 0; i< D ; i++)
	{
		string d;
		cin >> d;
		words.push_back(d);
	
	}

	//char line[333];
	//cin.getline(line,333);
	
	bool paren = 0;
	string pool;
	
	
	for(int i = 0; i < N ; i++)
	{
		//cin.getline(line,333);
		vector<string> pat;
		string pattern;
		cin >> pattern;
		//cout << pattern << endl;
		//parse
		//string::iterator sit;
		//for(sit = pattern.begin() ; sit < pattern.end(); sit++)
		for(int j = 0; j < pattern.length() ; j++)
		{
			if( pattern[j] == '(' )
			{
				pool = "";
				paren = 1;
			}
			else if( pattern[j] == ')' )
			{
				pat.push_back(pool);
				paren = 0;
			}
			else if( paren == 1)
			{
				pool.push_back(pattern[j]);
			
			}
			else
			{
				pool = "";
				pool.push_back(pattern[j]);
				pat.push_back(pool);			
			}
		
		
		}
		
		//for(int j = 0 ; j < pat.size() ; j++)
		//	cout << pat[j] << endl;
		
	
		
		int found = 0;
		
		for(int j = 0; j < D ; j++)
		{
			string cword = words[j];
			//
			bool fail = 0;
			size_t ind;
			//cout << cword << endl;
			for(int k = 0; k < cword.size() ; k++)
			{
				//cout << "is " << cword[k] << " in " << pat[k] << endl;
				//cout << pat[k].find(cword[k]) << endl;
				ind = pat[k].find(cword[k]);
				if(  ind == -1 )
				{	
					//cout << "no\n";
					fail = 1;
					break;
		
				}
			}
			if(!fail)
				found++;
			
			
		}
		
		
		cout << "Case #" << i+1 << ": " << found << endl;
	}
	
	
	
	
	
	return 0;
	
	
}
