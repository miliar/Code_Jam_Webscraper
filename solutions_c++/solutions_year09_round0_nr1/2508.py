#include<iostream>
#include<string>
#include<vector>
#include<set>

#define MAXL 10 // small: 10; large: 15
#define MAXD 25 // small: 25; large: 5000

using namespace std;

set<string> findMatches(set<string> dic, string prefix)
{
    set<string> subdic;
    subdic.clear();

    //cout<<"findMatches(dic, \""<<prefix<<"\"): subdic = ";
    for(set<string>::iterator item=dic.begin(); item != dic.end(); item++)
        if(prefix == "" || (*item).compare(0, prefix.length(), prefix) == 0)
        {
            subdic.insert(*item);
            //cout<<"\""<<*item<<"\" ";
        }
    //cout<<endl;

    return subdic;
}

unsigned long numValids(set<string> dic, vector<string> breakup, string prefix)
{
    unsigned long valids = 0;

    //cout<<"numValids(): breakup.size() = "<<breakup.size()<<", prefix.length() = "<<prefix.length()<<"[\""<<prefix<<"\"]"<<endl;

    set<string> subdic = findMatches(dic, prefix);
    if(subdic.size() == 0)
        return 0;
    else if(subdic.size() == 1 && prefix.length() == breakup.size())
        return 1;
    else
    {
        string newprefix;
        for(unsigned int i=0; i<breakup[prefix.length()].length(); i++)
        {
            newprefix = prefix + breakup[prefix.length()][i];
            valids += numValids(dic, breakup, newprefix);
        }
        return valids;
    }
}

int main(int argc, char *argv[])
{
    unsigned int L, D, N;
    
    //vector<string> dic;
    set<string> dic;
    set<char> dicbag[MAXL];

    string input, word, newword;
    vector<string> breakup;
    vector<unsigned int> breakupLen;
    vector<unsigned int> breakupCtr;

    int theend;
    
    unsigned long perms, valids;

    cin>>L>>D>>N;
    dic.clear();
    
    for(unsigned int i=0; i<L; i++)
        dicbag[i].clear();

    for(unsigned int i=0; i<D; i++)
    {
        cin>>word;
        dic.insert(word);

        for(unsigned int j=0; j<word.length(); j++)
            if(dicbag[j].find(word[j]) == dicbag[j].end())
                dicbag[j].insert(word[j]);
    }
    
    for(unsigned int mycase=1; mycase<=N; mycase++)
    {
        cin>>input;
        breakup.clear();
        breakupLen.clear();
        breakupCtr.clear();
        perms = 1;
        for(unsigned int i=0; i<input.length();)
        {
            if(input[i]!='(')
            {
                word = input.substr(i, 1);

                if(dicbag[breakup.size()].find(word[0]) == dicbag[breakup.size()].end())
                {
                    perms *= 0;
                    break;
                }
                //perms *= 1;

                breakup.push_back(word);
                breakupLen.push_back(1);
                breakupCtr.push_back(0);

                i++;
            }
            else
            {
                theend = input.find_first_of(')', i+1);
                word = input.substr(i+1, theend-i-1);
                newword = "";

                for(string::iterator letter=word.begin(); letter != word.end(); letter++) // unsigned int j=0; j<word.length(); j++)
                {
                    if(dicbag[breakup.size()].find(*letter) != dicbag[breakup.size()].end())
                        newword.append(&(*letter), 1);
                }

                perms *= newword.length();
                if(perms == 0)
                    break;

                breakup.push_back(newword);
                breakupLen.push_back(newword.length());
                breakupCtr.push_back(0);

                i = theend+1;
            }
        }

        /*cout<<input<<endl;
        for(unsigned int i=0; i<breakup.size(); i++)
            cout<<'['<<breakup[i]<<']';
        cout<<endl;
        cout<<"Compressed Permutations: "<<perms<<endl;*/

        valids = 0;

        if(perms > 0)
            valids=numValids(dic, breakup, "");

        /*for(unsigned int perm=0; perm<perms; perm++)
        {
            word = "";
            for(unsigned int i=0; i<breakup.size(); i++)
                word.append(&(breakup[i][breakupCtr[i]]), 1);

            //cout<<word<<endl;
            if(dic.find(word) != dic.end())
            {
                valids++;
                //cout<<"*"<<endl;
            }

            for(unsigned int j=0; j<breakup.size(); j++)
            {
                breakupCtr[j]++;
                if(breakupCtr[j]==breakupLen[j])
                    breakupCtr[j]=0;
                else
                    break;
            }
        }*/
        
        cout<<"Case #"<<mycase<<": "<<valids<<endl;
    }

    //system("pause");
    return 0;
}