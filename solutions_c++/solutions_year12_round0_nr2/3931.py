#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void DancingWithGooglers()
{
	ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");

    int num_cases;
    fin >> num_cases;

    for (int T = 1; T <= num_cases; ++T)
    {
    	int num_googler, num_surprise, best_result, count = 0;
    	fin >> num_googler;
    	fin >> num_surprise;
    	fin >> best_result;

    	for (int i = 0; i < num_googler; ++i)
    	{
    		int total;
    		fin >> total;

    		if (total < best_result || (total+1)/3 < (best_result-1))
    			continue;

    		if ((total+2)/3 >= best_result)
    			++count;
    		else if (num_surprise > 0)
    		{
				++count;
				--num_surprise;
    		}
    	}
        fout << "Case #" << T << ": " << count << endl;
    }
    fin.close();
    fout.close();
}
