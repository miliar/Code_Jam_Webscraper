#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
#define inf 1000000000
vector < string > mat;
vector < int> v;
int n;
int val ( string s ) 	{
	int ans=0,i;
	for (  i=0; i<s.size(); i++ ) if(s[i]=='1' ) ans=i;
	return ans;
}
int f(int pos )	{
	if ( pos==n-1 ) if (v[pos]<=pos ) return 0; else return inf;
	if ( v[pos]<=pos ) return f(pos+1);
	int temp,ans=inf;
	for ( int i=pos+1; i<n; i++ )	
		if ( v[i]<=pos ) {
			temp = v[i];
			v.erase ( v.begin() + i );
			v.insert ( v.begin()+pos , temp);
			temp = f ( pos+1 );
			if ( temp<inf  && temp+i-pos<ans ) ans=temp+i-pos;
			break;
		}
		return ans;
}
int main()	{
	ifstream fin ("inp.in");
	ofstream fout ("op");
	int T;int cnt=1;
	fin>>T;
	while ( T-- )	{
		fin>>n;
		mat.clear();
		mat.resize(n);
		v.clear();
		for ( int i=0; i<n; i++ ) fin>>mat[i];
		for ( int i=0; i<n; i++ ) { v.push_back(val(mat[i])); }//cout<<mat[i]<<" "<<val(mat[i])<<endl; }
		fout<<"Case #"<<cnt++<<": "<<f(0)<<endl;
	}
	return 0;
}

