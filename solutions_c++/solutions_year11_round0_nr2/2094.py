#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;


vector<string> combine, opposed;

int main()
{
	int T;
	cin >> T;
	for (int caseID = 1; caseID <= T; ++caseID)
	{
		int C;
		cin >> C;
		combine.resize(C);
		for (int i = 0; i < C; ++i)
			cin >> combine[i];
		int D;
		cin >> D;
		opposed.resize(D);
		for (int i = 0; i < D; ++i)
			cin >> opposed[i];
		int N;
		cin >> N;
		string involke;
		cin >> involke;

		vector<char> ans;

		for (int i = 0; i < N; ++i)
		{
			char next = involke[i];

			if (ans.empty()) {
				ans.push_back(next);
				continue;
			}

			bool merge = false;
			for (int j = 0; j < C; ++j)
				if (combine[j][0] == next && combine[j][1] == ans.back() ||
					combine[j][0] == ans.back() && combine[j][1] == next){
					ans.pop_back();
					ans.push_back(combine[j][2]);
					merge = true;
					break;
				}
			if (merge) continue;
			bool clear = false;
			for (int j = 0; j < ans.size(); ++j){	
				string cannot;
				cannot += next;
				cannot += ans[j];
				for (int k = 0; k < D; ++k)
					if (opposed[k][0] == next && opposed[k][1] == ans[j] ||
						opposed[k][1] == next && opposed[k][0] == ans[j]){
						clear = true;
						goto out;	
					}
			}
out:;
			if (clear) {
					ans.clear();
					continue;
			}
			ans.push_back(next);
		}		

		cout<<"Case #"<<caseID<<": [";
		for (int i = 0; i < ans.size(); ++i)
			if (i) cout<<", "<<ans[i];
			else cout<<ans[i];
		cout<<"]"<<endl;
	}

	return 0;
}
