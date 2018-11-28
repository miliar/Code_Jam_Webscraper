// Problem A. Diamond Inheritance.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
using namespace std;

struct Node
{
	vector<Node*> adjNodes;
};

int main()
{
	ifstream in("Large.in");
	ofstream out("Ldata.txt");
	vector<Node> Graph;
	vector<Node*> Aux;
	map<Node*,int> Included;
	int T,N,M,aux;
	bool found;
	in>>T;
	for(int t=1;t<=T;++t)
	{
		Graph.clear();
		in>>N;
		Graph.resize(N);
		
		for(int n=0;n<N;++n)
		{
			in>>M;
			for(int m=0;m<M;++m)
			{
				in>>aux;
				Graph[aux-1].adjNodes.push_back(&Graph[n]);
			}
		}
		
		found=false;
		for(int n=0;n<N&&!found;++n)
		{
			Included.clear();
			Aux=Graph[n].adjNodes;
			for(int i=0;i<Aux.size();++i)
			{
				if(Included[Aux[i]]++)
				{
					found=true;
					break;
				}
				for(int j=0;j<Aux[i]->adjNodes.size();++j)
				{
					Aux.push_back(Aux[i]->adjNodes[j]);
				}
			}
		}
		
		out<<"Case #"<<t<<": "<<(found?"Yes":"No")<<'\n';
	}
	return 0;
}