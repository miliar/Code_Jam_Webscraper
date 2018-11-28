#include<iostream>
#include<algorithm>	
#include<map>
#include<string>
#include<vector>
#include<queue>

#define INF ((1 << 30) - 1)

using namespace std;

int main() {
	int N, NA, NB, T, h, m;
	char colon;
	
	cin >> N;
	
	vector<int> DA, DB;
	deque<int> AA, AB;
	
	for(int ni = 0; ni < N; ni++) {
		cin >> T >> NA >> NB;
		
		DA.clear(); DB.clear();
		AA.clear(); AB.clear();
		
		while(NA--) {
			cin >> h >> colon >> m;
			DA.push_back(h * 60 + m);
			
			cin >> h >> colon >> m;
			AB.push_back(h * 60 + m + T);
		}
		
		while(NB--) {
			cin >> h >> colon >> m;
			DB.push_back(h * 60 + m);
			
			cin >> h >> colon >> m;
			AA.push_back(h * 60 + m + T);
		}
		
		sort(DA.begin(), DA.end());
		sort(AB.begin(), AB.end());
		sort(DB.begin(), DB.end());
		sort(AA.begin(), AA.end());
		
		NA = NB = 0;
		
		for(vector<int>::iterator it = DA.begin(); it != DA.end(); it++) {
			if(AA.size() > 0) {
				if(*it >= AA[0]) {
					AA.pop_front();
					continue;
				}
			}
			NA++;
		}
		
		for(vector<int>::iterator it = DB.begin(); it != DB.end(); it++) {
			if(AB.size() > 0) {
				if(*it >= AB[0]) {
					AB.pop_front();
					continue;
				}
			}
			NB++;
		}
		
		cout << "Case #" << (ni+1) << ": " << NA << " " << NB << endl;
	}
	
	return 0;
}
