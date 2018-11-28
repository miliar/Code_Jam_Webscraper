#include <stdio.h>
#include <fstream.h>

double test[101][101];
double rresult[101];
double wp[101];
double owp[101];
double oowp[101];
int winn[101];
int tot[101];

double WP(int i,int n)
{
	double result;

	double total = 0;
	double win = 0;

	for(int j=1;j<=n;j++)
	{
		if(test[i][j] == 1)
		{
			win++;
			total++;
		}
		else if(test[i][j] == 0)
			total++;
	}

	winn[i] = (int)win;
	tot[i] = (int)total;
	result = win / total;

	return result;
}

double OWP(int i,int n)
{
	double result = 0;
	int num = 0;

	for(int j=1;j<=n;j++)
	{
		if(test[i][j] != -1)
		{
			int total = tot[j];
			int wi = winn[j];
			if(test[j][i] == 0)
			{
				total--;
			}
			else
			{
				total--;
				wi--;
			}

			result += (double)wi/total;
			num++;
		}
	}

	result = result / num;

	return result;
}

double OOWP(int i,int n)
{
	double result = 0;
	int num = 0;

	for(int j=1;j<=n;j++)
	{
		if(test[i][j] != -1)
		{
			result += owp[j];
			num++;
		}
	}

	result = result / num;

	return result;
}

void main()
{
	ifstream in;
	ofstream out;

	in.open("D:\\input.in",ios::in,0);
	out.open("D:\\out.out",ios::out,0);

	int total;
	int index = 1;


	int num = 0;

	in>>total;

	while(total > 0)
	{
		total--;
		char c;
		in>>num;
		for(int i=1;i<=num;i++)
		{
			for(int j=1;j<=num;j++)
			{
				in>>c;
				if(c == '.')
					test[i][j] = -1;
				else
					test[i][j] = c-'0';
			}
		}

		for(i=1;i<=num;i++)
		{
			wp[i] = WP(i,num);
		}

		for(i=1;i<=num;i++)
		{
			owp[i] = OWP(i,num);
		}

		for(i=1;i<=num;i++)
		{
			oowp[i] = OOWP(i,num);
		}
		double o = 0.25;
		double p = 0.5;

		for(i=1;i<=num;i++)
		{
			rresult[i] = (double)(o * wp[i] + p * owp[i] + o * oowp[i]);
		}

		out<<"Case #"<<index<<":"<<endl;
		for(i=1;i<=num;i++)
		{
			out<<rresult[i]<<endl;
		}

		index++;
	}

	in.close();
	out.close();
}