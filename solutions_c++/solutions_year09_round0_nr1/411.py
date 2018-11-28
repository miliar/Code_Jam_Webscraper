#include<iostream>
#include<string>
#include<vector>
using namespace std;

vector<string> dict;
int index=0;
int L, D, N;

bool vfind(char a, vector<char> &s)
{
	for(int i=0; i<s.size(); i++)
	{
		if(s[i]==a)
			return true;
	}
	return false;
}

int main()
{
    int i,j,k;
    
    cin>>L>>D>>N;
    for(i=0; i<D; i++)
    {
	string word;
        cin>>word;
	dict.push_back(word);
    }
    sort(dict.begin(), dict.end());
    

    int token_ln[15];
    int token_ind[15];
    vector<vector<char> > tokens;
    tokens.resize(15);
    string init_word;

    for(int c=1; c<=N; c++)
    {
	    index=0;
        cin>>init_word;
        k=0;

        for(i=0; i<L; i++)
            token_ln[i]=token_ind[i]=0;

        for(i=0; i<init_word.length(); i++)
        {
	    tokens[k].clear();
            if(init_word[i]=='(')
            {
                i++;
                while(init_word[i]!=')')
                {
                    tokens[k].push_back(init_word[i]);
                    i++;
                }
            }
            else
                tokens[k].push_back(init_word[i]);
            k++;
        }

	int sum=0;

	for(i=0; i<D; i++)
	{
		for(j=0; j<L; j++)
			if(!vfind(dict[i][j], tokens[j]))
				break;
		if(j==L)
			sum++;
	}

        cout<<"Case #"<<c<<": "<<sum<<endl;
    }
}



                    

        
