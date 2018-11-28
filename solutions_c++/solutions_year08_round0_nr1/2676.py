#include <fstream>
#include <cmath>
#include <string>
using namespace std;

ifstream in;
ofstream out;
unsigned long amount;
unsigned long S;
unsigned long Q;
long num;
unsigned long re;
unsigned long last;
string strS[100];
string strQ[1000];
bool used[100];
string tmp;

void main()
{
	in.open("A-small.in");
	out.open("A-small.out");

	int k=0;
	int i, j, m;
	in >> amount;
	for(k=1; k<=amount; k++)
	{
		in >> S;
		getline(in, tmp);
		for(i=0; i<S; i++)
		{
			getline(in, strS[i]);
			used[i] = false;
		}

		in >> Q;
		getline(in, tmp);
		num = 0;
		re = S;
		last = 0;
		for(i=0; i<Q; i++)
		{
			getline(in, strQ[i]);
		}

		for(i=0; i<Q; i++)
		{
			for(j=0; j<S; j++)
			{
				if(strQ[i] == strS[j])
				{
					if(!used[j])
					{
						used[j] = true;
						re--;
					}
					break;
				}
			}
			if(re == 0)
			{
				for(m=0; m<S; m++)
				{
					used[m] = false;
				}
				num++;
				re = S;
				i--;
			}
		}

		out << "Case #" << k << ": " << num << endl;
	}

	in.close();
	out.close();
}