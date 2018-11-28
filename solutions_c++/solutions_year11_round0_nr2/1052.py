#include <map>
#include <set>
#include <iostream>
#include <fstream>
#include <string>

#include <stdlib.h>

#define DERR(x)   \
{  \
    cout << "error: " << (x) << endl; \
    exit(1); \
}

using namespace std;

static int debug = 0;

class elist_t
{
    private:
	map<string,string> combines;
        set<string> opposes;
	char data[100];
	int size;

	void checkcombine()
	{
	    if(size >= 2)
	    {
		char c1 = data[size-1];
	        char c2 = data[size-2];
		char s[3];
		map<string,string>::iterator it;

		s[0] = c1;
		s[1] = c2;
		s[2] = '\0';
	       	it = combines.find(string(s));
		if(it != combines.end())
		{
		    data[size-2] = (*it).second.c_str()[0];
		    size--;
		}

	    }
	}

	void checkoppose()
	{
	    set<string>::iterator it;

	    if(size<2) return;

	    char c1 = data[size-1];
	    for(int j=0; j<size-1; j++)
	    {
		char c0 = data[j];
	        char x[3];
	        x[0] = c0;
	        x[1] = c1;
	        x[2] = '\0';
	        string s(x);
	        it = opposes.find(s);
	        if(it != opposes.end())
	        {
		    size = 0;
		    return;
		}

	    }
	}


    public:

	elist_t()
	{
	    size = 0;
	}

	void addchar(char c)
	{
	    data[size++] = c;
	    if(size>100) DERR("queue blow up");
	    checkcombine();
	    checkoppose();
	}

	void addcombine(string& s)
	{
	    const char* p = s.c_str();
	    char x[3], y[2];
	    x[2] = '\0';
	    x[0] = p[0];
	    x[1] = p[1];
	    y[1] = '\0';
	    y[0] = p[2];
	    combines.insert(pair<string,string>(x,y));
	    if(debug) cout << x << "->" << y << endl;
	    x[0] = p[1];
	    x[1] = p[0];
	    combines.insert(pair<string,string>(x,y));
	    if(debug) cout << x << "->" << y << endl;
	}

	void addoppose(string& s)
	{
	    string s0 = s.substr(0,1);
	    string s1 = s.substr(1,1);
	    opposes.insert(s);
	    opposes.insert(s1 + s0);
	    if(debug) cout << s0 << "<->" << s1 << endl;
	}

	void print()
	{
	    cout << "[";
	    for(int i=0; i<size; i++)
	    {
		cout << data[i];
		if(i<size-1) cout << ", ";
	    }
	    cout << "]";
	}
	void clear()
	{
            size=0;
	    combines.clear();
	    opposes.clear();
	}
};


int main(int argc, char* argv[])
{
    elist_t elist;
    int T, C, D, N;
    string tmp;

    if(argc==1) DERR("no input file specified");

    ifstream infile(argv[1], ifstream::in);
    if(infile.fail()) DERR("cannot open file");
    infile >> T;
    if(debug) cout << "T=" << T << endl;
    for(int k=0; k<T; k++)
    {
	elist.clear();
	infile >> C;
	for(int j=0; j<C; j++)
	{
	    infile >> tmp;
	    elist.addcombine(tmp);
	}
	infile >> D;
	for(int j=0; j<D; j++)
	{
	    infile >> tmp;
	    elist.addoppose(tmp);
	}

	infile >> N;
	infile >> tmp;
        const char* p = tmp.c_str();
	for(int j=0; j<N; j++)
	{
	    elist.addchar(p[j]);
	    if(debug)
	    {	
		elist.print();
		cout << endl;
	    }
	}

	cout << "Case #" << (k+1) << ": ";
	elist.print();
	cout << endl;
    }

    return 0;
}



