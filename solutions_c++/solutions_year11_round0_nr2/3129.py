#include<fstream>
#include<iostream>
#include<vector>
#include<string>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int T, C, D, N;

int main()
{
    vector<char> current;
    vector<vector<char> > comb(256, vector<char>(256, 0));
    vector<vector<bool> > clear(256, vector<bool>(256, false));
    in >> T;
    for(int t = 0; t < T; t++)
    {
        comb = vector<vector<char> >(256, vector<char>(256, 0));
        clear = vector<vector<bool> >(256, vector<bool>(256, false));
        if(t == 4)
        {
            bool debug = true;
        }
        current = vector<char>();
        in >> C;
        for(int i = 0; i < C; i++)
        {
            string s;
            in >> s;
            comb[s[0]][s[1]] = s[2];
            comb[s[1]][s[0]] = s[2];
        }
        in >> D;
        for(int i = 0; i < D; i++)
        {
            string s;
            in >> s;
            clear[s[0]][s[1]] = true;
            clear[s[1]][s[0]] = true;
        }
        in >> N;
        string s;
        in >> s;
        for(int i = 0; i < N; i++)
        {
            current.push_back(s[i]);

            while(current.size() > 1)
            {
                char val = comb[current[current.size() - 1]][current[current.size() - 2]];
                if(val > 0)
                {
                    current.pop_back();
                    current[current.size() - 1] = val;
                }
                else
                    break;
            }
            for(int p1 = 0; p1 < current.size(); p1++)
                for(int p2 = 0; p2 < current.size(); p2++)
                    if(clear[current[p1]][current[p2]])
                        current.clear();
            if(t == 5)
            {
                cout << "added s[i] = " << s[i] << endl << "[";
                if(current.size() > 0)
                {
                    for(int i = 0; i < current.size() - 1; i++)
                        cout << current[i] << ", ";
                    cout << current[current.size() - 1];
                }
                cout << "]" << endl;
            }
        }
        out << "Case #" << t + 1 << ": [";
        if(current.size() > 0)
        {
            for(int i = 0; i < current.size() - 1; i++)
                out << current[i] << ", ";
            out << current[current.size() - 1];
        }
        out << "]" << endl;
    }
    return 0;
}
