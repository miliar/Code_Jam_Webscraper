#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

int process(string &s)
{
	stringstream ss(s);
	int num_G, num_S, p, tmp, tmp2, tmp3;
	vector<int> scores;

	ss >> num_G >>num_S >> p;
	for(int i = 0; i < num_G; i++)
	{
		ss>>tmp;
		scores.push_back(tmp);
	}

	int numOver=0;

	for(int i = 0; i < num_G; i++)
	{
		tmp = scores[i]/3;
		tmp2 = scores[i]%3;

		if(tmp2 == 2)
		{
			if(i==num_G-1 && num_S >0)
			{
				tmp2 = tmp; tmp3 = tmp+2;
				num_S--;
			}
			else if(tmp+2 < p || tmp >= p || num_S <=0)
			{
				tmp3=tmp2=tmp+1;
			}
			else
			{
				tmp2 = tmp; tmp3 = tmp+2;
				num_S--;
			}
		}

		else if(tmp2==1)
		{
			tmp2=tmp; tmp3=tmp+1;
		}

		else
		{
			if(scores[i]==0) tmp3=tmp=tmp2;
			else if(i==num_G-1 && num_S >0)
			{
				tmp--;
				tmp2=tmp+1;
				tmp3=tmp+2;
				num_S--;
			}
			else if(num_S<=0 || tmp>=p || tmp+1 < p)
				tmp3=tmp2=tmp;
			else
			{
				tmp--;
				tmp2=tmp+1;
				tmp3=tmp+2;
				num_S--;
			}
		}
		cout<<tmp<<' '<<tmp2<<' '<<tmp3<<endl;
		if(tmp2>=p || tmp2>=p ||tmp3>=p) numOver++;
	}
cout<<"end result:"<<numOver<<endl<<endl;
	return numOver;
}

int main()
{
	ifstream input("input.in");
	ofstream output("output.out");

	int input_number=0;

	input>>input_number;

	string s;
	getline(input,s);
	for(int i = 1; i <= input_number; i++)
	{
		if(input.good())
		{
			getline(input, s);
			output<<"Case #"<<i<<": ";
			output<<process(s)<<endl;
		}
	}

	input.close();
	output.close();

	return 0;
}
