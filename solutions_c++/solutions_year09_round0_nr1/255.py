#include <fstream>
#include <vector>
#include <string>
#include <set>

using namespace std;

int main(int argc, char** argv)
{
    int L, D, N;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    vector<string> dict;
    
    fin >> L >> D >> N;
    for(int i = 0; i < D; i++)
    {
        string word;
        fin >> word;
        dict.push_back(word);
    }
    
    for(int i = 0; i < N; i++)
    {
        string pat;
        int count = 0;
        
        vector< set<char> > pattern;
        bool paren = false;
        
        fin >> pat;
    

        // parse pat
        for(int j = 0; j < pat.size(); j++)
        {
            if(pat[j] == '(')
            {
                paren = true;
                pattern.push_back(set<char>());
            }
            else if(pat[j] == ')')
            {
                paren = false;
            }
            else if(paren == true)
            {
                pattern.back().insert(pat[j]);
            }
            else
            {
                pattern.push_back(set<char>());
                pattern.back().insert(pat[j]);
            }
        }
        
        for(int j = 0; j < D; j++)
        {
            bool flag = true;
            if(pattern.size() != dict[j].size()) continue;
            for(int k = 0; k < pattern.size(); k++)
            {
                if(pattern[k].count(dict[j][k]) == 0)
                {
                    flag = false;
                    break;
                }
            }
            if(flag) count++;
        }
        
        fout << "Case #" << i + 1 << ": " << count << endl;
    }
    
    fin.close();
    fout.close();
    return 0;
}
