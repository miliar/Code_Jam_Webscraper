# include <fstream>
# include <iostream>
# define MAX 300

using namespace std;

int main(int argc, char **argv)
{
	ifstream in("input.in");
	ofstream out("output.out");
	int totalCase;
	in >> totalCase;

	for(int totalNumber = 1; totalNumber <= totalCase; totalNumber++)
	{
		int count;
		in >> count;
		double wp[MAX]={0,}, owp[MAX]={0,}, oowp[MAX]={0,};
		int w[MAX][MAX];

		for(int i = 0; i < count; i++)
		{
			for(int j = 0; j < count; j++)
			{
				char ch;
				in >> ch;
				if(ch == '0')
				{
					w[i][j] = 0;
				}
				else if(ch == '1')
				{
					w[i][j] = 1;
				}
				else
				{
					w[i][j] = 2;
				}
			}
		}

		for(int i = 0; i < count; i++)
		{
			double a=0, b=0;
			for(int j = 0; j < count; j++)
			{
				if(w[i][j] == 1)
				{
					a++;
				}

				if(w[i][j] == 0)
				{
					b++;
				}
			}
			wp[i] = a / (a + b);
		}

		for(int i = 0; i < count; i++)
		{
			double a=0, b=0, c=0;
			for(int j = 0; j < count; j++)
			{
				if(w[i][j] != 2)
				{
					c++;
					a=0;
					b=0;
					for(int k = 0; k < count; k++)
					{
						if( k != i)
						{
							if(w[j][k] == 1){
								a++;
							}
							else if(w[j][k] == 0){
								b++;
							}
						}
					}
					owp[i] += a / (a + b);
				}
			}
			owp[i] = owp[i] / c;
		}

		for(int i = 0; i < count; i++)
		{
			double n=0, b=0;
			for(int j = 0; j < count; j++)
			{
				if(w[i][j] != 2)
				{
					n++;
					oowp[i] += owp[j];
				}
			}
			oowp[i] = oowp[i] / n;
		}

		out << "Case #" << totalNumber << ": " << endl;
		for(int i = 0; i < count; i++)
		{
			out << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
		}
	}
	return 0;
}