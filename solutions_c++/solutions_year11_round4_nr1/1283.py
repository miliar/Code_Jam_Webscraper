# include <iostream>
# include <stdio.h>
# include <fstream>

# define MAX 3000

using namespace std;

int main(int argc, char **argv)
{
	ifstream in("input.in");
	FILE* out = fopen("output.out","w");
	int totalCase;
	in >> totalCase;

	for(int caseNum = 1; caseNum <= totalCase; caseNum++)
	{
		double answer = 0;
		int w[MAX][3];
		int d[MAX][3];
		
		int len, count, cnt, num;
		double runT, runS, speed;
		in >> len >> speed >> runS >> runT >> count;
		for(int i = 0; i < count; i++)
		{
			in >> w[i][0] >> w[i][1] >> w[i][2];
		}

		int n = 0;
		cnt = 0;
		
		for(int i = 0; i < count; i++)
		{
			if(w[i][0] != n)
			{
				d[cnt][0] = n;
				d[cnt][1] = w[i][0];
				d[cnt][2] = 0;
				cnt++;
			}
			
			n = w[i][1];
			d[cnt][0] = w[i][0];
			d[cnt][1] = w[i][1];
			d[cnt][2] = w[i][2];
			cnt++;
		}


		if(n != len)
		{
			d[cnt][0] = n;
			d[cnt][1] = len;
			d[cnt][2] = 0;
			cnt++;
		}
		int max = -1;
		for(int i = 0 ; i < cnt; i++)
		{
			if(d[i][2] > max)
			{
				max = d[i][2];
			}
		}

		
		int t;
		for(int i = 0; i <= max; i++)
		{
			t = i;
			num = 0;
			for(int j = 0; j < cnt; j++)
			{
				if(d[j][2] == i)
				{
					num += (d[j][1] - d[j][0]);
				}
			}

			double a = num / (runS + i);
			if(a >= runT)
			{
				answer += runT;
				answer += ((num - runT * (runS + i)) / (speed + i));
				break;
			}
			else
			{
				answer += (num / (runS + i));
				runT -= (num / (runS + i));
			}
		}

		for(int i = 0; i < cnt; i++)
		{
			if(d[i][2] > t)
			{
				answer += ((d[i][1] - d[i][0]) / (speed + d[i][2]));
			}
		}

		fprintf(out,"Case #%d: %llf\n", caseNum, answer);
		//out << "Case #" << caseNum << ": " << answer << endl;
	}
	return 0;
}