#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main (int argc, char *argv[])
{
	fstream file;
	char SearchEngName[110][100];
	int vSE[100];
	int S;				//No. of Search Engines
	char query[100];
	int Q;				//No. of Queries
	int N;				//Test Cases
	int switches;
	
	file.open (argv[1], ios::in);
	
	file >> N;
	for (int i=0; i<N; i++)
	{
		switches = 0;
		file >> S;
		file.get();
		for (int j=0; j<S; j++)
		{
			file.getline (SearchEngName[j], 100);
			vSE[j] = 0;
		}
		int uniq = 0;
		file >> Q;
		file.get();
		for (int k=0; k<Q; k++)
		{
			int j;
			file.getline (query, 100);
			
			for (j=0; j<S; j++)
			{
				if (!strcmp(query, SearchEngName[j]))
					break;
			}
			if (!vSE[j])
			{
				vSE[j] = 1;
				uniq ++;
			}
			if (uniq == S)
			{
				switches ++;
				for (int x=0; x<S; x++)
					vSE[x] = 0;
				vSE[j] = 1;
				uniq = 1;
			}
		}
		cout <<"Case #" <<i+1 <<": " <<switches <<endl;
	}
	return 0;
}
