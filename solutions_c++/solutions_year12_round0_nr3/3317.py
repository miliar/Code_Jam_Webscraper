#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{

	ifstream in("C-small-attempt0.in");
	ofstream out("C-small-attempt0.out");
	int N;
	int A;
	int B;
	in>>N;
	vector<int> val;
	vector<int> tempval;
	string outval;
	int num = 0;
	int change = 0;
	int start = 1;
	while(N--)
	{
		num = 0;
		in>>A>>B;
		for(int a = A;a <= B;a++)
		{
			int temp = a;
			//cout<<a<<endl;
			val.clear();
			
			while(temp)
			{
				val.push_back(temp%10);
				temp /= 10;
			}
			for(int i = 0;i< val.size();i++)
			{
				tempval.clear();
				for(int j=i;j >= 0;j--)
					tempval.push_back(val[j]);
				for(int k = val.size() - 1;k > i;k--)
					tempval.push_back(val[k]);
			
				outval.clear();
				for(int i = 0;i< tempval.size();i++)
				{
					outval.push_back(char(tempval[i]+48));
				}
				int p = outval.length();
				change = 0;
				for(int i=0;i< outval.length();i++)
				{
					change += (outval[i] - 48) * pow(double(10),--p);
				}
			//	change = int(outval);
				if(change > a && change <=B && change >= A)
					++num;
			}
		}
		out<<"Case #"<<start<<": "<<num<<endl;
		++start;
	}

	return 0;
}