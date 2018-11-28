#include <iostream>
#include <map>
#include <string>
using namespace std;
class test;

class test
{
public:
	string name;
	map<string,test *>st;
public:
	test(string as)
	{
		name=as;
	}
	test()
	{

	}
	~test()
	{
		map<string,test *>::iterator it=st.begin();
		for(it;it!=st.end();++it)
		{
			delete (*it).second;
		}
	}
};

int processString(string temp,test &root);
int main()
{

	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.in.txt.txt","w",stdout);

	char buf[500];

	int T;
	cin>>T;
	int caseNow=0;
	while(T-->0)
	{
		test root;
		caseNow++;
		int N,M;
		cin>>N>>M;
		int protime=0;
		for(int i=0;i<N;++i)
		{
			string temp;
			cin>>buf;
			temp=buf;
			processString(temp,root);
		}
		for(i=0;i<M;++i)
		{
			string temp;
			cin>>buf;
			temp=buf;
			protime+=processString(temp,root);
		}
		cout<<"Case #"<<caseNow<<": "<<protime<<endl;
	}
}
int processString(string temp,test &root)
{
	int processtime=0;
	test *a2=&root;
	temp=temp.substr(1);
	int a1=0;
	while (temp.size()>0)
	{
		string temp2;
		a1=temp.find('/');
		if(a1>=temp.size()||a1<0)
		{
			temp2=temp;
			temp="";
		}
		else
		{
		 temp2=temp.substr(0,a1);
		 temp=temp.substr(a1+1);
		}

		test* tempt=new test(temp2);

		if(a2->st.find(temp2)!=a2->st.end())
		{
			a2=a2->st[temp2];
			delete tempt;
		}		
		else
		{
			a2->st[temp2]=tempt;
			a2=tempt;
			processtime++;
		}
	
	}

	return processtime;

}