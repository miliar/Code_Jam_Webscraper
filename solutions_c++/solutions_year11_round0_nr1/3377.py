#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<utility>

using namespace std;

int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	int nTest;
	cin>>nTest;
	for(int test = 1; test<= nTest;test++)
	{
		int nInput;
		cin>>nInput;
		vector<int> Orange,Blue;
		vector<pair<char,int> > input;
		for(int i=0;i<nInput;i++)
		{
			char robot;
			int button;
			cin>>robot>>button;
			if(robot == 'O')
				Orange.push_back(button);
			else
				Blue.push_back(button);
			pair<char,int> item;
			item.first = robot; item.second = button;
			input.push_back(item);
		}
		int Otime(0),Opos(1),Btime(0),Bpos(1);
		int result(0),time;
		for(int i=0;i<nInput;i++)
		{
			if(input[i].first =='O')
			{
				if(Btime > abs(Opos - input[i].second))//already stay
					time = 1;
				else//have to move
					time = abs(Opos - input[i].second) - Btime +1;
				Btime = 0;
				Otime += time;
				result += time;
				Opos = input[i].second;
			}
			else
			{
				if(Otime > abs(Bpos - input[i].second))//already stay
					time = 1;
				else//have to move
					time = abs(Bpos - input[i].second) - Otime +1;
				Otime = 0;
				Btime += time;
				result += time;
				Bpos = input[i].second;
			}
			//cout<<"Case @"<<test<<": "<<result<<endl;
		}
		cout<<"Case #"<<test<<": "<<result<<endl;
	}
	return 0;
}