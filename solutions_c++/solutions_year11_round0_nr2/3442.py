#include<iostream>
#include<vector>
#include<map>
using namespace std;

int hash(char a)
{
	switch(a)
	{
		case 'Q' :
			return 0;
		case 'W' :
			return 1;
		case 'E' :
			return 2;
		case 'R' :
			return 3;
		case 'A' :
			return 4;
		case 'S' :
			return 5;
		case 'D' :
			return 6;
		case 'F' :
			return 7;
		default :
			return -1;
	}
}

void clearPresence(int *p)
{
	for(int i=0;i<8;i++)
		p[i] = 0;
}

int main()
{
	int T;
	int count = 0;

	cin>>T;
	while(T--)
	{
		count++;

		vector<char> combine[8];
		vector<char> result[8];
		vector<char> oppose[8];
		
		int c;
		string s;
		cin>>c;
		for(int i=0;i<c;i++)
		{
			cin>>s;
			combine[hash(s[0])].push_back(s[1]); //s[1] combines with s[0]
			result[hash(s[0])].push_back(s[2]);

			combine[hash(s[1])].push_back(s[0]);
			result[hash(s[1])].push_back(s[2]);
		}

		int d;
		cin>>d;
		for(int i=0;i<d;i++)
		{
			cin>>s;
			oppose[hash(s[0])].push_back(s[1]);
			oppose[hash(s[1])].push_back(s[0]);
		}

		int n;
		cin>>n;
		cin>>s;
		vector<char> final_string;
		int present[8];
		clearPresence(present);
		char last_char = s[0];
		int last_int = hash(s[0]);
		present[last_int]++;
		
		final_string.push_back(s[0]);
		for(int i=1;i<n;i++)
		{
//			cout<<"Current char = "<<s[i]<<endl;
			if(last_int >= 0)
			{
			 	int j;
				for(j=0;j<combine[last_int].size();j++)
				{
					if(s[i] == combine[last_int][j])
					{
//					cout<<"Combined"<<endl;
						present[last_int]--;
						final_string[final_string.size()-1] = result[last_int][j];
						break;
						
					}
				}
				if(j < combine[last_int].size())
				{
					last_int = -1;
					last_char = final_string[final_string.size()-1];
					continue;
				}
			}
			int j;
			int current_int = hash(s[i]);
			for(j=0;j<oppose[current_int].size();j++)
			{
				if(present[ hash(oppose[current_int][j]) ] != 0)
				{
//					cout<<"Cleared"<<endl;
					final_string.clear();
					last_int = -1;
					clearPresence(present);
					break;
				}
			}
			if( j < oppose[current_int].size())
			{
				continue;
			}
			final_string.push_back(s[i]);
			last_char = s[i];
			last_int = hash(s[i]);
			present[last_int]++;
		}

		cout<<"Case #"<<count<<": [";
		if(final_string.size() > 0)
		{
			cout<<final_string[0];
		}
		for(int i=1;i<final_string.size();i++)
		{
			cout<<", "<<final_string[i];
		}
		cout<<"]"<<endl;
		
	}
}
