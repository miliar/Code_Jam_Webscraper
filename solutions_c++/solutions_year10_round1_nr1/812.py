#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
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
        bool Red = false, Blue = false;
        string result = "";

        //input
        int N, K;
        ifs >> N >> K;
        vector<string> field(N), field2(N), field3(2*N), field4(2*N);
        for(int i=0; i<N; i++) { ifs >> field[i]; }

        // remove '.' and reverse and add '.' until N columns
        for(int i=0; i<N; i++)
        {
            for(int j=N-1; j>=0; j--)
            {
                if(field[i][j] == '.') field[i].erase(field[i].begin()+j);
            }
            reverse(field[i].begin(), field[i].end());
            field[i] += string(N-field[i].size(), '.');
        }

        // transposed field
        // field2
        for(int i=0; i<N; i++)
        {
            field2[i] = string(N, '.');
            for(int j=0; j<N; j++)
            {
                field2[i][j] = field[j][i];
            }
        }
        // field3
        for(int i=0; i<2*N; i++)
        {
            field3[i] = string(N, '.');
        }
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                field3[i+N-j][j] = field[i][j];
            }
        }
        // field4
        for(int i=0; i<2*N; i++)
        {
            field4[i] = string(N, '.');
        }
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                field4[i+j][j] = field[i][j];
            }
        }

        // check
        for(int i=0; i<N; i++)
        {
            // hor
            if(field[i].find(string(K, 'B'), 0) != string::npos) Blue = true;
            if(field[i].find(string(K, 'R'), 0) != string::npos) Red = true;
            //ver
            if(field2[i].find(string(K, 'B'), 0) != string::npos) Blue = true;
            if(field2[i].find(string(K, 'R'), 0) != string::npos) Red = true;
        }
        for(int i=0; i<2*N; i++)
        {
            // diag
            if(field3[i].find(string(K, 'B'), 0) != string::npos) Blue = true;
            if(field3[i].find(string(K, 'R'), 0) != string::npos) Red = true;
            if(field4[i].find(string(K, 'B'), 0) != string::npos) Blue = true;
            if(field4[i].find(string(K, 'R'), 0) != string::npos) Red = true;
        }

        if(Blue && Red) result = "Both";
        else if(Blue) result = "Blue";
        else if(Red) result = "Red";
        else result = "Neither";

        //output
		ofs << "Case #" << problem+1 << ": " << result << endl;
		cout << problem << endl;
	}

	return 0;
}

