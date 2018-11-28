#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;


int main()
{
	string file = "B-large";
	ifstream ifs((file+".in").c_str());
	ofstream ofs((file+".out").c_str());
	int num_of_problems;

	ifs >> num_of_problems;
    for(int problem=0; problem<num_of_problems; problem++)
	{
        //input
        long long L, P, C;
        ifs >> L >> P >> C;
        
        // init
        long long result = 0;
        long long val = P;

        // main
        while(L * C < val)
        {
            val = ceil(sqrt((double)L * val));
            result++;
        }

        //output
		ofs << "Case #" << problem+1 << ": " << result << endl;
		cout << problem << endl;
	}

	return 0;
}

