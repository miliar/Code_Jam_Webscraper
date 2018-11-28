#include <iostream>
using namespace std;

int nodes[40];
int changes[40];
int num_node;
int root_val;

bool eval_tree(int arr[], int ind)
{
	if (ind > (num_node-1)/2) return arr[ind];
	bool left = eval_tree(arr,2*ind);
	bool right = eval_tree(arr,2*ind+1);
	if (arr[ind] == 1) // AND
		return left && right;
	else // OR
		return left || right;
}

int countbit(int n)
{
	int ret = 0;
	while(n > 0)
	{
		if (n%2) ret++;
		n /= 2;
	}
	return ret;
}
int main()
{
	int ncase; cin >> ncase;
	for(int icase=1; icase <= ncase; icase++)
	{
		cout << "Case #" << icase << ": ";
		cin >> num_node >> root_val;

		int i;
		for(i=1; i <= (num_node-1)/2; i++)
			cin >> nodes[i] >> changes[i];
		for(;i <= num_node; i++)
			cin >> nodes[i];
		
		int inner = (num_node-1)/2;
//cout << num_node << " " << inner << endl;
		int minbit = inner+1;
		int loop;
		for(loop=0; loop < (1<<inner); loop++)
		{
			int duptree[40];
			for(int i=1; i <= num_node; i++)
				duptree[i] = nodes[i];
			for(int pos=0; pos < inner; pos++)
			{
				if ((loop&(1<<pos)) == 0 || changes[pos+1] == 0) continue;
				duptree[pos+1] = 1-duptree[pos+1];
			}
			if (eval_tree(duptree,1) == root_val) { minbit = min(minbit, countbit(loop)); }
		}
		if (minbit > inner) cout << "IMPOSSIBLE\n";
		else cout << minbit << "\n";
	}
}

