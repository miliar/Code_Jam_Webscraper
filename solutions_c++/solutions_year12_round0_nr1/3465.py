#include<iostream>
#include<fstream>
#include<cassert>
#include<cstring>

using namespace std;

#define REP(i,a,b) for(int i=a;i<b;++i)

int main(int argc, char *argv[])
{

	if(argc!=3) return -1;
	
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	char trans[26]={'y','h','e','s','o','c','v','x','d','u'
				   ,'i','g','l','b','k','r','z','t','n','w'
				   ,'j','p','f','m','a','q'};

	int T;
	string in;
	fin>>T;
	getline(fin,in);
	REP(i,0,T)
	{
		getline(fin,in);
		REP(j,0,in.size())
			if(in[j]-'a'>=0 && in[j]-'a'<26)
				in[j]=trans[ in[j]-'a' ];
			else
				assert(in[j]==' ');
		cout<<"Case #"<<i+1<<": "<<in<<endl;
		fout<<"Case #"<<i+1<<": "<<in<<endl;
	}

	return 0;
}
