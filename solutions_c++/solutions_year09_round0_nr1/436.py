#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<sstream>
#include<fstream>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");
    int ntokens,nwords,ntests;
    fin>>ntokens>>nwords>>ntests;
    //get dictionary
    vector<string>dict;
    for(int i=0;i<nwords;i++)
    {
        string word;
        fin>>word;
        dict.push_back(word);
    }
    string trash;
    getline(fin,trash);
    //get tests
    vector<string>tests;
    for(int i=0;i<ntests;i++)
    {
        string test;
        getline(fin,test);
        tests.push_back(test);
    }
    
    //parse tests
    //(make (ab) (bc) (ca) into a vector[3][2]
    vector<vector<string> >atests;
    for(int i=0;i<ntests;i++)
    {
        string curstr=tests[i];
        string characters;
        int curstrsize=curstr.size();
        vector<string>tokens;
        //for all characters in curstr
        for(int j=0;j<curstrsize;j++)
        {
            string characters;
            if(curstr[j]=='(')
            {
                //goto next character and look until ')' is hit
                for(j++;j<curstrsize && curstr[j]!=')';j++)
                {
                    characters+=curstr[j];
                }
                
            }
            else characters+=curstr[j];
            tokens.push_back(characters);
        }
        atests.push_back(tokens);
    }
    //process
    //for all tests
    for(int i=0;i<ntests;i++)
    {
        long long tot=0;
        int curtestsize=atests[i].size();
        //check to see if word fits with test
        //for all words in dictionary
        vector<string>tokens=atests[i];
        for(int j=0;j<nwords;j++)
        {
            string curword=dict[j];
            int curwordsize=curword.size();
            if(curtestsize!=curwordsize)continue;
            
            bool foundword=true;
            //for each character in curword && token place
            for(int k=0;k<curwordsize;k++)
            {
                //for each character in tokens
                bool foundchar=false;
                for(int l=0;l<tokens[k].size();l++)
                {
                    if(tokens[k][l]==curword[k])
                    {
                        foundchar=true;
                        break;
                    }
                }
                //if can't find char then cant find word
                if(!foundchar)
                {
                    foundword=false;
                    break;
                }
            }
            if(foundword)
            {
                tot++;
            }
        }
        fout<<"Case #"<<i+1<<": "<<tot<<endl;
    }
    cout<<"done"<<endl;
    int z;
    cin>>z;
    return 0;
}
        
