#include <iostream>
#include <vector>

using namespace std;

main(){
	int T, count = 0;
	cin >> T;
	while(count < T){
		count++;
		int N, S, p, result = 0;
		cin >> N >> S >> p;
		vector<int> scores, ix;
		while(scores.size() != N){
			int temp;
			cin >> temp;
			scores.push_back(temp);
		}
		for(int i = 0; i < N; i++){
			if(scores[i] % 3 == 0){
				if(scores[i] >= 3 && scores[i] <= 27){
					if((scores[i]/3 + 1) >= p){
						if(scores[i]/3 < p && S > 0){
							ix.push_back(i);
							result++;
							S--;
						}
					}
				}
			}
			else if((scores[i] - 2) % 3 == 0){
				if(scores[i] >= 2 && scores[i] <= 26){
					if((scores[i] + 4)/3 >= p){
						if((scores[i] + 1)/3 < p && S > 0){
							ix.push_back(i);
							result++;
							S--;
						}
					}
				}
			}
		}
		for(int i = 0; i < ix.size(); i++){
			scores.erase(scores.begin()+ix[i]);
		}		
		for(int i = 0; i < scores.size(); i++){
			if(scores[i] % 3 == 0){
				if(scores[i] >= 3 && scores[i] <= 27 && S > 0){
					if((scores[i]/3 + 1) >= p){	
						result++;
						S--;	
					}
				}
				else if(scores[i]/3 >= p)	result++;
			}
			if((scores[i] - 1) % 3 == 0){
				if(scores[i] >= 4 && scores[i] <= 28 && S > 0){
					if((scores[i] + 2)/3 >= p){
						result++;
						S--;
					}
				}
				else if((scores[i] + 2)/3 >= p)      result++;
			}
			if((scores[i] - 2) % 3 == 0){
				if(scores[i] >= 2 && scores[i] <= 26 && S > 0){
					if((scores[i] + 4)/3 >= p){
						result++;
						S--;
					}
				}
				else if((scores[i] + 1)/3 >= p)      result++;
			}
		}
		cout << "Case #" << count << ": " << result << endl;
	}
	return 0;
}
	

			
				
					
		
