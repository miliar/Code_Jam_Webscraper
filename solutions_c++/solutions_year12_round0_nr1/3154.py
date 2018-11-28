#include <iostream>
#include <map>
#include <vector>
using namespace  std;

map<char,char> tr;

void init()
{
	vector<string> in, out;
	in.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	in.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	in.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
	in.push_back("y qee");
	
	out.push_back("our language is impossible to understand");
	out.push_back("there are twenty six factorial possibilities");
	out.push_back("so it is okay if you want to just give up");
	out.push_back("a zoo");
	
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<in[i].size(); j++)
		{
			tr[in[i][j]]=out[i][j];
		}
	}
	tr['z']='q';
}

int main (int argc, char * const argv[]) {
    init();
	int T;
	cin >> T;
	string s;
	getline(cin,s);
	for(int i=0; i<T;i++)
	{
		getline(cin, s);
		string res = s;
		for(int j=0; j<s.size();j++)
		{
			res[j]=tr[s[j]];
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
    return 0;
}
