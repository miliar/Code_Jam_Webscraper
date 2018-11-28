#include <iostream>
#include <string>
#include <vector>
using namespace std;

string words[5000];
string pattern[15];
int main()
{
    int L; // every word has contain exactly L letters
    int D; // there are exactly D words in the language
    int N; // number of test cases
    string p;
    int match;
    
    cin >> L >> D >> N;
    
    for(int i = 0; i < D; ++i)
        cin >> words[i];
    
    for(int i = 0; i < N; ++i)
    {
        cin >> p;
        
        string::iterator end = p.end();
        string::iterator iter = p.begin();
        for(int j = 0; j < L; ++j)
        {
            if(*iter == '(')
            {
                string tmp = "";
                ++iter;
                while(*iter != ')')
                {
                    tmp.push_back(*iter);
                    ++iter;
                }
                pattern[j] = tmp;
            }
            else
            {
                string tmp = "";
                tmp.push_back(*iter);
                pattern[j] = tmp;
            }
            ++iter;
        }
        /*
        for(int j = 0; j < L; ++j)
            cout << pattern[j] << " ";
        cout << endl;
        */
        
        match = 0;
        for(int j = 0; j < D; ++j)
        {
            int k;
            for(k = 0; k < L; ++k)
            {
                if(pattern[k].find(words[j][k]) == string::npos)
                    break;
            }
            if(k == L)
                match += 1;
        }
        printf("Case #%d: %d\n", i + 1, match);
    }
    return 0;
}
                
        
    
    
