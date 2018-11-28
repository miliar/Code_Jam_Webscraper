#include<iostream>
#include<string>
#include<vector>
#include<fstream>
using namespace std;
struct Node
{
	string Name;
	double Weight;
	Node *Left, *Right;
	~Node()
	{
		if(Left)
			delete Left;
		if(Right)
			delete Right;
	}
};
ifstream cin;
Node *Read()
{
	char c;
	::cin>>c;
	Node *N = new Node();
	::cin>>N->Weight;
	N->Left = NULL;
	N->Right = NULL;
	N->Name = "";
	char S;
	::cin>>S;
	if(S==')')
		return N;
	c=::cin.peek();
	string ss="";
	if(c>='a' && c<='z' || c>='A' && c<='Z')
		::cin>>ss;
	N->Name = S+ss;
	N->Left = Read();
	N->Right = Read();
	::cin>>c;
	return N;
}
double Prob(vector<string> Features,Node *Tree)
{
	if(Tree->Name == "")
		return Tree->Weight;
	for(int i=0;i<Features.size();i++)
		if(Tree->Name == Features[i])
			return Tree->Weight * Prob(Features,Tree->Left);
	return Tree->Weight * Prob(Features,Tree->Right);
}
int main()
{
	::cin.open("d:\\codejam.in");
	ofstream cout("d:\\codejam.out");
	int N;
	::cin>>N;
	for(int Case = 1;Case<=N;Case++)
	{
		int L;
		::cin>>L;
		Node * Tree = Read();
		string name;
		cout<<"Case #"<<Case<<":"<<endl;
		int K;
		::cin>>K;
		for(int i=0;i<K;i++)
		{
			vector<string> Features;
			::cin>>name;
			int n;
			::cin>>n;
			for(int i=0;i<n;i++)
			{
				::cin>>name;
				Features.push_back(name);
			}
				cout<<Prob(Features,Tree)<<endl;
			
		}
		delete Tree;
	}
}