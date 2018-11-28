#include<iostream>
#include<vector>
#include<queue>
using namespace std;

struct node
{
	int count;
	node * arr[128];
	
	node()
	{
		memset(arr,0,sizeof(arr));
		count = 0;
	}
		
};

void insertWord(node * root, string g, int pos)
{
	if(pos == g.size()-1)
	{
		root->count++;
		return;
	}
	
	if(root->arr[g[pos]] == 0)
	{
		node * t = new node;
		root->arr[g[pos]] = t;
		insertWord(t,g,pos+1);
	}
	else
	{
		insertWord(root->arr[g[pos]],g, pos+1);
	}
	
	
}

int  countTotalWords(node * root)
{
	int x = root->count;
	for(int i = 'a'; i <= 'z';i++)
	{
		if(root->arr[i] != 0)
			x += countTotalWords(root->arr[i]);
	}
	return x;
}


int main()
{
	node  root;	
	int L, D, N;
	cin >> L >> D >> N;
	vector<string> dict;
	
	for(int i = 0; i < D;i++)
	{
		string g;
		cin >> g;
		dict.push_back(g);
		//insertWord(&root, g,0);
	}
	//cout << countTotalWords(&root) << endl;
	
	vector<string> words;
	
	for(int i = 0; i < N;i++)
	{
		vector<bool> used(dict.size(),true);
		int numWords = 0;
		string g;
		cin >> g;
		//cout << "g is " << g << endl;
		//vector<node *> roots;
		//roots.push_back(&root);
		int pos = 0;
		for(int j = 0; j < g.size();j++)
		{
			string test;
			if(g[j] == '(')
			{
				j++;
				while(g[j] != ')')
				{
					test.push_back(g[j]);
					j++;
				}
			}
			else
				test.push_back(g[j]);
				
			//cout << "test is " << test << endl;	
			for(int k = 0; k < dict.size();k++)
			{
				if(used[k] == false)
					continue;
				
				if(test.find(dict[k][pos],0) == -1)
				{
					used[k] = false;
				}
			}
			pos++;
		}
		
		for(int k = 0; k < used.size();k++)
		{
			if(used[k] == true)
				numWords++;
		}
			
			/*vector<node *> nextRoots;
			cout << "test is " << test << endl;
			for(int k = 0; k < test.size();k++)
			{
				for(int z = 0; z < roots.size();z++)
				{
					if( roots[z]->arr[ test[k] ] != 0)
					{
						
						nextRoots.push_back(roots[z]->arr[test[k]]);
					}
				}
			}
			
			for(int z = 0; z < nextRoots.size();z++)
			{
				numWords += nextRoots[z]->count;
			}
			roots.clear();
			roots = nextRoots;*/
		
		cout << "Case #" << (i+1) << ": " << numWords << endl;	
			
	}
	
	
}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	