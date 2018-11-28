//////////////////////////////////////////////////////////////////////////
// Correct for small and large testsets
//////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
using namespace std;


int main()
{
	ifstream cin("A-small-attempt2.in");//("test.txt");//("A-small-attempt0.in");
	ofstream out("output.txt");

	string msg;
	int T;
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		vector<char> ch;
		vector<int> chidx;
		cin>>msg;
		int idx = 0;
		bool flag = true;
		for(int j=0; j<msg.length()-1; j++)
		{
			if(msg[j]!=msg[j+1])
				flag = false;
		}
		if(flag)	//all same
		{
			idx = 2;
			for(int j=0; j<msg.length(); j++)
				chidx.push_back(1);
		}
		else
		{
			for(int j=0; j<msg.length(); j++)
			{
				if(find(ch.begin(), ch.end(), msg[j])==ch.end())	//not found
				{
					if(idx==0)
						chidx.push_back(1);
					else if(idx==1)
						chidx.push_back(0);
					else
						chidx.push_back(idx);

					idx++;
					ch.push_back(msg[j]);
				}
				else
				{
					for(int k=0; k<ch.size(); k++)
					{
						if(ch[k]==msg[j])
						{
							if(k==0)
								chidx.push_back(1);
							else if(k==1)
								chidx.push_back(0);
							else
								chidx.push_back(k);
							break;
						}
					}
				}
			}
		}
		
		//compute result number
		double sum = 0;
		double temp = 1;
		reverse(chidx.begin(), chidx.end());
		for(int j=0; j<chidx.size(); j++)
		{
			sum += chidx[j]*temp;
			temp*=idx;
		}

		out<<"Case #"<<i<<": "<<(int)sum<<endl;
	}

	//getchar();
	return 0;
}