#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <set>
using namespace std;

set<string> fset;

ifstream fin("A-large.in");
ofstream fout("output.txt");

struct node
{
	double p;
	string feature;
	node *left;
	node *right;
}*root=NULL;

void readtree(node *&p)
{
	p=new node();
	p->left=NULL;
	p->right=NULL;
	while(fin.peek()!='(') fin.ignore();
	fin.ignore();
	while(isspace(fin.peek())) fin.ignore();
	char temp[20];
	int pos=0;
	while(!isspace(temp[pos]=fin.peek()) && temp[pos]!=')')
	{
		++pos;
		fin.ignore();
	}
	temp[pos]='\0';
	sscanf(temp,"%lf",&p->p);
	while(isspace(fin.peek())) fin.ignore();
	if(fin.peek()!=')')
	{
		char temp[20];
		int pos=0;
		while(!isspace(temp[pos]=fin.peek()))
		{
			++pos;
			fin.ignore();
		}
		temp[pos]='\0';
		p->feature=temp;
		readtree(p->left);
		readtree(p->right);
		while(isspace(fin.peek())) fin.ignore();
	}
	fin.ignore();
}

double work(double pr,node *&p)
{
	if(p==NULL) return pr;
	pr*=p->p;
	if(fset.find(p->feature)!=fset.end()) return work(pr,p->left);
	return work(pr,p->right);
}

void destroy(node *&p)
{
	if(p==NULL) return;
	destroy(p->left);
	destroy(p->right);
	delete p;
	p=NULL;
}

int main()
{
	int t;
	fin>>t;
	for(int i=0;i<t;++i)
	{
		fout<<"Case #"<<i+1<<":"<<endl;
		int l;
		fin>>l;
		readtree(root);
		int a;
		fin>>a;
		for(int j=0;j<a;++j)
		{
			string temp;
			fin>>temp;
			fset.clear();
			int n;
			fin>>n;
			for(int k=0;k<n;++k)
			{
				fin>>temp;
				fset.insert(temp);
			}
			fout.setf(ios::fixed);
			fout.precision(7);
			fout<<work(1,root)<<endl;
		}
		destroy(root);
	}
	return 0;
}
