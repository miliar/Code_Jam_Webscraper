#include <iostream>
#include <vector>
using namespace std;

void readTokens(vector<string> &tokens, string &inp)
{
    int startp = 0;
    bool inuse=false;
    for(int i = 0; i < inp.length(); ++i)
    {
        if(inuse)
        {
            if(inp[i] == ')')
            {
                tokens.push_back(inp.substr(startp, i - startp));
                inuse=false;
            }
        }
        else
        {
            if(inp[i]== '(')
            {
                startp = i+1;
                inuse = true;
            }
            else
                tokens.push_back(inp.substr(i,1));
        }
    }
}

int main(int argc, char** argv)
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int l,d,n;
    cin>>l>>d>>n;
    vector< string > words;
    string word;
    for(int k = 0; k < d; ++k)
    {
        cin>>word;
        words.push_back(word);
    }
    for(int k = 0; k < n; ++k)
    {
        int res = 0;
        vector<string> tokens;
        cin>>word;
        readTokens(tokens, word);
        if(tokens.size()==l)
        {
            for(int i = 0; i < d; ++i)
            {
                bool isFound = true;
                for(int j = 0; (j < l) && isFound; ++j)
                    isFound = tokens[j].find(words[i][j]) != -1;
                if(isFound) res++;
            }
        }
        cout<<"Case #"<<k+1<<": "<<res<<endl;
    }

    return (0);
}
