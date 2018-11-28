#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

class BotTrust
{
public:
	int T;
	vector<vector<int>> buttons;
	vector<vector<int>> sides; //0 for Orange, 1 for Blue
	
	BotTrust(){}

	BotTrust(string name)
	{
		ifstream f(name.c_str());
		stringstream ss;
		string st;

		if (f.is_open())
		{
			getline(f, st);
			ss << st;
			ss >> T;
			buttons.resize(T);
			sides.resize(T);
			for (int i=0; i<T; ++i)
			{
				ss.clear();
				getline(f, st);
				ss << st;
				int n;
				ss >> n;
				buttons[i].resize(n);
				sides[i].resize(n);
				for (int j=0; j<n; ++j)
				{
					char c; 
					int b;
					ss >> c >> b;
					if (c=='O') sides[i][j] = 0;
					else if (c=='B') sides[i][j] = 1;
					else cout <<"Input Error OB"<<endl;
					buttons[i][j] = b;
				}
			}
		}
		//test io
		if (1)
		{
			cout <<"Test io "<<endl;
			cout <<T<<endl;
			for (int i=0; i<T; ++i)
			{
				int n = buttons[i].size();
				cout << n <<" ";
				for (int j=0; j<n; ++j)
				{
					if (sides[i][j]==0) cout <<"O ";
					else cout <<"B ";
					cout <<buttons[i][j]<<" ";
				}
				cout <<endl;
			}
		}
		cout <<"IO finish "<<endl;
	}

	int result(int k)
	{
		vector<int>& button = buttons[k];
		vector<int>& side = sides[k];
		//least time interval without waiting
		//of both sides
		int n = button.size();
		vector<int> bs[2];
		
		bs[0].reserve(n);
		bs[1].reserve(n);
		for (int i=0; i<n; ++i)
		{
			int b = button[i];
			bs[side[i]].push_back(b);
		}
		//interval between beginning and b1: b1
		//interval between b1 and b2: b2-b1+1 

		for (int j=0; j<2; ++j)
		{
			for (int i=bs[j].size()-1; i>0; --i)
			{
				//expected interval time
				bs[j][i] = abs(bs[j][i]-bs[j][i-1])+1;
			}
			//bs[j][0] is not changed
		}



		//running
		int current_time = 0;
		int expected_time[2]={0,0};
		if (!bs[0].empty())	expected_time[0] = bs[0][0];
		if (!bs[1].empty()) expected_time[1] = bs[1][0];
		//0 for o, 1 for b
		int id[2]={0,0};

		//for (int i=0; i<n; ++i)
		
		for (int i=0; i<n; ++i)
		{
			int s = side[i];
			current_time = max(current_time+1, expected_time[s]);

			id[s]++;
			if (id[s]<bs[s].size()) expected_time[s] = current_time+bs[s][id[s]];
			
			//update current time

		}
		return current_time;

	}

	void run()
	{
		for (int k=0; k<T; ++k)
		{
			cout <<"Case #"<<k<<": "<<result(k)<<endl;
		}
	}

	void run(string name)
	{
		ofstream f(name.c_str());
		if (f.is_open())
		{
			for (int k=0; k<T; ++k)
			{
				int res = result(k);
				f <<"Case #"<<k+1<<": "<<res<<endl; 
			}
			f.close();
		}
	}

};

int main(int argc, char** argv)
{
	cout <<"Hello World"<<endl;
	if (argc<3)
		cout <<"Command: bottrust [input_filename] [output_filename]"<<endl;
	else
	{
		BotTrust bot(argv[1]);
		bot.run(argv[2]);
	}
}