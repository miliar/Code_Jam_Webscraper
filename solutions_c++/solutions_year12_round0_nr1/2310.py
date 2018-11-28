#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

ifstream cin ("A-small-attempt9.in");
ofstream cout ("Prob1");

string s1 ="our language is impossible to understandaozq";
string s2 = "there are twenty six factorial possibilities";
string s3 = "so it is okay if you want to just give up";
string r1 = "ejp mysljylc kd kxveddknmc re jsicpdrysiyeqz";
string r2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string r3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";


 
 
void fillm(string a, string b, map <char,char> &mp){
	for(int i=0;i<a.size();i++){
		mp[char(a[i])] = (char)b[i];
	}
}

int main(){
	map <char, char> mpc;	
	fillm(r1,s1,mpc);
	fillm(r2,s2,mpc);
	fillm(r3,s3,mpc);

	int T;
	cin >> T;
	string s;
	ws(cin);
	for(int i=0;i<T;i++){
		getline(cin,s);
		for(int j=0;j<s.size();j++){
			char z = mpc[s[j]];
			s[j]=z;
		}
		cout <<"Case #" << i+1 << ": "<< s << endl;
	}
	return 0;
}
 