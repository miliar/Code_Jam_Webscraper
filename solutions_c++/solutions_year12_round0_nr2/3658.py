#include<iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>

using namespace std;

const char in_name[]="B-large(1).in";
const char out_name[]="out.txt";

ifstream c_in(in_name);
ofstream c_out(out_name);

class Solver
{
	private:
		vector<int> score;
		int n;
		int surp;
		int p;
		int sum;
	public:
		void InputData()
		{
			c_in>>n>>surp>>p;
			score.resize(n);
			for(int i=0;i<n;i++)
				c_in>>score[i];
		}

		void Work()
		{
			sum=0;
			for(int i=0;i<n;i++)
			{
				switch(score[i]%3)
				{
					case 0:
						if(score[i]/3>=p)
							sum++;
						else if(surp>0 && score[i]/3+1>=p && (score[i]/3>0))
						{
							sum++;
							surp--;
						}
						break;
					case 1:
						if(score[i]/3+1>=p)
							sum++;
						else if(surp>0 && score[i]/3+1>=p && (score[i]/3>0))
						{
							sum++;
							surp--;
						}
						break;
					case 2:
						if(score[i]/3+1>=p)
							sum++;
						else if(surp>0 && score[i]/3+2>=p)
						{
							sum++;
							surp--;
						}
						break;
				}
			}
		}

		void OutputData()
		{
			c_out<<sum<<endl;
		}
	private:
};

int main()
{
	

	int T;
	c_in>>T;
	for(int i=0;i<T;i++)
	{
		Solver X;
		X.InputData();
		X.Work();
		c_out<<"Case #"<<i+1<<": ";
		X.OutputData();
	}

	c_in.close();
	c_out.close();
	return 0;
}