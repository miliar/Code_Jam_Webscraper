# include <iostream>
# include <fstream>
# define MAX 2000

using namespace std;

int main(int argv, char **argc)
{
	ifstream in("input.in");
	ofstream out("output.out");
	int totalCase;
	in >> totalCase;
	
	for(int caseNumber = 1; caseNumber <= totalCase; caseNumber++)
	{
		int bn, bt, count, cnt;
		int answer = 0;
		int w[MAX];
		char buff[20];
		in >> bn >> buff >> count >> cnt;
		bt = 0;
		for(int i = 0; i < strlen(buff); i++)
		{
			bt = bt * 10;
			bt += (buff[i] - '0');
			if(bt >= 10000000)
			{
				bt = 10000000;
				break;
			}
		}

		for(int i = 0 ; i < cnt; i++)
		{
			in >> w[i];
		}


		int n = 0;
		int a = 0;
		int index = 0;
		int value = 0;
		for(int i = 0 ; i < count; i++)
		{
			value = w[i % cnt];
			if(n + value * 2 > bt){
				a= value - (bt - n) / 2;
				index = i + 1;
				break;
			}

			n = n + value * 2;
			if( n >= bt)
			{
				index = i + 1;
				break;
			}
		}

		int d[MAX];
		int num = 0;
		answer += bt;

		if(a != 0){
			d[0] = a;
			num=1;
		}

		for(int i = index; i < count; i++)
		{
			d[num] = w[i % cnt];
			num++;
		}

		int max,r;
		for(int i = 0; i < bn; i++)
		{
			max = 0;
			for(int j = 0; j < num; j++)
			{
				if(max < d[j])
				{
					max=d[j];
					r=j;
				}
			}
			answer += d[r];
			d[r] = 0;
		}

		for(int i = 0; i < num; i++)
		{
			answer += (d[i] * 2);
		}
		out << "Case #" << caseNumber << ": " << answer << endl;
	}

	in.close();
	out.close();
	return 0;
}