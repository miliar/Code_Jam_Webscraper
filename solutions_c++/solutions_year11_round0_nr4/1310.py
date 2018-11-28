#include <iostream>
#include <fstream>

using namespace std;

int seq[1001];
int main()
{
    ifstream fin("D-large.in");
    ofstream fout("D-large.out");
    int T, N;
    fin >> T;
    for (int i = 1 ; i <= T; i++)
    {  
		fin >> N;
	   
		int count_wrong = 0;
		for (int j = 1 ; j <= N ; j++)
		{
			fin >> seq[j];
			if (seq[j] != j) count_wrong++;
		}
		    
		fout << "Case #" << i << ": ";
		fout << count_wrong << endl;		
    }
}
