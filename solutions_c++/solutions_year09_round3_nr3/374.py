#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int func ( vector<int> V, int n) 
{
	int ans;

/*	for (int i = 0; i < V.size(); i++ ) {
		cout << V[i] << " ";
	}	

cout << endl;*/
	vector <int> q;
	q.push_back(0);
	q.push_back(n+1);

	ans = 0;

	for(int i = 0; i < V.size(); i++ ) {
		int mindif=n,maxdif=n, min, max;
		for(int j = 0; j < q.size(); j++ ) {
			if(V[i] - q[j] -1< mindif && q[j] < V[i]) {
				mindif = V[i]-q[j]-1;
				min=V[i];
			}
			if(q[j] - V[i] -1< maxdif && q[j] > V[i]) {
				maxdif = q[j]-V[i]-1;
				max=V[i];
			}
		}
		
		ans += mindif;
		ans+= maxdif;
		q.push_back(V[i]);


	}

	return ans;

}
int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int n, l;
		cin >> n >> l;
		vector<int> v;
		vector<int> tv;
		for (int j = 0; j < l; j++)
		{
			int m;
			cin >> m;
			v.push_back(m);
		}

		sort (v.begin(), v.end());
		tv = v;

		int min = 1000000000;
		int s;
		do {
			 if ( (s = func (v, n )) < min) {
				 min = s;
			 }
		 	next_permutation(v.begin(),v.end()) ;
		} while ( v != tv);
		
		cout << "Case #" << i << ": " << min<< endl;
	}

	return 0;
}
