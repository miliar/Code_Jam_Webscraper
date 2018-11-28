#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main (int argc, char * const argv[]) {
	int N, S, Q;
	string engines[100];
	string search[1000];
	int results[100];
	int result;
	string current;
	int l, m;
	bool f1, f2;
	
	ifstream	fin ("/input.in");
	ofstream fout ("/output.txt");
	
	fin >> N;
	
	for (int i=0; i<N; i++)
	{
		l =0;
		m =0;

		fin >> S;
		getline (fin, engines[0]);
		for (int j=0; j<S; j++)
		{
			getline (fin, engines[j]);
		}

		fin >> Q;
		getline (fin, search[0]);
		for (int k=0; k < Q; k++)
		{
			getline (fin, search[k]);
		}

		while (m < Q)
		{		
//l++;
			result =0;
			for (int n=0; n<S; n++)
			{
				if (results[n]>0)
					results[n]--;
				if (results[n]==1)
					result = 1;
			}
			f1 = false;		
			while (m<Q && f1 == false)
			{
					f2 = false;
					for (int j=0; j<S && f2 == false; j++)
					{
						if (results[j]==0)
						{
							if (search[m] == engines[j])
							{
								result++;								
								if (result == S)
								{
									results[j]=2;
									f2=true;
								}
								else
									results[j]=1;
							}
						}
					}
					m++;
					if (result == S)
					{
						l++;
						f1 = true;
					}
			}
		}
		if (l<0)
			l=0;
		fout << "Case# " << (i+1) << ": " << l << endl;
	}
	fin.close();
	fout.close();
    return 0;
}
