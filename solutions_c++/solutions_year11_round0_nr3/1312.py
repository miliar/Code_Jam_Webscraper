#include <iostream>
#include <fstream>

using namespace std;

int seq[1001];
int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    int T, N;
    fin >> T;
    for (int i = 1 ; i <= T; i++)
    {  
		fin >> N;

        int check = 0;
        int smallest = 1000000;
        int sum = 0;
		for (int j = 1 ; j <= N ; j++)
		{
			fin >> seq[j];
			if (smallest > seq[j]) smallest = seq[j];
			sum += seq[j];
			check = check^seq[j];
		}
  
  
		fout << "Case #" << i << ": ";
		if (check != 0) fout << "NO" << endl;		
		else fout << sum-smallest << endl;
    }
}
