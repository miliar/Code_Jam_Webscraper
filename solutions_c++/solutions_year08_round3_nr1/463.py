
#include <algorithm>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
typedef long long LL;
typedef long double LD;
#define FOR(j) for(int i = 0; i < (j); ++i)
#define FORS(s,j) for(int i = (s); i < (j); ++i)

class Problem
{
private:
	string m_buffer;
	int nk;
	int key;
	int c;
	vector<int> f;

public:
       Problem(istream & is)
       {
    	   is >> nk >> key >> c;
    	   f.resize(c);
    	   for(int i = 0; i < c; ++i)
    	   {
    		   is >> f[i];
    		   clog << f[i] << " ";
    	   }
    	   clog <<endl;

       }
public:
      LL Solve()
      {
    	  sort(f.begin(),f.end(),greater<int>());
    	  LL sum = 0;
    	  for(int i = 0; i < f.size(); ++i)
    	  {
    		  clog<<f[i] << " "<<(i/key+1) <<endl;
    		  sum += f[i]*(i/key+1);
    		  clog <<"sum = "<<sum<<endl;
    	  }
    	  return sum;
      }
};

int main(int argc, char** argv)
{
	int type;
	cout<<"Enter 0 for Sample, 1 for small file and 2 for large file:"<<endl;
	cin >> type;

	string ifile,ofile;
	string sub_string;

	switch(type)
	{
	case 0:
		ifile = "sample.in";
		ofile = "sample.out";
		break;
	case 1:
		cin >> sub_string;
		ifile = "A-small-attempt"+ sub_string+ ".in";
		ofile = "A-small-attempt"+ sub_string+ ".out";
		break;
	case 2:
		ifile = "A-large.in";
		ofile = "A-large.out";
		break;
	default:
		cerr<<"Invalid input."<<endl;
		return -1;
	}

    ifstream is(ifile.c_str());
    if(!is.good())
    {
    	cerr<<"Can not open output file: "<<ifile<<endl;
    	return -2;
    }
    ofstream os(ofile.c_str());
    if(!os.good())
    {
    	cerr<<"Can not open output file :  "<<ofile<<endl;
    	return -3;
    }

    clog <<"Running..."<<endl;

    is.exceptions ( ifstream::failbit | ifstream::badbit );
    os.exceptions ( ofstream::failbit);

    try
    {
        int nCase; is >> nCase; is.ignore(256,'\n');
        clog << "nCase = "<<nCase<<endl<<endl;
        for(int i = 1; i <= nCase ; ++i)
        {
        	clog<< "Processing Case #"<<i<<endl;
        	os << "Case #" << i << ": " << Problem(is).Solve() <<endl;
        	clog<< "Case #"<<i<<" solved."<<endl<<endl;
        }
    }
    catch(...)
    {
    	cerr << "Exception during I/O" <<endl;
    	os.flush();
    }

    is.close();
	os.close();

	clog <<"Completed."<<endl;

	return 0;
}
