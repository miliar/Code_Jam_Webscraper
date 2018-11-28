#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <assert.h>

using namespace std;

#define CLEAR(x,with) memset(x,with,sizeof(x))  
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

struct node 
{ 
	double prob; 
	string name;
	int left; 
	int right;
	int top;
}; 

int main()
{
	int N;
	string A;
	getline(cin, A);
	stringstream ss1(A);
	ss1 >> N;
	for(int c=1; c<=N; c++)
	{
		int numlines;
		getline(cin, A);
		stringstream ss2(A);
		ss2 >> numlines;

		string DT = "";
		for(int i=0; i<numlines; i++)
		{
			string temp;
			getline(cin, temp);
			DT += " " + temp;
		}

		int idx = 0;
		while(DT[idx] != '(') idx++;
		int current = 0;
		node temp;
		temp.prob = 0.0;
		temp.name = "";
		temp.left = -1;
		temp.right = -1;
		temp.top = -1;
		vector<node> DTree;
		DTree.push_back(temp);
		
		for(int i=idx+1; i<(int)DT.size(); i++)
		{
			if(DT[i] == ' ') continue;
			if(DT[i] == '(')
			{
				node temp;
				temp.prob = 0.0;
				temp.name = "";
				temp.left = -1;
				temp.right = -1;
				temp.top = -1;
				DTree.push_back(temp);

				int next = (int)DTree.size()-1;
				if(DTree[current].left == -1)
					DTree[current].left = next;
				else
					DTree[current].right = next;
				DTree[next].top = current;
				current = next;
			}
			else if(DT[i] == ')')
			{
				current = DTree[current].top;
			}
			else if((DT[i] >= '0' && DT[i] <= '9') || DT[i] == '.')
			{
				double prob;
				string number = "";
				while(DT[i] != ' ' && DT[i] != ')' )
				{
					number += DT[i];
					i++;
				}
				if(DT[i] == ')') i--;
				stringstream ssnumber(number);
				ssnumber >> prob;

				DTree[current].prob = prob;
			}
			else if(DT[i] >= 'a' && DT[i] <= 'z')
			{
				string name = "";
				while(DT[i] != ' ')
				{
					name += DT[i];
					i++;
				}

				DTree[current].name = name;
			}
			else assert(false);
		}

		cout << "Case #" << c << ":" << endl;
		getline(cin, A);
		stringstream ss3(A);
		ss3 >> numlines;
		for(int i=0; i<numlines; i++)
		{
			string query;
			string name;
			int num_q;
			getline(cin, query);

			stringstream ssquery(query);
			ssquery >> name >> num_q;
			map<string, bool> queries;
			for(int j=0; j<num_q; j++)
			{
				string tempq;
				ssquery >> tempq;
				queries[tempq] = true;
			}

			double ans = 1.;
			int current = 0;
			while(true)
			{
				ans *= DTree[current].prob;
				if( queries[DTree[current].name] )
				{
					current = DTree[current].left;
				}
				else
				{
					current = DTree[current].right;
				}
				if(current == -1) break;
			}
			cout << ans << endl;
		}
	}

	return 0;
}
