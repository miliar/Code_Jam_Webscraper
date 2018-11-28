#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


int match_pattern(vector<string> words, string pattern);

int main()
{
    ifstream infile;
    ofstream outfile;
    
    int D;
    int L;
    int N;
    
    int i;
    
    int match_count;
    
    vector<string> words(5000);
    vector<string> patterns(500);
    
    infile.open("alienb.in");
    outfile.open("alienb.out");
    
    if(infile.is_open())
    {
        infile >> L >> D >> N;
        
        words.clear();
        words.resize(D);
        
        patterns.clear();
        patterns.resize(N);
        
        for(i=0; i<D; i++)
            infile >> words[i];
        for(i=0; i<N; i++)
            infile >> patterns[i];
            
        for(i=0; i<patterns.size(); i++)
        {
            //match_count = 0;
            
            //for(j=0; j<words.length; j++)
            //{
            //    if(match_pattern(words[j], pattern[i]))
            //        ++match_count;
            //}
            //clog << "pattern = " <<patterns[i] << endl;
            
            match_count = match_pattern(words, patterns[i]);
            
            //clog << "count = " << match_count << endl;
            //system("PAUSE");
            
            outfile << "Case #" << i+1 << ": " << match_count << endl;
        }
    }
    
    infile.close();
    outfile.close();

    //system("PAUSE");
    return 0;
}
        
int match_pattern(vector<string> words, string pattern) 
{
    string word;
    bool composite_literal = false;
    int literal_count = 0;
    int match_count = 0;
    int i;
    int j;
    int k;
    
    bool found;
    
    //clog << "inside method\n" << endl;
    //clog << "pattern = " << pattern << endl;
    //clog << "breaking the pattern\n" << endl;
    
    vector<string> literals (pattern.length());
    for(i=0; i<pattern.length(); i++)
    {
        
        //clog << "char = " << pattern[i] << endl;
        if(pattern[i] == '(')
        {
            composite_literal = true;
            //if(i != 0)
                //++literal_count;
        }
        else if(pattern[i] == ')') 
        {
            composite_literal = false;
            ++literal_count;
        }
        else
        {
            if(literals[literal_count].length() == 0)
                literals[literal_count] = pattern[i];
            else
                literals[literal_count] += pattern[i];
                
            //clog << "literal = " << literals[literal_count] << endl;
                
            if(!composite_literal)
                ++literal_count;
        }
        
        
    }
    
    //clog << "size = " << words.size() << endl;
    
    for(i=0; i<words.size(); i++)
    {
        word = words[i];
        found = true;
        
        //clog << "word = " << word << endl;
        //clog << "length = " << word.length() << endl;
        //system("PAUSE");
        
        for(k=0; k<word.length(); k++)
        {
            //clog << "matching : " << literals[k] << " - " << word[k] << endl;
            if(literals[k].find(word[k]) == string::npos)
            {
                found = false;
                break;
            }
        }
        
        if(found == true)
            ++match_count;
    }
    
    return match_count; 
}
            
            
