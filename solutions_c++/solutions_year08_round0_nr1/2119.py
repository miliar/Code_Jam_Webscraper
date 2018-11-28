#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

int dp[1001][101];

int solve(const vector<string> &engines, const vector<string> &queries, int ind, bool first, int pInd)
{	
	int len = engines.size(), qLen = queries.size();
	
	if(ind >= qLen) return 0;
	
	int ans = 100000000;
	
	//cout << "Called: " << ind << ", " << pInd << endl;
	
	for(int i = 0; i < len; i++)
	{
		if(i == pInd) continue;
		if(!first && dp[ind][pInd] != -1) {
			//cout << "we have dp[" << ind << "][" << pInd << "[ = " << dp[ind][pInd] << endl;
			return dp[ind][pInd];
		}
		if(queries[ind] == engines[i]) continue;
		
		int nInd = ind;
		while(nInd < qLen && queries[nInd] != engines[i]) nInd++;
				
		int temp = solve(engines, queries, nInd, false, i);
		
		//if(ind == 0) cout << "temp: " << temp << ", with i: " << i << endl;
		
		if(!first && engines[i] != engines[pInd]) temp++;
		if(ans > temp) ans = temp;
		
		
		
	/*	if(!first) { 		
			dp[ind][pInd] = temp;
			cout << "dp[" << ind << "][" << pInd << "[ = " << dp[ind][pInd] << endl;
		}
		else dp[ind][i] = temp; */
				
	}
	
	//cout << "Returned ans with " << ind << ", parent " << pInd << " : " << ans << endl;
	if(!first)dp[ind][pInd] = ans;
	
	return ans;
}

void init(const int e, const int q)
{	
	for(int j = 0; j < q; j++)
		for(int k = 0; k < e; k++)
			dp[j][k] = -1;
}

int main()
{
	int t, engines, queries;
	int _case = 1;
	
	cin >> t;
	
	while(t--)
	{
		cin >> engines; cin.get();
				
		vector<string> sEngines(engines);
					
		for(int i = 0; i < engines; i++){
			getline(cin, sEngines[i]);			
		}
		
		cin >> queries; cin.get();
		vector<string> sQueries(queries);
				
		string temp, first;
				
		for(int j = 0; j < queries; j++)
		{
			getline(cin, sQueries[j]);
			//assert(temp.size() != 0);
		}
				
		init(engines, queries);
		
		//cout << "BEFORE SOLVING" << endl;
		
		int ans = solve(sEngines, sQueries, 0, true, -1);
		
		cout << "Case #" << _case++ << ": " << ans << endl;
	}
}










			
			