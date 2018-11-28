#include<vector>
#include<string>
#include<iostream>
#include<fstream>
using namespace std;

vector<string> WordParts;
vector<string> dict;
//fill prev indices completely 
/* D-> Words in the language
   L-> Lowercase letters in a word
   N-> number of words given
   */
void ExtractWordParts(string wrd)
{
	WordParts.clear();
	string str;
	for(int i=0;i<wrd.size();i++)
	{
		if(wrd[i]=='(')
		{
			str = "";
			++i;
			while(wrd[i]!=')')
			{
				str += wrd[i];
				i++;
			}
			WordParts.push_back(str);
		}
		else
		{
			string tstr;
			tstr+=wrd[i];
			WordParts.push_back(tstr);
		}
	}
}

int ret = 0;
int L;
void solve(vector<int> PrevIndices,int d=0)
{
	/*cout<<"\nd="<<d<<" ch="<<ch<<" PrevIndices = ";
	for(int k=0;k<PrevIndices.size();k++)
		cout<<PrevIndices[k]<<",";*/
	
	if(PrevIndices.empty()) return;
	
	if(d == L) 
	{
		//cout<<"\nreturning 1";
	    ++ret;
		return;
	}
	for(int i=0;i<WordParts[d].size();i++)
	{
		vector<int> NextIndices;
		for(int j=0;j<PrevIndices.size();j++)
		{
			if(dict[PrevIndices[j]][d] == WordParts[d][i])
				NextIndices.push_back(PrevIndices[j]);
		}
		solve(NextIndices,d + 1);
		//cout<<ch<<WordParts[d][i];
	}
}
void main()
{
	int D,N,i;
	ifstream in("c:\\GCJ-2009\\A-small-attempt0.in");
	ofstream out("c:\\GCJ-2009\\A-small-attempt0.out");
	in>>L>>D>>N;
	string temp;
	dict.clear();
	vector<int> ind;
	for(i=0;i<D;i++)
	{
		in>>temp;
		dict.push_back(temp);
		ind.push_back(i);
	}

	string wrd;
	for(i=0;i<N;i++)
	{
		in>>wrd;
		ExtractWordParts(wrd);
		ret = 0;
		solve(ind);
		out<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	in.close();
	out.close();
	system("pause");
}
