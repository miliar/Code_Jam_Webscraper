#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T, PD, PG;
	long long N;
    fin >> T;
    for (int i = 1 ; i <= T ; i++)
    {
        fin>> N >> PD >> PG;
		int s = 0;
		bool check = true;
		for (int k = 1 ; k <= 100 ; k++)
			if ((k*PD)%100==0) {s=k; break;}
		if (s > N) check = false;
        else
		{
			if (PG == 100 && PD != 100) check = false;
			if (PG == 0 && PD != 0) check = false;
		}		
		
		fout << "Case #" << i << ": ";
		if (check) fout << "Possible" << endl;
		else fout << "Broken" << endl;
    }
       
}
