#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;



int main()
{
	int N , S , Q;
	ifstream file;
	file.open("inl.txt");
	ofstream out;
	out.open("outl.txt");
	file >> N;
	string Engine[110];
	string Query[1001];
	int Es[100];
	int jumps;
	int i , j;
	for (int count = 1 ; count <= N ; count++)
	{
		jumps = 0;
		file >> S;
		i=1;
		getline(file , Engine[i] , '\n');
		for ( ; i <= S ; i++)
		{
			getline(file , Engine[i] , '\n');
		}
		file >> Q;
		i=1;
		getline(file , Query[i] , '\n');
		for ( ; i <= Q ; i++)
		{
			getline(file , Query[i] , '\n');
		}
		int Curr = 1;
BACK:
		for (i=1 ; i <= S ; i++)
		{
			Es[i] = -1;
		}
		for (i=1 ; i <= S ; i++)
		{
			for (j=Curr ; j <= Q ; j++)
			{
				if (Query[j] == Engine[i])
				{
					Es[i] = j;
					break;
				}
			}
		}
		int max = 1;
		for (i=1 ; i <= S ; i++)
		{
			if (Es[i] == -1)
			{
				goto Display;
			}
		}
		for (i=1 ; i <= S ; i++)
		{
			if (Es[max] < Es[i])
			{
				max = i;
			}
		}
		jumps++;
		Curr = Es[max];
		goto BACK;
Display:
		out << "Case #" << count << ": " << jumps << "\n";
	}
	file.close();
	out.close();
	return 0;
}