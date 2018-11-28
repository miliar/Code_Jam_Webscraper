#include <cstdio>
#include <cmath>
#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

#define INFILE "1.txt"
#define OUTFILE "A-small.out"


int main()
{
	ifstream in(INFILE);
	ofstream out(OUTFILE);
	if (!in || !out)
	{
		cout << "file oo"<< endl;
		return 0;
	}


	int T,n,icase,i,re,t;
	list<int> v1,v2;
	list<int>::iterator it1,it2;
	in>>T;

    for (icase=0;icase<T;icase++)
    {
		in>>n;
		v1.clear();
		v2.clear();

		for(i=0;i<n;i++)
		{
			in>>t;
			v1.push_back(t);
		}
		for(i=0;i<n;i++)
		{
			in>>t;
		
			v2.push_back(t);
		}

		v1.sort();
		v2.sort();
		v2.reverse();
		

		re=0;
		for(it1=v1.begin(),it2=v2.begin();it1 != v1.end();it1++,it2++)
		{
			re += (*it1) *(*it2);
			
		}
		
		out<<"Case #"<<icase+1<<": "<<re<<endl;
	
    }
	

	
	in.close();
	out.close();
	return 0;
}