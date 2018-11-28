#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <queue>
using namespace std;
int main (int argc , char *argv[])
{
   	
short int T;	
cin >> T;
		
//Clear Buffer
char test;cin.get(test);
for (int i =0;i < T ;i++)
{
	string str;
	std::getline(cin,str);
			
	//Break into tokens
	char * cstr = new char[str.size()+1];
	strcpy(cstr,str.c_str());
	char * p = strtok(cstr," ");
	int R = atoi(p);
	p=strtok(NULL," ");
	int k = atoi(p);
	p=strtok(NULL," ");
	int N = atoi(p);
	
	//Read the group size
	str.clear();	
	std::getline(cin,str);
	//cout<< str<<endl;
	queue<int> roller_queue;
	
	//Break into tokens
	cstr = new char[str.size()+1];
	strcpy(cstr,str.c_str());
	p = strtok(cstr," ");
	while(p!=NULL)
	{
		roller_queue.push(atoi(p));
		p=strtok(NULL," ");
		//cout << "Item "<<endl;
	}
		
	//cout << R << k << N<<endl;	
	unsigned int total_people = 0;//for every round
	unsigned int money = 0;
	for ( int j=1;j<=R ;j++) //Rounds
	{
		queue<int> temp_queue;
		//cout<<"Round"<<j<<endl;
		total_people = 0;//for every round
		///Either roller limit exhauts or people exhauts
		while(!roller_queue.empty())
		{
			int group_size = roller_queue.front();
			if(total_people+group_size>k)break;
			total_people += group_size ;
			roller_queue.pop();
			temp_queue.push(group_size);
			//cout<< group_size<<total_people<<endl;		
		}
		//Reinit the queue
		if(roller_queue.empty())
			roller_queue = temp_queue;
		else
		{
			while(!temp_queue.empty())
			{
				roller_queue.push(temp_queue.front());
				temp_queue.pop();	
			}
		}	
		
			
		money+=total_people;
	}
	cout<< "Case #"<<i+1<<": "<<money<<endl;
}//Test Cases
}
