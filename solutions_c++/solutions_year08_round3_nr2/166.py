#include <iostream>
#include <fstream>
#include <map>
#include <cmath>
#include <iomanip>

using namespace std;

ifstream fin;
ofstream fout;

int N;
char line[1024];
char *sa;
int len;

int pa[] = {2, 3, 5, 7};

double nu;

void calc()
{
	int i, j;
	int s;
	double re, tmp;

	sa[len - 1] = '+';

/*	for(i = 0; i < len ; i ++)
	{
		cout << sa[i] << " " ;
	}
	cout << endl;
*/
	if(len == 1)
	{	
		re = line[0] - 0x30;
	}
	else
	{
		//re = line[0] - 0x30;
		tmp = 0; s = 1; re  = 0;

		for(i = 0; i < len; i ++)
		{
			if(sa[i] == '0')
			{
				tmp = tmp * 10 + line[i] - 0x30;
			}
			else if(sa[i] == '-')
			{
				tmp = tmp * 10 + line[i] - 0x30;
				re += tmp * s;
				s = -1;
				tmp = 0;
			}
			else if(sa[i] == '+')
			{
				tmp = tmp * 10 + line[i] - 0x30;
				re += tmp * s;
				s = 1;
				tmp = 0;
			}
		}
	}

	for(j = 0; j < 4; j ++)
	{
		if(floor(re / pa[j]) ==  re / pa[j])
		{
			nu ++;
			break;
		}
	}
//	cout << "result " << re << endl;
}

void setsa(int p)
{
	if(p == len - 1)
	{
		
		calc();
		return;
	}

	sa[p] = '-';
	setsa(p + 1);

	sa[p] = '0';
	setsa(p + 1);

	sa[p] = '+';
	setsa(p + 1);
}

void solve(int i)
{


	len = strlen(line);
	
	sa = new char[len + 1];
	
	nu = 0;
	setsa(0);

	cout << "Case #" << i << ": " << fixed  << nu << endl;
	fout << "Case #" << i << ": " << fixed << setprecision(0) << nu << endl;
	delete[] sa;

}



int main()
{
	int i, j, k, h;
	double re;
	fin.open("B-small.in");
	fout.open("B-small.out");

	fin >> N;
	fin.getline(line, 1024);

	for(i = 0; i < N; i ++)
	{
		fin.getline(line, 1024);
	//	cout << line << endl;

		if(strlen(line) == 1 && line[0] == '0')
		{
			cout << "Case #" << i + 1 << ": " << 1 << endl;
			fout << "Case #" << i + 1 << ": " << 1 << endl;
		}
		else
		{
			solve(i + 1);
		}

	}

	return 0;
}