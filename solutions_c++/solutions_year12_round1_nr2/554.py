#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

class Level {
	public:
		bool DoneEasy, DoneHard;
		int Easy, Hard;
		
		Level(){
			DoneEasy = DoneHard = false;
			Easy = Hard = 0;
		}
		
		bool operator<(const Level &Other) const{
			if(Hard < Other.Hard)
				return true;
			if(Hard == Other.Hard)
				return Easy < Other.Easy;
			return false;
		}
};

int main(void){
	int T;
	cin >> T;
	
	for(int t=1; t<=T; t++){
		int N;
		cin >> N;
		
		vector<Level> Levels(N);
		int Stars = 0;
		
		for(int n=0; n<N; n++)
			cin >> Levels[n].Easy >> Levels[n].Hard;
		sort(Levels.begin(), Levels.end());
		
		int PlayCount = 0;
		for(int n=0; n<N && PlayCount>=0; n++){
			if(Levels[n].DoneHard)
				continue;
			if(Levels[n].Hard <= Stars){
				PlayCount++;
				Stars += Levels[n].DoneEasy ? 1 : 2;
				Levels[n].DoneEasy = Levels[n].DoneHard = true;
			}else{
				int m;
				for(m=N-1; m>=0; m--){
					if(Levels[m].DoneEasy)
						continue;
					if(Levels[m].Easy <= Stars){
						PlayCount++;
						Stars += 1;
						Levels[m].DoneEasy = true;
						break;
					}
				}
				if(m < 0)
					PlayCount = -1;
				n--;
			}
		}
		
		if(PlayCount >= 0)
			cout << "Case #" << t << ": " << PlayCount << endl;
		else
			cout << "Case #" << t << ": Too Bad" << endl;
	}
	
	return 0;
}
