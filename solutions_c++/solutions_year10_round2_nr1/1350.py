#include <fstream>
#include <iostream>
#include <string.h>
using namespace std;
#include <string>
#include <vector>
typedef unsigned long long Integer;
// To customize this part
Integer Calc(Integer N,Integer M,vector<string>existing,vector<string>tobeCreate);

class Directory
{
	public:
		string name;
		Directory* parent;
		vector<Directory*> children;
		
	public:
		Directory() {name="";parent=NULL;children.clear();}
		Directory(Directory* p) {name="";parent=p;children.clear();}
		Directory(Directory* p,const string s) {name=s;parent=p;children.clear();}
		~Directory();
		Directory* getChild(string s);
		bool insertChild(string s);
};

int main(int argc,char* argv[])
{
	ifstream foo;
	char buf[0x200];
	sprintf(buf,"%s.in",argv[1]);
	foo.open(buf);
	if(foo.is_open()==false){
		cout<<"input file error!\n";
		return -1;
	}
	ofstream fout;
	sprintf(buf,"%s.out",argv[1]);
	fout.open(buf);
	int nCase=0;
	foo>>nCase;
	cout<<"Number of Case :"<<nCase+1<<endl;
	for(int i=0;i<nCase;i++){
		cout<<"***********************************"<<endl;
		cout<<"Processing: "<<i+1<<"/"<<nCase<<endl;
		int N;//existing
		int M;//to be create
		foo>>N>>M;
		vector<string> existing;
		existing.resize(N);
		vector<string> tobeCreate;
		tobeCreate.resize(M);
		for(int k=0;k<N;k++)
			foo>>existing[k];
		for(int k=0;k<M;k++)
			foo>>tobeCreate[k];
// 		for(int i=0;i<N;i++)
// 			cout<<i<<" "<<existing[i]<<endl;
// 		for(int i=0;i<M;i++)
// 			cout<<i<<" "<<tobeCreate[i]<<endl;
		int result=Calc(N,M,existing,tobeCreate);
		fout<<"Case #"<<i+1<<": "<<result<<endl;
	}
	foo.close();
	fout.close();
}

Integer Calc(Integer N,Integer M,vector<string>existing,vector<string>tobeCreate)
{
	Directory* root= new Directory(NULL,"root");
	
	for(int k=0;k<N;k++)
	{
		string local=existing[k];
		
		const char* ptr=local.c_str();
		cout<<"Original is "<<ptr<<endl;
		char buf[0x200];
		int cnt=0;
		Directory* current=root;
		for(int i=1;i<strlen(ptr);i++){
			if(ptr[i]!='/' && (i!=(strlen(ptr)-1))){
				buf[cnt]=ptr[i];
				cnt++;
			}
			else if(i==(strlen(ptr)-1))
			{
				buf[cnt]=ptr[i];
				buf[cnt+1]='\0';
// 				cout<<buf<<"===";
				string ss=buf;
				current->insertChild(ss);
				current=current->getChild(ss);
// 				cout<<"Current is "<<current->name<<endl;
				cnt=0;
			}	
			else{
				buf[cnt+1]='\0';
// 				cout<<buf<<"!!!";
				string ss=buf;
				current->insertChild(ss);
				current=current->getChild(ss);
// 				cout<<"Current is "<<current->name<<endl;
				cnt=0;
			}
			
			
		}
// 		cout<<endl;
	}
	cout<<"Read in finished!\n";
	
	int result=0;
	for(int k=0;k<M;k++)
	{
		string local=tobeCreate[k];		
		const char* ptr=local.c_str();
		cout<<"Original create is "<<ptr<<endl;
		char buf[0x200];
		int cnt=0;
		Directory* current=root;
		for(int i=1;i<strlen(ptr);i++){
			if(ptr[i]!='/' && (i!=(strlen(ptr)-1))){
				buf[cnt]=ptr[i];
				cnt++;
			}
			else if(i==(strlen(ptr)-1))
			{
				buf[cnt]=ptr[i];
				buf[cnt+1]='\0';
// 				cout<<buf<<"===";
				string ss=buf;
				bool isInsert= current->insertChild(ss);
				if(isInsert)
					result++;
				current=current->getChild(ss);
// 				cout<<"Current is "<<current->name<<endl;
				cnt=0;
			}	
			else{
				buf[cnt]='\0';
// 				cout<<buf<<"!!!";
				string ss=buf;
				bool isInsert=current->insertChild(ss);
				if(isInsert)
					result++;
				current=current->getChild(ss);
// 				cout<<"Current is "<<current->name<<endl;
				cnt=0;
			}
			
			
		}
// 		cout<<endl;
	}
	return result;
}

Directory* Directory::getChild(string s)
{
	vector<Directory*>::iterator it=children.begin();
	while(it!=children.end())
	{
		if( (*it)->name==s)
			return *it;
		it++;
	}
	return NULL;
}

bool Directory::insertChild(string s)
{
	if(getChild(s)!=NULL)
		return false; //no insertion
	Directory* newDir=new Directory(this,s);
	children.push_back(newDir);
	return true; //
}
Directory::~Directory()
{
vector<Directory*>::iterator it=children.begin();
	while(it!=children.end())
	{
		delete *it;
	}
}