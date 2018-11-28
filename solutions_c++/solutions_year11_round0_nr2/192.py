#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<map>
#include<vector>
#include<algorithm>
#include<iterator>
#include<sstream>
#include<set>
using namespace std;

typedef unsigned long long uint64;
typedef long long int64;

int main(int argc, char *argv[])
{
//readin file
	string file;
	if(argc!=2){cerr<<"0,1 or 2!"<<endl;exit(1);}
	switch(atoi(argv[1]))
	{
		case 0: file="test"; break;
		case 1: file="B-small"; break;
		case 2: file="B-large"; break;
		default: cerr<<"choose the correct file, 0(test),1(small),2(large)"<<endl;exit(1); break;
	}
	string ifilename=file+".in"; string ofilename=file+".out";
	ifstream input(ifilename.c_str());ofstream output(ofilename.c_str());

//read in number of events
	int T;
	input>>T;
	int C,D,N;

//main loop start
	for(int t=0;t<T;t++)
	{
		input>>C;
		map<string,char> Comb;
		string ss;

		map<string,char>::iterator it;
		for(int i=0;i<C;i++)
		{
			input>>ss;
			string st(ss.begin(),ss.begin()+2);
			Comb[st]=ss[2];
			st=ss[1];
			st+=ss[0];
			Comb[st]=ss[2];
		}
		input>>D;
		map<char,string> Oppo;
		map<char,string>::iterator itcc;
		for(int i=0;i<D;i++)
		{
			input>>ss;
			Oppo[ss[0]]=Oppo[ss[0]]+ss[1];
			Oppo[ss[1]]=Oppo[ss[1]]+ss[0];
		}
		input>>N;
		input>>ss;
//		cout<<ss<<endl;
		vector<char>X;
		for(int i=0;i<N;i++)
		{
			if(X.size()==0){X.push_back(ss[i]);continue;}
			//combine
			string st;
			st=X[X.size()-1];
			st+=ss[i];
			it = Comb.find(st);
			if(it!=Comb.end()){X[X.size()-1]=it->second;continue;}
			//oppose
			itcc=Oppo.find(ss[i]);
			bool cl=false;
			if(itcc!=Oppo.end())
			{
				for(int i=0;i<X.size();i++)
				{
					int where=(itcc->second).find(X[i]);
					if(where!=string::npos){cl=true;break;}
				}
			}
			if(cl){X.clear();continue;}
			X.push_back(ss[i]);
		}

		cout<<"case : "<<t+1<<endl;
		output<<"Case #"<<t+1<<": [";
		cout<<X.size()<<endl;
		if(X.size()>0){
		for(int i=0;i<(X.size()-1);i++)
		{
			output<<X[i]<<", ";
		}
		output<<X[X.size()-1]<<"]"<<endl;
		}
		else output<<"]"<<endl;
	}

	input.close();
	output.close();
	return 0;
}
