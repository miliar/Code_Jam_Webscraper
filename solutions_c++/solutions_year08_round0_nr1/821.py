#include<iostream>
#include<map>
#include<string>
#include<algorithm>
#include<cstdlib>
using namespace std;
int main()
{
	int num_cases=0,num_keys=0,num_strings=0;
	string word;
	cin>>num_cases;
	for(int i=0;i<num_cases;i++)
	{
		cin>>num_keys;
		getline(cin,word,'\n');
		map<string,bool> dictionary;
		int count=0,num_switches=0;
		for(int j=0;j<num_keys;j++)
		{
			getline(cin,word,'\n');
			dictionary[word]=false;
		}
		cin>>num_strings;
		getline(cin,word,'\n');

		for(int j=0;j<num_strings;j++)
		{
			getline(cin,word,'\n');
			if(!dictionary[word])
			{
				dictionary[word]=true;
				count++;
				if(count==num_keys)
				{
					num_switches++;
					map<string,bool>::iterator p;
					for(p=dictionary.begin();p!=dictionary.end();p++)
					{
						dictionary[p->first]=false;
					}
					dictionary[word]=true;
					count=1;			
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<num_switches<<'\n';	
	}
	return(0);
}				
				

			
