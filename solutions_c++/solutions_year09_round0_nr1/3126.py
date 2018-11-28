#include <regex.h>
#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
    int L, D, N;
    
    cin >> L >> D >> N;
    
    char **words = new char*[D];
    
    for(int i=0; i<D; ++i)
        words[i] = new char[L];
        
    string *patterns = new string[N];
    regex_t *regex = new regex_t[N];
    
    
    for(int i=0; i<D; ++i)
        cin >> words[i];
    
    cin.ignore(80, '\n');
    for(int i=0; i<N; ++i)
    {
        getline(cin, patterns[i]);
        
        replace(patterns[i].begin(), patterns[i].end(), '(', '[');
        replace(patterns[i].begin(), patterns[i].end(), ')', ']');
    }
    
    for(int i=0; i<N; ++i)
        regcomp(regex+i, patterns[i].c_str(), REG_NOSUB);
    
    int *num_matched = new int[N];
    
    for(int i=0; i<N; ++i)
        num_matched[i] = 0;
        
    for(int i=0; i<N; ++i)
        for(int j=0; j<D; ++j)
            if( regexec(regex+i, words[j], 0, NULL, 0) == 0 )
                num_matched[i]++;

    for(int i=0; i<N; ++i)
        cout << "Case #" << (i+1) << ": " << num_matched[i] << endl;
            

    for(int i=0; i<D; ++i)
        delete [] words[i];    
        
    delete [] words;
    delete [] patterns;
    delete [] regex;
    delete [] num_matched;
    
    return 0;
} 

