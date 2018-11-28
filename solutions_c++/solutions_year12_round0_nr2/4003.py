#include <iostream>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("Blarge-out.in");
	int T, N, S, p, num=0;

	infile >> T;
	for(int i=0;i<T;i++)
	{
		num = 0;
		infile >> N >> S >> p;
		for(int j=0;j<N;j++)
		{
			int ggler, ave, rem;
			infile >> ggler;
			ave = ggler/3;
			rem = ggler%3;
			if(ave >= p)
			{
				//if average score already > p, this ggler is qualified and no adjustment needed
				num++;
			}
			else if((ave+1)>=p) //possible to qualify
			{
				if(rem==1 || rem==2)
					num++;
				else if(rem==0)
					if(S>0 && ave!=0) //cannot do adjustment score=0 or no more surprise triplet
					{
						num++;
						S--;
					}
			}
			else if((ave+2)==p)
			{
				if((S>0)&&(rem==2))
				{
					num++;
					S--;
				}
			}
		}
		outfile << "Case #" << (i+1) << ": " << num << endl;
	}


	outfile.close();
	infile.close();

	return 0;
}
