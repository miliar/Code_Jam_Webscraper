//============================================================================
// Name        : CodeJam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void print(vector<string> &in)
{
	for(int i=0;i<in.size();++i)
	{
		cout<<in[i]<<endl;
	}
}

class TicToe
{
public:
	void solve()
	{
		ifstream infile("input");
		ofstream outfile("output");
		if(!infile.is_open())
			cout<<"error while opening";

		int T;
		infile>>T;
		for(int i=0; i<T; ++i)
		{
			vector<string> in;
			for(int j=0; j<4; ++j)
			{
				string line;
				infile>>line;
				in.push_back(line);
			}

			string res=calc(in);

			outfile<<"Case #"<<(i+1)<<": "<<res<<endl;
		}

		infile.close();
		outfile.close();
	}
private:
	string calc(vector<string> in)
	{
		bool fin=true;

		//print(in);
		//cout<<"next:";

		//if finished
		string dot(".");
		for(int i=0; i<4; ++i)
		{
			for(int j=0; j<in[i].size();++j)
			{
				if (in[i][j]=='.')
				{
					fin=false;
					break;
				}
			}
			if(!fin)
				break;
		}

		//check possible win situation
		//row
		for(int i=0; i<4; ++i)
		{
			int Oc=0;
			int Xc=0;
			int Tc=0;
			for(int j=0; j<4; ++j)
			{
				if(in[i][j]=='X')
					Xc++;
				else if(in[i][j]=='O')
					Oc++;
				else if(in[i][j]=='T')
					Tc++;
			}
			if(Xc==4 || (Xc==3 && Tc==1))
				return "X won";

			if(Oc==4 || (Oc==3 && Tc==1))
				return "O won";
		}

		//col
		for(int i=0; i<4; ++i)
		{
			int Oc=0;
			int Xc=0;
			int Tc=0;
			for(int j=0; j<4; ++j)
			{
				if(in[j][i]=='X')
					Xc++;
				else if(in[j][i]=='O')
					Oc++;
				else if(in[j][i]=='T')
					Tc++;
			}
			if(Xc==4 || (Xc==3 && Tc==1))
				return "X won";

			if(Oc==4 || (Oc==3 && Tc==1))
				return "O won";
		}

		//diagonal
		{
			int Oc=0;
			int Xc=0;
			int Tc=0;
			for(int j=0; j<4; ++j)
			{
				if(in[j][j]=='X')
					Xc++;
				else if(in[j][j]=='O')
					Oc++;
				else if(in[j][j]=='T')
					Tc++;
			}
			if(Xc==4 || (Xc==3 && Tc==1))
				return "X won";

			if(Oc==4 || (Oc==3 && Tc==1))
				return "O won";
		}
		//secon diagonal
		{
			int Oc=0;
			int Xc=0;
			int Tc=0;
			for(int j=0; j<4; ++j)
			{
				if(in[j][3-j]=='X')
					Xc++;
				else if(in[j][3-j]=='O')
					Oc++;
				else if(in[j][3-j]=='T')
					Tc++;
			}
			if(Xc==4 || (Xc==3 && Tc==1))
				return "X won";

			if(Oc==4 || (Oc==3 && Tc==1))
				return "O won";
		}

		if(fin)
			return "Draw";

		return "Game has not completed";
	}

};

int main() {
	TicToe tt;
	tt.solve();
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
