#include <iostream>
#include <vector>
#include <boost/regex.hpp> 



using namespace std;
using namespace boost;

int main()
{
    int L, D, N;
    vector<string> words, patterns;
    
    cin >> L >> D >> N;
    
    // cout << "L = " << L << ", D = " << D << ", N = " << N << endl;
    
    for (int i = 0; i < D; ++i)
    {
        string w;
        
        cin >> w;
        
        words.push_back(w);
    }
    
    for (int i = 0; i < N; ++i)
    {
        string p;
        
        cin >> p;
        
        // insert pipes
        bool in_brackets = false;
        int bracket_chars = 0;
        for (int c = 0; c < p.size(); ++c)
        {
            if (p.at(c) == '(')
            {
                in_brackets = true;
                bracket_chars = 0;
            }
            else
                if (p.at(c) == ')')
                {
                    in_brackets = false;
                    bracket_chars = 0;
                }
            else
            {
                if (in_brackets)
                {
                    if (bracket_chars > 0)
                    {
                        p.insert(c, "|");
                        c++;
                    }
                    bracket_chars++;
                }
            }
                
        }
        
        
        patterns.push_back(p);
    }
    
#if 0    
    cout << "patterns:\n";
    for (int i = 0; i < N; ++i)
    {
	cout << patterns.at(i) << endl;
    }
#endif
    
    for (int k = 0; k < N; ++k)
    {
        int count = 0;
        for (int w = 0; w < D; ++w)
        {
            //cmatch what;
            regex re(patterns.at(k));
            if (regex_match(words.at(w), re))
                count++;
        }
        cout << "Case #" << k+1 << ": " << count << endl;
    }
    
    
}
