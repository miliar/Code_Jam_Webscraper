#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T, N,S, p;
    fin >> T;
    
    int score[101];
    for (int i = 1 ; i <= T; i++)
    {  
		fin >> N >> S >> p;

		int low_bound = p + max(p-1,0)*2;
		int superlow_bound = p + max(p-2,0)*2;

		int low_answer = 0;
		int superlow_answer = 0;
		for (int j = 0 ; j < N ; j++)
		{
            fin >> score[j];
            if (score[j] >= low_bound)
                low_answer++;
			else if (score[j] >= superlow_bound)
				superlow_answer++;
		}
		
		int answer = low_answer + min(superlow_answer, S);
		fout << "Case #" << i << ": ";
		fout << answer << endl;
    }
}
