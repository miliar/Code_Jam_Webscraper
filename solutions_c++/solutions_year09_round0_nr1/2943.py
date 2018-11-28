#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
vector< string > dict,msg;
string str;
vector < string > poss;
vector<char> emp_char_arr;
int ans[100];
int f ( int pos) {
	
}
bool present ( char c , int index ) 	{
	for ( int i=0; i<poss[index].size();i++) if(c==poss[index][i]) return true;
	return false; 
}
bool possi  ( string s ) 	{
	for ( int i=0; i<s.size(); i++ ) if ( !present(s[i],i))	 return false;
	return true;
}
int main()	{
	ifstream fin("A-large.in");
	int n,d,l,i,p,ans,T=1;
	string temp;
	bool bkt;
	fin>>l>>d>>n;
	dict.resize(d);
	for(i=0;i<d;i++) fin>>dict[i];
	while(n--)	{
		fin>>str;
		poss.clear();
		poss.resize(l+1);
		p=0;
		temp="";
		for ( i=0; i<str.size(); i++ )  {	
			if ( str[i]=='(')	{
				i++;
				if(temp!="") poss[p++]=temp;
				temp="";
				while ( str[i]!=')' ) { temp.push_back(str[i]); i++; }
				poss[p++]=temp;
				temp="";
			}
			else {
				temp.push_back(str[i]);
				poss[p++]=temp;
				temp="";
			}
		}
		if(temp!="") poss[p++]=temp;
		//for ( i=0; i<poss.size(); i++ ) { for ( int j=0; j<poss[i].size(); j++) cout<<poss[i][j]<<" ";  cout<<endl; }
		ans=0;
		for ( i=0; i<d; i++) if(possi(dict[i])) ans++;
		cout<<"Case #"<<T++<<": "<<ans<<endl;
	}
	return 0;
}
