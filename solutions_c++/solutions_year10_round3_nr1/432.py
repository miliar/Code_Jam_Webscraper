#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;


int main()
{
	string file = "A-large";
	ifstream ifs((file+".in").c_str());
	ofstream ofs((file+".out").c_str());
	int num_of_problems;

	ifs >> num_of_problems;
    for(int problem=0; problem<num_of_problems; problem++)
	{
        //input
        int N; ifs >> N;
        vector<int> A(N), B(N);
        for(int i=0; i<N; i++) { ifs >> A[i] >> B[i]; }
        
        // init
        int result = 0;

        // main
        for(int i=0; i<N; i++)
        {
            for(int j=i; j<N; j++)
            {
                if(A[i] < A[j] && B[i] > B[j] || A[i] > A[j] && B[i] < B[j]) result++;
            }
        }
        

        //output
		ofs << "Case #" << problem+1 << ": " << result << endl;
		cout << problem << endl;
	}

	return 0;
}

