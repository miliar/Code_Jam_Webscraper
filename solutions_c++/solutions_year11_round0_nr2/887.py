#include <fstream>
#include <iostream>
#include <map>
//#include <fstream>

#include <vector>
#include <utility>
#include <string>
using namespace std;

ifstream in;
string res0;
///int beg = 0;
/*
void check(){
	
	ifstream out1 ("B-small.out");
	ifstream out2 ("out.txt");
	ofstream chOut ("check.out");

	for( int i=1;i<=100;i++){
		string s1,s2;
		getline( out1, s1);
		getline( out2, s2);
		if( s1==s2 )
			chOut<<"Case #"<<i<<": OK"<<endl;
		else
			chOut<<"Case #"<<i<<": --------------------------------"<<endl;
	}

}*/

char prev(int cur){
	if( cur>0 )
		return res0[ res0.length()-1 ];
	else
		return 'Z';
}

string solve(){
	
	char combo[26][26];
	bool opp[26][26];

	for( int i = 0; i < 26; i++){
		for( int j = 0; j < 26; j++){
			combo[i][j] = 0;
			opp[i][j] = false;
		}
	}

	//beg = 0;
	res0 ="";

	int c,d,n;
	in>>c;

	char a1,a2,a3;
	for( int i = 0; i < c; i++){
		in>>a1>>a2>>a3;
		combo[ a1-'A' ][ a2-'A' ] = combo[ a2-'A' ][ a1-'A' ] = a3;
	}

	in>>d;
	for( int i = 0; i < d; i++){
		in>>a1>>a2;
		opp[ a1-'A' ][ a2-'A' ] = opp[ a2-'A' ][ a1-'A' ] = true;
	}
	in>>n;

	int was[26] = {0};
	char curCh;
	char prevCh;
	bool add;

	for( int i = 0; i < n; i++){
		add = true;
		int len = res0.length();
		in>>curCh;
		prevCh = prev( len );
		if( combo[ curCh-'A' ][ prevCh-'A' ] ){
			res0[len-1] = combo[ curCh-'A' ][ prevCh-'A' ];
			was[prevCh-'A']--;
		}
		else{ 
			for( int j = 0; j < 26; j++){
				if( opp[ curCh-'A' ][ j ] && was[ j ] ){
					//beg = len;
					res0 = "";
					for( int k=0; k<26;k++)
						was[k]=0;
					add = false;
					break;
				}
			}
			if( add ){
				was[ curCh-'A' ]++;
				res0+=curCh;
			}
		}
	}

	string res = "[";
	for( int i = 0; i<res0.length(); i++){
		if( i!=0 )
			res+=", ";
		res += res0[i];
	}
	res+=']';
	
	return res;
}

int main(){
	in = ifstream("B-small.in");
	ofstream out ("B-small.out");
	int T;
	in >> T;

	for( int i = 1; i <= T; i++)
		out<<"Case #"<<i<<": "<<solve()<<endl;
	out.close();
	in.close();
	//check();
}