
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

class Problem
{
private:
	int m_N;
	multiset<long> m_set1;
	multiset<long> m_set2;
public:
       Problem(istream & is)
       {
    	   int temp;
    	   is >> m_N;
    	   for(int i = 0; i < m_N; ++i)
    	   {
    		   is >> temp;
    		   cout<<"row 1 temp = "<<temp<<endl;
    		   m_set1.insert(temp);
    	   }
    	   for(int i = 0; i < m_N; ++i)
    	   {
    		   is >> temp;
    		   cout<<"row 2 temp = "<<temp<<"size:"<<m_set2.size()<<endl;
    		   m_set2.insert(temp);
    	   }
       }
public:
      long Solve()const
      {
    	  long sum = 0;
    	  set<long>::const_iterator p_1 = m_set1.begin();
    	  set<long>::const_reverse_iterator p_2 = m_set2.rbegin();
    	  while(p_1 != m_set1.end())
    	  {
    		  sum += *p_1 * (*p_2);
    		  cout<<*p_1<<" "<<*p_2<<endl;
    		  ++p_1;
    		  ++p_2;
    	 }
    	  cout<<"sum = "<<sum<<endl;
    	  return sum;
      }
};

int main(int argc, char** argv)
{
	int type;
	cout<<"Enter 0 for Sample, 1 for small file and 2 for large file:"<<endl;
	cin >> type;

	string ifile,ofile;

	switch(type)
	{
	case 0:
		ifile = "sample.in";
		ofile = "sample.out";
		break;
	case 1:
		ifile = "A-small-attempt0.in";
		ofile = "A-small-attempt0.out";
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
    for(int i = 1; i <= nCase ; ++i) os << "Case #" << i << ": " << Problem(is).Solve() <<endl;
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
