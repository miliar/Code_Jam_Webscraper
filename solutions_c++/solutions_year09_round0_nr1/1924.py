#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
using namespace std;
    
struct pattern
{
    bool valid[15]['z' - 'a' + 1];
    
    pattern()
    {
        memset(valid, false, sizeof(valid));
    }
};

bool word_matches(string word, pattern p)
{
    for (size_t j = 0; j < word.size(); j++)
        if (!p.valid[j][word[j] - 'a'])
            return false;
    return true;
}

int main()
{
    vector<string> words;
    int L, D, N;

    cin >> L >> D >> N;
    for (int i = 0; i < D; i++)
    {
        string word;
        cin >> word;
        words.push_back(word);
    }
    
    for (int i = 0; i < N; i++)
    {
        pattern p;
        string word;
        cin >> word;
        int index = 0;
        int matches = 0;
        bool in_parenthesis = false;
        for (size_t j = 0; j < word.size(); j++)
        {
            if (word[j] == '(')
                in_parenthesis = true;
            else if (word[j] == ')')
                in_parenthesis = false;
            else
                p.valid[index][word[j] - 'a'] = true;
            
            if (!in_parenthesis)
                index++;
        }
        
        for (size_t j = 0; j < words.size(); j++)
            if (word_matches(words[j], p))
                matches++;
        
        cout << "Case #" << i + 1 << ": " << matches << endl;
    }
    
    return 0;
}
