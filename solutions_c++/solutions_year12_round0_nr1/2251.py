#include <fstream>
#include <string>
#include <sstream>
#include <map>
using namespace std;

ifstream fin("in");
ofstream fout("out");

map<char,char> trans;

void addtomap(string english, string googlerese) {
	for(int i=0; i<(int)english.size(); i++)
		trans[googlerese[i]] = english[i];
}

string translate(string g) {
	string e;
	for(int i=0; i<(int)g.size(); i++)
		if(trans.count(g[i])==0)
			e.push_back('0');
		else
			e.push_back(trans[g[i]]);
	return e;
}

void init() {
	addtomap("aoz","yeq");
	string e1="our language is impossible to understand";
	string g1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string e2="there are twenty six factorial possibilities";
	string g2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string e3="so it is okay if you want to just give up";
	string g3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	addtomap(e1,g1);
	addtomap(e2,g2);
	addtomap(e3,g3);
}

void findmiss() {
	int a[26]={0};
	char x;
	for(char ch='a'; ch<='z'; ch++)
		if(trans.count(ch)>0)
			a[(int)(trans[ch]-'a')]++;
		else
			x=ch;
	for(int i=0; i<26; i++)
		if(a[i]==0)
			trans[x]=(char)('a'+i);
}

int main() {
	int T; fin>>T;
	init();
	findmiss();
	string junk; getline(fin,junk);
	for(int t=1; t<=T; t++) {
		string g; getline(fin,g);
		fout << "Case #" << t << ": " << translate(g) << endl;
	}
	return 0;
}
