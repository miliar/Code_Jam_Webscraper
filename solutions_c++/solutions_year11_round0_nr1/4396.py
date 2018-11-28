#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

//vector < pair<char,int> > box;
queue < string > Orange;
queue < string > Blue;
queue < string > Order;

void go( string cha, int head, int tail )
{
	string tmp = "";
	if(head < tail)
	{
		if(cha == "O"){
			for(int i=head+1; i<=tail; i++){
				tmp = "move";
//				tmp += i+'0';
				Orange.push(tmp);
			}
			tmp = "push";
//			tmp += tail+'0';
			Orange.push(tmp);
		}
		else{
			for(int i=head+1; i<=tail; i++){
				tmp = "move";
//				tmp += i+'0';
				Blue.push(tmp);
			}
			tmp = "push";
//			tmp += tail+'0';
			Blue.push(tmp);
		}
	}
	else
	{
		if(cha == "O"){
			for(int i=head-1; i>=tail; i--){
				tmp = "move";
//				tmp += i+'0';
				Orange.push(tmp);
			}
			tmp = "push";
//			tmp += tail+'0';
			Orange.push(tmp);
		}
		else{
			for(int i=head-1; i>=tail; i--){
				tmp = "move";
//				tmp += i+'0';
				Blue.push(tmp);
			}
			tmp = "push";
//			tmp += tail+'0';
			Blue.push(tmp);
		}
	}
}

void output()
{
	long long time = 0;
	while( !Order.empty() )
	{
		string Now = Order.front(); Order.pop();
		
		string stnd;
		if(Now == "O"){
			while(true)
			{
				stnd = Orange.front(); Orange.pop();
				
				time++;

				if( !Blue.empty() && Blue.front() == "move") Blue.pop();
				if( stnd.substr(0, 4) == "push" ) break;
			}
		}

		else{
			while(true){
				stnd = Blue.front(); Blue.pop();
				
				time++;

				if( !Orange.empty() && Orange.front().substr(0, 4) == "move") Orange.pop();
				if(stnd.substr(0, 4) == "push") break;
			}
		}
	}
	cout << time << endl;
}

int main()
{
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	int tc;
	cin >> tc;
	for(int i=1; i<=tc; i++)
	{
		cout << "Case #" << i << ": ";
		int N;
		cin >> N;

		int Ohead, Bhead;
		Ohead = Bhead = 1;
		for(int i=0; i<N; i++)
		{
			string tmp; int point;
			cin >> tmp >> point;
			Order.push( tmp );
			
			if(tmp == "O"){
				go( tmp, Ohead, point );
				Ohead = point;
			}
			else{
				go( tmp, Bhead, point );
				Bhead = point;
			}
		}
		
		output();
	}
	return 0;
}