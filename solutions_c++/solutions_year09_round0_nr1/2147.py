#include<iostream>
#include<vector>
#include<queue>

using namespace std;

struct node
{
	struct node *child[26];
};

void makenull(struct node *tmp)
{
	for (int i = 0; i < 26; i++) tmp->child[i] = NULL;
}

int main()
{
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> v;
	string s;
	for (int i = 0; i < d; i++) 
	{
		cin >> s;
		v.push_back(s);
	}
	struct node *head, *temp, *tmp;
	head = new node;
	makenull(head);
	for (int i = 0; i < v.size(); i++) 
	{
		temp = head;
		for (int j = 0; j < l; j++)
		{
			if (temp->child[v[i][j] - 'a'] == NULL)
			{
				tmp = new node;
				makenull(tmp);
				temp -> child[v[i][j] - 'a'] = tmp;
				temp = tmp;
			}
			else 
			{
				temp = temp -> child[v[i][j] - 'a'];
			}
		}
	}
	vector<string> w;
	for (int i = 0; i < n; i++)
	{
		string s1, s2;
		cin >> s1;
		for (int j = 0; j < s1.size(); j++) 
		{
			if (s1[j] == '(')
			{
				j++;
				while (s1[j] != ')') 
				{
					s2 += s1[j];
					j++;
				}
				w.push_back(s2);
				s2.clear();
			}
			else 
			{
				s2 += s1[j];
				w.push_back(s2);
				s2.clear();
			}
		}
		queue<node*> q;
		temp = head;
		q.push(temp);
		for (int j = 0; j < l; j++) 
		{
			int len = q.size();
			while (len--) 
			{
				temp = q.front();
				q.pop();
				for (int k = 0; k < w[j].size(); k++)
				{
					if (temp->child[w[j][k] - 'a'] != NULL)
					{
						q.push(temp->child[w[j][k] - 'a']);
					}	
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << q.size() << endl;
		w.clear();
	}
	return 0;
}
