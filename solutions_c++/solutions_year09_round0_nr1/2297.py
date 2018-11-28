#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>
#include <windows.h>
#include <iostream>
using namespace std;

int s2i(string s){stringstream ss(s);int i;ss>>i;return i;}
string i2s(int i){stringstream ss; ss<<i;return ss.str();}

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)

typedef vector<int> VI;
typedef vector<int>::iterator VIT;

typedef vector<string> VS;
typedef vector<string>::iterator VST;

struct Input
{
	vector<string> letters;
	int nr;
};
vector<Input> GetInput(const char* filename,vector<string>& words);
void WriteOutput(const char* filename,VI out);

vector<string> words;

class ProcessCase
{
public:
	void operator()(Input& e)
	{
		VS wor(words);
		int lett=0;
		for(VST i = e.letters.begin();e.letters.end()!=i;++i)
		{
			VS tmp;
			for(VST w = wor.begin();wor.end()!=w;++w)
			{
				if(i->find_first_of((*w)[lett]) != string::npos)
				{
					tmp.push_back(*w);
				}
			}
			wor.assign(tmp.begin(),tmp.end());
			tmp.clear();
			++lett;
		}
		out.push_back(wor.size());
	}
	VI go(){return out;}
private:
	VI out;
};


void main()
{

	vector<Input> cases = GetInput("A-large.in",words);

	VI o = for_each(cases.begin(),cases.end(),ProcessCase()).go();

	WriteOutput("small.out",o);

}

class Writer
{
public:
	Writer():m_count(1){}
	void operator()(int out)
	{
		stringstream buffer;
		buffer<<"Case #"<<m_count<<": " <<out<<endl;
		m_out+= buffer.str();
		++m_count;
	}
	string GetOutput(){return m_out;}
private:
	string m_out;
	int m_count;
};
void WriteOutput(const char* filename,VI out)
{
	string output = for_each(out.begin(),out.end(),Writer()).GetOutput();
	ofstream myfile;
	myfile.open (filename);
	myfile << output;
	myfile.close();
}



vector<Input> GetInput(const char* filename,vector<string>& words)
{
	ifstream file;
	file.open(filename);

	vector<Input> lines;
	string sLine;
	getline(file, sLine);
	int nrL,D,N;
	stringstream buffer;
	buffer<<sLine;
	buffer>>nrL>>D>>N;

	REP(i,D)
	{
		getline(file, sLine);
		words.push_back(sLine);
	}	


	int nr=0;
	REP(i,N)
	{
		getline(file, sLine);

		Input in;
		string::iterator it = sLine.begin();
		REP(j,nrL)
		{
			string str;
			if((*it) == '(')
			{
				++it;
				while(*it!=')')
				{
					str+=(*it);
					++it;
				}
				++it;
			}
			else
			{
				str+=(*it);
				++it;
			}
			in.letters.push_back(str);
		}

		++nr;
		in.nr=nr;
		lines.push_back( in );
		
	}
	return lines;
}