#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T,N,i,p,pos_o,pos_b,flag_o,flag_b,j,counts,temp,a;
	char q;
	vector<int> num,o,b;
	vector<char> type;
	
	fin>>T;
	temp = T;
	while(T--)
	{
		num.clear();
		o.clear();
		b.clear();
		type.clear();
		fin>>N;
		for(i=0;i<N;i++)
		{
			fin>>q;
			type.push_back(q);
			fin>>p;
			num.push_back(p);
			if(q=='O')
				o.push_back(p);
			else
				b.push_back(p);
		}
		num.resize(101);
		o.resize(101);
		b.resize(101);
		type.resize(101);
		pos_o = 1;
		pos_b = 1;
		flag_o = 0;
		flag_b = 0;
		j=0;
		counts = 0;
		while(N)
		{
			a = N;
			if(pos_o<o[flag_o])
				pos_o++;
			else if(pos_o>o[flag_o])
				pos_o--;
			else if(pos_o==o[flag_o]&&type[j]=='O'&&num[j]==o[flag_o])
			{
				flag_o++;
				N--;
			}
			if(pos_b<b[flag_b])
				pos_b++;
			else if(pos_b>b[flag_b])
				pos_b--;
			else if(pos_b==b[flag_b]&&type[j]=='B'&&num[j]==b[flag_b])
			{
				flag_b++;
				N--;
			}
			if(a!=N)
				j++;
			counts++;
		}

		cout<<"Case #"<<temp-T<<": "<<counts<<endl;
		fout<<"Case #"<<temp-T<<": "<<counts<<endl;
	}


	return 0;
}

