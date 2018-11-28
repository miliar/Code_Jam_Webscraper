#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Node
{
    Node* child[26];
    Node();
};

Node::Node()
{
    memset(child, NULL, sizeof(Node*)*26);
}

int main()
{
    int L, D, N;
    cin >> L >> D >> N;
    string word;
    Node root;
    for (int i=0; i<D; i++)
    {
	cin >> word;
	Node* p = &root;
	for (int j=0; j<word.size(); j++)
	{
	    if (!p->child[word[j] - 'a'])
	    {
		p->child[word[j] - 'a'] = new Node;
	    }
	    p = p->child[word[j] - 'a'];
	    //cout << word[j] << " " << p << endl;
	}
	//cout << word << endl;
    }

    string testStr;
    for (int caseId = 1; caseId <= N; caseId++)
    {
	cin >> testStr;
	int j = 0;
	vector<Node*> sum;
	sum.push_back(&root);
	for (int i=0; i<L && sum.size(); i++, j++)
	{
	    vector<Node*> temp;
	    
	    if (testStr[j] == '(')
	    {
		j++;
		while (testStr[j] != ')')
		{
		    for (int k=0; k<sum.size(); k++)
		    {
			if (sum[k]->child[testStr[j]-'a'])
			{
			    temp.push_back(sum[k]->child[testStr[j]-'a']);
			}
		    }
		    j++;
		}
		sum = temp;
	    }

	    else if (testStr[j] >= 'a' && testStr[j] <= 'z')
	    {
		for (int k=0; k<sum.size(); k++)
		{
		    if (sum[k]->child[testStr[j]-'a'])
		    {
			temp.push_back(sum[k]->child[testStr[j]-'a']);
		    }
		}
		sum = temp;
	    }
	    //cout << i << " " << sum.size() << endl;
	}
	cout << "Case #" << caseId << ": " << sum.size() << endl;
    }

    return 0;
}
