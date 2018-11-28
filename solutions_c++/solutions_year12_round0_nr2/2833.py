//Christopher Mueller
//Made for Google Code Jam 2012

#include <fstream>
#include <string>
#include <sstream>

using namespace std;

void solve(string& str)
{
    int N, S, p;
    stringstream ss(str);
    ss >> N >> S >> p;

    int total = 0; //the number of dancers who could have scored at least p
    for(int i = 0; i < N; ++i)
    {
        int score;
        ss >> score;

        int quotient = score / 3;
        int remainder = score % 3;

        if(remainder == 1)
        {
            if(quotient + 1 >= p) ++total;
        }
        else if(remainder == 0)
        {
            if(score != 0 || p == 0)
            {
                if(quotient >= p) ++total;
                else if(S > 0 && quotient + 1 == p)
                {
                    ++total;
                    --S;
                }
            }
        }
        else
        {
            if(quotient + 1 >= p) ++total;
            else if(S > 0 && quotient + 2 == p)
            {
                ++total;
                --S;
            }
        }
    }

    stringstream out;
    out << total;
    str = out.str();
}

int main()
{
    string str;

    ifstream infile("B-large.in");
    int T;
    infile >> T;
    getline(infile, str); //remove the newline after T

    ofstream outfile("output.txt");
    for(int i = 0; i < T; ++i)
    {
        outfile << "Case #" << i + 1 << ": ";
        getline(infile, str);

        solve(str);

        outfile << str << endl;
    }

    return 0;
}
