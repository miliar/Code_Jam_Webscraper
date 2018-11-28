#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

bool match(string s, vector<string> pt)
{
	if (s.length() != pt.size()) return false;
	for ( int i = 0; i < s.length(); i ++ )
	{
		int found = 0;
		for ( int j = 0; j < pt[i].length(); j ++)
			if (pt[i][j] == s[i]) found = 1;
		if ( found == 0 ) return false;
	}
	return true;
}
int main()

{
	ifstream inp("e:\\A-large.in");
	ofstream out("e:\\output.txt");

	int L,D,N;
	int i;
	inp >> L >> D >> N;
	
	vector<string> words;
	for (  i = 0; i < D; i ++ )
	{
		string s;
		inp >> s;
		words.push_back(s);
	}

	for ( i = 0; i < N; i++)
	{
		string ps;
		inp >> ps;
		vector<string> patterns;
		int p = 0;
		while ( p < ps.length())
		{
			if (ps[p] != '(') 
			{
				patterns.push_back( ps.substr(p,1) );
				p ++;
			}

			else
			{
				int p1 = p + 1;
				while (p1 < ps.length() && ps[p1] != ')' ) p1 ++;
				patterns.push_back( ps.substr(p + 1, p1 - p - 1) );
				cout<<p<<" "<<p1<<endl;
				p = p1 + 1;

			}

		}
		
		cout<<patterns.size()<<" "<<endl;
		for ( int j = 0; j < patterns.size(); j ++) cout<<patterns[j]<<" ";
		cout<<endl;
		int total = 0;
		for (  j = 0; j < D; j ++)
			if (match(words[j], patterns)) total ++;
			cout<<"Case #"<<i + 1<<": "<<total<<endl;
            out<<"Case #"<<i + 1<<": "<<total<<endl;
		
	}

  return 0;
}