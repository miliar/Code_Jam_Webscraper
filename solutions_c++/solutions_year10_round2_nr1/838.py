#include<iostream>
#include<vector>
#include<map>
using namespace std;


struct node
{

	map<string, node *> m;

};

int insert(node * root, string g)
{	
	//cout << "g is " << g << endl;
	if(g.size() == 0)
		return 0;
	int x = g.find('/');
	string h;
	if( x == string::npos)
		h = g;
	else
		 h = g.substr(0,x);
	int y = 0;
	if(root->m.count(h) == 0)
	{
		node * n = new node;
		root->m[h] = n;
		y = 1;
	}
	if(x == string::npos)
		return y;
	return y + insert(root->m[h], g.substr(x+1));
	



}

int main()
{

	int T;
	cin >> T;
	for(int t = 0; t < T;t++)
	{
		int N, M;
		cin >> N >> M;
		node * root = new node;
		for(int i = 0; i < N;i++)
		{
			string g;
			cin >> g;
			insert(root, g.substr(1));
		}
		int total = 0;
		for(int i = 0; i < M;i++)
		{
			string g;
			cin >> g;
			total += insert(root, g.substr(1));
		}
		cout << "Case #" << t+1 << ": " << total << endl;
		
		
	}

}
