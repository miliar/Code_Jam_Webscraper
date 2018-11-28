#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");

	int N;
	in>>N;
	int T,S,P;
	vector<vector<int> > val;
	vector<int> tempval;
	int temp;
	int div = 0;
	int mod = 0;
	int big = 0;
	int small = 0;
	int start = 1;
	while(N--)
	{
		in>>T>>S>>P;
		val.clear();
		while(T--)
		{
			in>>temp;
			div = temp/3;
			mod = temp%3;
			tempval.clear();
			switch(mod)
			{
			case 0:
				tempval.push_back(0);
				tempval.push_back(div);
				tempval.push_back(div);
				tempval.push_back(div);
				break;
			case 1:
				tempval.push_back(1);
				tempval.push_back(div);
				tempval.push_back(div);
				tempval.push_back(div+1);
				break;
			case 2:
				tempval.push_back(2);
				tempval.push_back(div);
				tempval.push_back(div+1);
				tempval.push_back(div+1);
				break;
			}
			val.push_back(tempval);
		
		}
		big = 0;
		small = 0;
		for(int i=0;i< val.size();i++)
		{
			if(val[i][3] >= P)
			{
				++ big;
				continue;
			}
			if(val[i][0] == 0 && val[i][1] > 0)
			{
				if( val[i][3] == P-1)
					++small;
		
			}
			else if(val[i][0] == 2)
			{
				if( val[i][3] == P-1)
					++small;				
			}

		}
		if(small > S)
			big += S;
		else 
			big += small;
		out<<"Case #"<<start<<": "<<big<<endl;
		++start;
	}
	return 0;
}