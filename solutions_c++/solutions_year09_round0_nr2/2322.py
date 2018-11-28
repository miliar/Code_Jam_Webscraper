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
typedef vector<VI> VVI;

typedef vector<char> VC;
typedef vector<VC> VVC;


struct Casei
{
	VVI ce;
	int He,Wi;
	int nr;
};
struct Caseo
{
	VVC ce;
	int He,Wi;
	int nr;
};
vector<Casei> GetInput(const char* filename);
void WriteOutput(const char* filename,vector<Caseo> out);

struct Cell
{
	Cell():n(0),hei(-1),c('0'){}
	char c;
	Cell* n;
	int hei;
	char Get()
	{
		if(c!='0') return c;
		if(n)return n->Get();
		return c;
	}
	void Set(char ch)
	{
		c = ch;
		if(n) n->Set(ch);
	}
	
};
typedef vector<Cell> VCE;
typedef vector<VCE> VVCE;

class ProcessCase
{
public:
	void operator()(Casei& e)
	{
		Caseo o;
		o.He = e.He;
		o.Wi = e.Wi;
		o.nr = e.nr;

		VVCE cells(e.He,VCE(e.Wi,Cell()));
		o.ce = VVC(o.He,VC(e.Wi,'0'));
		
		REP(r,e.He) 
		{
			REP(c,e.Wi)
			{
				cells[r][c].hei = e.ce[r][c];
				
			}
		}
		REP(r,e.He) 
		{
			REP(c,e.Wi)
			{
				Cell* m = NULL;
				int min = cells[r][c].hei;
				if(r-1>=0)
				{
					if(cells[r-1][c].hei<min)
					{	
						m = &cells[r-1][c]; 
						min = cells[r-1][c].hei;
					}
				}
				if(c-1>=0)
				{
					if(cells[r][c-1].hei<min)
					{	
						m = &cells[r][c-1]; 
						min = cells[r][c-1].hei;
					}
				}
				if(c+1<e.Wi)
				{
					if(cells[r][c+1].hei<min)
					{	
						m = &cells[r][c+1];
						min = cells[r][c+1].hei;
					}
				}
				if(r+1<e.He)
				{
					if(cells[r+1][c].hei<min)
					{	
						m = &cells[r+1][c]; 
						min = cells[r+1][c].hei;
					}
				}		

				cells[r][c].n = m;
			}
		}
		char ch = 'a';
		REP(r,e.He) 
		{
			REP(c,e.Wi)
			{
				if(cells[r][c].Get()=='0')
				{
					cells[r][c].Set(ch);
					++ch;
				}
			}
		}
		REP(r,e.He) 
		{
			REP(c,e.Wi)
			{
				//cells[r][c].Set(cells[r][c].Get());
				o.ce[r][c] = cells[r][c].Get();
			}
		}

		out.push_back(o);
	}
	vector<Caseo> go(){return out;}
private:
	vector<Caseo> out;
};

void main()
{
	vector<Casei> cases = GetInput("B-large.in");

	vector<Caseo> ocases = for_each(cases.begin(),cases.end(),ProcessCase()).go();

	WriteOutput("ws-large.out",ocases);
}

class Writer
{
public:
	Writer():m_count(1){}
	void operator()(Caseo out)
	{
		stringstream buffer;
		buffer<<"Case #"<<m_count<<":\n";

		REP(r,out.He) 
		{
			REP(c,out.Wi)
			{
				buffer<<out.ce[r][c];
				if(c<out.Wi-1)
					buffer<<" ";
			}
			buffer<<endl;
		}
		
		m_out+= buffer.str();
		++m_count;
	}
	string GetOutput(){return m_out;}
private:
	string m_out;
	int m_count;
};
void WriteOutput(const char* filename,vector<Caseo> out)
{
	string output = for_each(out.begin(),out.end(),Writer()).GetOutput();
	ofstream myfile;
	myfile.open (filename);
	myfile << output;
	myfile.close();
}


vector<Casei> GetInput(const char* filename)
{
	ifstream file;
	file.open(filename);


	string sLine;
	getline(file, sLine);
	int nrC;
	stringstream buffer;
	buffer<<sLine;
	buffer>>nrC;

	vector<Casei> cases;
	int nr=0;
	REP(i,nrC)
	{
		Casei ca;

		getline(file, sLine);

		stringstream buffer;
		buffer<<sLine;
		buffer>>ca.He>>ca.Wi;

		REP(r,ca.He) 
		{
			getline(file, sLine);
			stringstream buff;
			VI row;
			buff<<sLine;
			REP(c,ca.Wi)
			{
				int cel;
				buff>>cel;
				row.push_back(cel);
			}
			ca.ce.push_back(row);
		}
		ca.nr = ++nr;
		cases.push_back(ca);
	}	

	return cases;
}