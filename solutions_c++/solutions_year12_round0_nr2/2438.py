#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <map>
#include <vector>
#include <cmath>

using namespace std;


int main() {

	int T;
	cin >> T;

	vector<pair<int,int> > canBe; //Normal Supr.
	vector<pair<int,int> > canBe2;


	for(int t=0; t < T; ++t){
		int N; cin >> N;
		int S; cin >> S;
		int P; cin >> P;

		canBe.clear();

		for(int i=0; i < N; ++i){
			int googler; cin >> googler;

			canBe.push_back(pair<int,int>(-1,-1)); //Norm Sup

			for(int a=0; a <= 10; ++a)
				for(int b=0; b <= 10; ++b)
					for(int c=0; c <= 10; ++c){
						if(a + b + c == googler && abs(a-b) <= 2 && abs(a-c) <= 2 && abs(b-c) <= 2){
							if(abs(a-b) < 2 && abs(a-c) < 2 && abs(b-c) < 2){
								canBe[canBe.size()-1].first = max(canBe[canBe.size()-1].first, c);
							}
							else{
								canBe[canBe.size()-1].second = max(canBe[canBe.size()-1].second, c);
							}
						}
					}
		}

		
		int result=0;
		canBe2.clear();

		for(int i=0; i < canBe.size(); ++i){
			if(canBe[i].second == -1 && canBe[i].first >= P)
				++result;
			else if(canBe[i].first < P && canBe[i].second >= P && S > 0){
				++result;
				--S;	
			}
			else
				canBe2.push_back(canBe[i]);
		}
	
		for(int i=0; i < canBe2.size(); ++i){
			if(canBe2[i].first >= P){
				++result;
			}
			if(S > 0)
				--S;
		}

		cout << "Case #" << t+1 << ": " << ((!S)? result : 0) << endl;

	}




	return 0;
}


