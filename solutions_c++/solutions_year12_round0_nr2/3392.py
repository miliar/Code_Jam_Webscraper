//============================================================================
// Name        : GCJ2012_B.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class HiScore {
public:
	int supp;
	int nosupp;

	HiScore(){
		this->supp = 0;
		this->nosupp = 0;
	}

	HiScore(int supp, int nosupp){
		this->supp = supp;
		this->nosupp = nosupp;
	}
};

void getHighScore(int totalPoints, HiScore& hiscore){
	int sho = totalPoints/3;
	int amari = totalPoints % 3;

	if(totalPoints == 0){
		hiscore.supp = 0;
		hiscore.nosupp = 0;
	}else if(totalPoints == 1){
		hiscore.supp = 0;
		hiscore.nosupp = 1;
	}else{
		if(amari == 0){
			hiscore.supp = sho + 1;
			hiscore.nosupp = sho;
		}else if(amari == 1){
			hiscore.supp = sho + 1;
			hiscore.nosupp = sho + 1;
		}else if(amari == 2){
			hiscore.supp = sho + 2;
			hiscore.nosupp = sho + 1;
		}
	}
}
// threshold超えているなら+1
int solve(int googlerm, int &numSup, int threshold, int points){

	HiScore hiscore;

	getHighScore(points, hiscore);

	if(hiscore.nosupp >= threshold){
		return 1;
	}else{
		if(numSup > 0){
			if(hiscore.supp >= threshold){
				numSup--;
				return 1;
			}
		}
	}

	return 0;
}
int main() {
	int testcase_num = 0;
	std::cin >> testcase_num;

	for(int i = 0; i < testcase_num; ++i){
		int ans = 0;
		int googler;
		int numSup;
		int threshold;

		cin >> googler;
		cin >> numSup;
		cin >> threshold;

		for(int j = 0; j < googler; j++){
			int totalpoints;
			cin >> totalpoints;
			ans += solve(googler, numSup, threshold, totalpoints);
		}


		printf("Case #%d: %d\n", i+1, ans);
	}

	return 0;
}
