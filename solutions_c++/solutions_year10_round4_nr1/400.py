#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

bool elegant(const vector<string> &d, int ax)
{
    int K = d.size() / 2 + 1;
    for(int i=K-1-ax; i<d.size()-1-(K-1-ax); i++)
    {
        int start_j;
        if(i <= K-1) { start_j = (K - 1) - i; }
        else { start_j = i - (K - 1); }
        for(int j=start_j; j<ax; j++)
        {
            if(d[i][j] != d[i][2*ax-j]) return false;
        }
    }
    return true;
}


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
        int K;
        ifs >> K;
        string buf; getline(ifs, buf);
        vector<string> diamond(2*K-1);
        for(int i=0; i<2*K-1; i++)
        {
            getline(ifs, diamond[i]);
            while(diamond[i].size()<2*K-1) diamond[i] += " ";
        }
        
        // init
        int result = 0;

        // main
        // horizon check
        vector<string> diamond_r = diamond;
        for(int i=0; i<diamond.size(); i++) for(int j=0; j<diamond[i].size(); j++)
        {
            diamond_r[i][j] = diamond[i][2*K-2-j];
        }
        for(int ax=K-1; ax>0; ax--)
        {
            if(elegant(diamond, ax) || elegant(diamond_r, ax)) break;
            else result++;
        }

        // “]’u‚µ‚Ä“¯—l‚É
        vector<string> diamond_t = diamond;
        for(int i=0; i<diamond.size(); i++) for(int j=0; j<diamond[i].size(); j++)
        {
            diamond_t[i][j] = diamond[j][i];
        }

        for(int i=0; i<diamond_t.size(); i++) for(int j=0; j<diamond_t[i].size(); j++)
        {
            diamond_r[i][j] = diamond_t[i][2*K-2-j];
        }
        for(int ax=K-1; ax>0; ax--)
        {
            if(elegant(diamond_t, ax) || elegant(diamond_r, ax)) break;
            else result++;
        }

        int res = 0;
        for(int i=0; i<result; i++) res += 2*(K + i) + 1;

        //output
		ofs << "Case #" << problem+1 << ": " << res << endl;
		cout << problem << endl;
	}

	return 0;
}

