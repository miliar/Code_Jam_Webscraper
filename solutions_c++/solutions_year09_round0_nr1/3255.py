#include <fstream>
#include <string>
#include <vector>

using namespace std;

ifstream fin("A-small.in");
ofstream fout("A-small.out");

vector<string>words;
vector<vector<char>>curword;
int l,d,n;

vector<vector<char>>parse(string s)
{
	int cpos=0;
	int i;
	bool open=false;
	vector<vector<char>>res;
	res.resize(l);
	vector<char>curletter;
	for(i=0;i<l;i++)
	{
		while(cpos<=s.size())
		{
			if(s[cpos]=='(')open=true;
			else if(s[cpos]==')')
			{
				open=false;
				res[i]=curletter;
				cpos++;
				break;
			}
			else 
			{
				curletter.push_back(s[cpos]);
				if(!open)
				{
					res[i]=curletter;
					cpos++;
					break;
				}
			}
			cpos++;
		}
		curletter.clear();
	}
	return res;
}

bool check_letter(int letindex,char letter)
{
	int i;
	for(i=0;i<curword[letindex].size();i++)
	{
		if(curword[letindex][i]==letter)
			return true;
	}
	return false;
}

bool can(string word)
{
	int i;
	for(i=0;i<curword.size();i++)
	{
		if(!check_letter(i,word[i]))
			return false;
	}
	return true;
}

int find_()
{
	int i,res=0;
	for(i=0;i<words.size();i++)
	{
		if(can(words[i]))
			res++;
	}
	return res;
}

int main()
{
	int i,res;
	string s;
	fin>>l>>d>>n;
	words.resize(d);
	for(i=0;i<d;i++)fin>>words[i];
	for(i=0;i<n;i++)
	{
		fin>>s;
		curword=parse(s);
		res=find_();
		fout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}