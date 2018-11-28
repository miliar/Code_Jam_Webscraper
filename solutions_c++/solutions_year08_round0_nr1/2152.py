#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	int i,j,k;
	int N,S,Q,nswitch,num;
	ifstream in;
	ofstream out;
	char sample[100][100] = {0};
	char temp[100] = {0};
	char bused[100];
	in.open ("A-large.in");
	out.open ("A-large.out");
	in>>N;
	for (i=0; i<N; i++)
	{
		in>>S;
		in.ignore ();
		nswitch = 0;
		num = 0;
		memset(bused,0,100);
		for (j=0; j<S; j++)
		{
			in.getline(sample[j],100);
		}
		in>>Q;
		in.ignore ();
		for (j=0; j<Q; j++)
		{
			in.getline(temp,100);
			for (k=0;k<S;k++)
			{
				if (!strcmp(temp,sample[k]))
				{
					
					if (bused[k] == 0)
					{
						if (num == S - 1)
						{
							nswitch++;
							memset (bused,0,100);
							bused[k] = 1;
							num = 1;
						}
						else
						{
							bused[k] = 1;
							num++;
						}
					}
					break;
				}
			}
			
		}
		out<<"Case #"<<i+1<<": "<<nswitch<<endl;
	}
	in.close();
	out.close();
}