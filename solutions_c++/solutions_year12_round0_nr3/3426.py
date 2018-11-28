//============================================================================
// Name        : GCJ2012_C_onlySmall.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;
class Digit{
public:
	int x;
	vector<int> vecx;

	Digit(int x){
		this->x = x;
		this->setVec(x);
	}

	void setVec(int x){
		while(1){
			if(x != 0){
				vecx.push_back(x % 10);
				x /= 10;
			}else{
				break;
			}
		}
	}

	int getKeta(){
		return vecx.size();
	}

	int recycle(){
		int ret = vecx[0];

		for(int i = vecx.size() - 1; i > 0; i--){
			ret *= 10;
			ret += vecx[i];
		}

		return ret;
	}
};


bool isInbound(int lw, int up, int x){
	if(lw <= x && x <= up){
		return true;
	}else{
		return false;
	}
}

int recycle(Digit &dx){
	int recyc = 0;

	recyc = dx.recycle();

	return recyc;

}


int solve(int lw, int up){
	int ret = 0;

	for(int x = lw; x <= up; x++){
		Digit dx = Digit(x);
		int y = recycle(dx);
		if(isInbound(lw, up, y)){
			if(x != y){
				if(dx.getKeta() == 2 && x < y){
					ret++;
				}else if(dx.getKeta() == 3){
					ret++;
				}
			}
		}
	}

	return ret;
}
int main() {
	int testcase_num = 0;
	std::cin >> testcase_num;

	for(int i = 0; i < testcase_num; ++i){
		int ans = 0;
		int lower;
		int upper;

		cin >> lower;
		cin >> upper;

		ans = solve(lower, upper);

		printf("Case #%d: %d\n", i+1, ans);
	}

}
