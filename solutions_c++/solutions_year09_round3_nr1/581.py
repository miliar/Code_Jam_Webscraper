#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<fstream>
using namespace std;
#define LL long long
set <char> sym;
map <char , int> val;
void symb( string s )  	{
	for ( int i=0; i<s.size(); i++ )  sym.insert(s[i]);
}
void set_val ( string s ) 	{
	set < char> done;
	val [ s[0] ] = 1;
	done.insert( s[0]);
	int curr=0;
	for  ( int i=1 ; i<s.size(); i++  )	{
		if ( done.find(s[i])==done.end() )	{
			val[s[i]]=curr;
			done.insert(s[i]);
			if(curr==0 ) curr=2;
			else curr++;
		}
	}
}	
long long f ( string s ) 	{
	reverse ( s.begin() , s.end() );
	int base = sym.size();
	long long ans=0,p=1;
	if ( sym.size()==1 ) base=2;
	for ( int i=0; i<s.size(); i++ )  {
		ans = (LL) ans + (LL) ( (LL)val[s[i]] * (LL) p);
		p*=(LL)base;
	}
	return ans;
}
int main()	{
	int T,n,test=1;
	ifstream fin ( "inp.in" );
	ofstream fout("op.txt");
	
	fin>>T;
	string s;
	while (	T-- )  {
		fin>>s;
		val.clear();
		sym.clear();
		symb(s);
		set_val(s);
		
		fout<<"Case #"<<test++<<": "<<f(s)<<endl;
	}
		return 0;
}
