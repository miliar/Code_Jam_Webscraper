#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stdio.h>
#include <set>
using namespace std;


int animaln;
set<string> animal[105];
string s;
int nowpos;

string getToken()
{
	int curpos = nowpos;
	int ns=0;
	for( int i=curpos; i<s.length(); i++ ) {
		if( s[i]!=' ' ) {
			ns = i; break;
		}
	}

	string re="";
	for( int i=ns; i<s.length(); i++ ) {
		if( s[i]=='(' || s[i]==')') {
			if( re!="" ) {
				nowpos = i;
				break;
			}
			else {
				re = s[i]; 
				nowpos = i+1;
				break;
			}
		}
		if( s[i]!=' ') {
			re += s[i];
		}
		if( s[i]==' ' ) {
			nowpos=i;
			break;
		}
	}

	return re;
}

void process(int animalidx)
{

	double prob = 1.0;
	int len = s.length();
	int startpos=-1;
	for(int i=0; i<len; i++ ) {
		if( s[i]=='(' ) {
			startpos = i+1;
			break;
		}
	}

	nowpos = startpos;
	string t;
	double nowp=1.0;
	while(true) {
		t = getToken();
		if( t[0]>='0' && t[0]<='9' ) {
			sscanf(t.c_str(), "%lf", &nowp);
			prob *= nowp;
		}
		else if( t[0]>='a' && t[0]<='z' ) {
			if( animal[animalidx].find(t) != animal[animalidx].end() ) {
				getToken();
			}
			else {
				int level =0;
				while(true) {
					string temp = getToken();
					if( temp == "(" ) level++;
					if( temp == ")" ) level--;
					if( level == 0 ) break;
				}
				getToken();
			}
		}
		else if( t[0] == ')' ) {
			break;
		}
	}

	printf("%.7lf\n", prob);
}

int main()
{
	freopen("A-large.in", "rt", stdin );
	freopen("A.out", "wt", stdout );

	int n;
	cin>>n;
	char ins_char[100];
	string ins;
	for( int i=0; i<n; i++ ) {
		int l;
		cin>>l;
		cin.getline(ins_char ,100);
		s="";
		for( int j=0; j<l; j++ ) {
			cin.getline(ins_char ,100);
			s = s+ins_char;
		}

		cin>>animaln;
		for( int j=0; j<animaln; j++ ) {
			animal[j].clear();
			string aname;
			cin>>aname;
			int afn;
			cin>>afn;
			for( int k=0; k<afn; k++ ) {
				string af;
				cin>>af;
				animal[j].insert(af);
			}
		}


		cout<<"Case #"<<i+1<<": "<<endl;
		for( int j=0; j<animaln; j++ ) {
			process(j);
		}
	}
	return 0;
}