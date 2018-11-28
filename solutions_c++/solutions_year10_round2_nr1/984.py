/*
 *  q_1.cpp
 *  
 *  Created by Jack Cohen on 22/05/
*/

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{	
	int T;
	cin >> T;
	
	//cases
	for (int k=1; k<=T; k++)
	{
		vector<string> existing_paths;
		
		int makes = 0;
		
		int N; //existing 
		int M; //to be made
		
		cin >> N;
		cin >> M;
		string dead;
		getline(cin,dead);
		// read in existing; store into structure;
		//cout << "exisitng"<< endl;
		for (int n=0; n<N; n++)
		{
			string e_path;
			getline(cin, e_path);
			
			string token;
			istringstream iss(e_path);
			//cout << "token" << endl;
			// separate paths
			string build;			
			while ( getline(iss, token, '/') )
			{
				if (token=="")
					continue;
				build+="/"+token;
				//cout << "adding: " << build << endl;
				existing_paths.push_back(build);
			}
			
			//cout << e_path << endl;
		}
		//cout << "to make" << endl;
		// folders to make
		for (int m=0; m<M; m++)
		{
			string m_path;
			getline(cin, m_path);
			
			// split into paths and see if each exists;
			// if not add
			string token;
			istringstream iss(m_path);
			string build;
			
			vector<string>::iterator p;
			
			while ( getline(iss, token, '/') )
			{
				if (token=="")
					continue;
				build+="/"+token;
				p = find(existing_paths.begin(), existing_paths.end(), build);				
				// if not found
				if (p == existing_paths.end())    
				{
					makes++;
					//cout << "adding: " << build << endl;
					existing_paths.push_back(build);
				}										
			}
			
			//cout << m_path << endl;
		}
		
		cout << "Case #" << k << ": " << makes << endl;
	}
	
	return 0;
}
