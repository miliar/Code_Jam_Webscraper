#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int dn[10];
string ins;
vector<char> str;

int comp(string a, string b ) {
	if( a.length() != b.length() ) {
		if( a.length() > b.length() ) return 1;
		if( a.length() == b.length() ) return 0;
		if( a.length() < b.length() ) return -1;
	}
	else {
		if( a>b ) return 1;
		if( a==b ) return 0;
		if( a<b ) return -1;
	}
}


void process()
{
	vector<char> nows;
	nows = str;
	next_permutation(nows.begin(), nows.end());

	string newstring = "";
	for(int i=0; i<nows.size(); i++ ) {
		newstring += nows[i];
	}

	nows = str;
	while( comp( newstring , ins) <= 0 ) {
		nows.push_back(' ');
		for(int i=nows.size()-1; i>=1 ; i-- ) {
			nows[i]=nows[i-1];
		}
		nows[0] = '0';

		next_permutation(nows.begin(), nows.end());

		newstring = "";
		for(int i=0; i<nows.size(); i++ ) {
			newstring += nows[i];
		}	
	}

	cout<<newstring<<endl;

}

int main()
{
	freopen("B-large.in", "rt", stdin);
	//freopen("B.out","wt", stdout);
	int t;
	cin>>t;
	for( int i=0; i<t; i++ ) {
		cin>>ins;


		str.clear();
		for( int j=0; j<ins.length(); j++ ) {
			dn[ ins[j]-'0' ] ++;
			str.push_back(ins[j]);
		}


		cout<<"Case #"<<i+1<<": ";
		process();
	}
	return 0;
}