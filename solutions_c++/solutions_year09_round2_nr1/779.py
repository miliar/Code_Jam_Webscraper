#include <iostream>
#include <cstring>
#include <set>
#define MAX_NODES 100000
using namespace std;

struct node
{
	double weight;
	string feature;
} nodes[MAX_NODES];

void readTree(int numNode)
{
	char aux;
	
	cin >> skipws >> aux;
	cin >> nodes[numNode].weight;
	cin >> skipws >> aux;
	if(aux == ')') return;
	else
	{
		cin.unget();
		
		cin >> nodes[numNode].feature;
		readTree(numNode * 2);
		readTree(numNode * 2 + 1);
		cin >> skipws >> aux;
	}
	
	return;
}

int main(void)
{
	int numCases, L, A;
	
	cin >> numCases;
	for(int numCase = 1; numCase <= numCases; numCase++)
	{
		for(int i = 1; i < MAX_NODES; i++)
		{
			nodes[i].weight = 0.0;
			nodes[i].feature = "";
		}
		
		int numNode = 1;
		cin >> L;
		readTree(numNode);

		cout << "Case #" << numCase << ":" << endl;		
		
		cin >> A;
		cin.get();
		while(A--)
		{
			string pet, feature;
			set<string> features;
			int numFeatures;
			
			cin >> pet >> numFeatures;
			while(numFeatures--)
			{
				cin >> feature;
				features.insert(feature);
			}
			
			long double P = 1.0000000;
			int node = 1;
			do
			{
				P *= nodes[node].weight;
				if(nodes[node].feature == "") break;
				else if(features.find(nodes[node].feature) != features.end()) node = node * 2;
				else node = node * 2 + 1;
			}
			while(true);
			
			printf("%.7Lf\n", P);
		}
		
	}
}
