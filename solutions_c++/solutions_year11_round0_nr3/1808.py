#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
ifstream in("C-large.in");
ofstream out("C-large.out");
// ifstream in(stdin);
// ofstream out(stdout);

int bit[32];

void binary_add(int x)
{
	/*out<<"add X = "<<x<<endl;*/
	int tmp;
	int idx = 0;
	while (x !=0)
	{
		tmp = x&0x00000001;
		x >>= 1;
		bit[idx] =( bit[idx] == tmp ? 0 : 1 );
		idx++;
	}

// 	for (int i=0;i<32;i++)
// 	{
// 		out<<bit[i];
// 	}
// 	out<<endl;
// 	system("pause");
}
bool zero()
{
	for (int i=0;i<32;i++)
	{
		if (bit[i] == 1)
			return false;
	}
	return true;
}

int main()
{
	int t,n;
	int tmp;
	in>>t;
	for(int ii=1;ii<=t;ii++)
	{
		memset(bit,0,sizeof(bit));
		in>>n;
		int count = 0;
		int min = 0x7fffffff;
		for (int i=0;;i++)
		{
			in>>tmp;
			if (min > tmp)
			{
				min = tmp;
			}
			count+=tmp;
			binary_add(tmp);
			if (i == n-1)
			{
				if (!zero())
				{
					out<<"Case #"<<ii<<": NO"<<endl;
				}
				else
				{
					out<<"Case #"<<ii<<": "<<count-min<<endl;
				}
				break;
			}
		}
	}
	//system("pause");
	return 0;
}