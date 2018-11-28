#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <map>
#include <sstream>

//# define INP cin
//# define OUT cout

using namespace std;

typedef long long int64;
typedef long double ld;

void epura(string& s)
{
	for(int i=0;i<s.size();i++)
		if(s[i]=='/')
			s[i]=' ';
	return;
}

int main (int argc, char * const argv[]) {
    
	fstream INP("input.txt", fstream::in);
	fstream OUT("output.txt",fstream::out);
	
	int T;
	
	INP>>T;
	
	for(int cont=1;cont<=T;cont++)
	{
		set< pair< int,vector<string> > > archipre;
		set< pair< int,vector<string> > > archipost;
		
		int N,M;
		INP>>N>>M;

		for(int i=0;i<N;i++)
		{
			string str;
			INP>>str;
			epura(str);
			stringstream q;
			q<<str;
			vector<string> pezzogra;
			string pr;
			while(q>>pr)
				pezzogra.push_back(pr);
			
			for(int j=0;j<pezzogra.size();j++)
			{
				vector<string> aus;
				for(int k=0;k<=j;k++)
					aus.push_back(pezzogra[k]);
				archipre.insert(make_pair(j, aus));
			
			}
		}
		
		for(int i=0;i<M;i++)
		{
			
			string str;
			INP>>str;
			epura(str);
			stringstream q;
			q<<str;
			vector<string> pezzogra;
			string pr;
			while(q>>pr)
				pezzogra.push_back(pr);
			
			for(int j=0;j<pezzogra.size();j++)
			{
				vector<string> aus;
				for(int k=0;k<=j;k++)
					aus.push_back(pezzogra[k]);
				archipost.insert(make_pair(j, aus));
			}
		}
		vector< pair<int, vector<string> > > diff;
		set_difference(archipost.begin(),archipost.end(),archipre.begin(),archipre.end(),back_inserter(diff));
		
				
		OUT<<"Case #"<<cont<<": "<<diff.size()<<endl;	
	}
	
	
    return 0;
}
