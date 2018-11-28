#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class chick{
	vector<int> vv;
	vector<int> vx;
	vector<int> rtbl;
	int mB;
	int mK;
	int mN;
	int mT;
	int mRCnt;
public:
	chick(int n, int k, int b, int t){
		mN = n;
		mK = k;
		mB = b;
		mT = t;
		vv.clear();
		vx.clear();
		rtbl.clear();
	}

	void addvx(int x){
		vx.push_back(x);
	}

	void addvv(int v){
		vv.push_back(v);
	}

	int CrnMove(){
		if(mK == 0)
			return 0;

		makertbl();

		if(mRCnt < mK)
			return -1;

		int ret = 0;

		for(int i=0;i<mK;i++){
			if(rtbl[i])
				continue;
			for(int j=i+1;j<mN;j++){
				if(rtbl[j]){
					rtbl[i]=1;
					rtbl[j]=0;
					ret += j-i;
					break;
				}
			}
		}

		return ret;
	}

	void makertbl(){
		rtbl.clear();
		mRCnt = 0;
		for(int i=mN-1;i>=0;i--){
			if(CanReach(i)){
				rtbl.push_back(1);
				mRCnt++;
			}else{
				rtbl.push_back(0);
			}
		}
	}

	bool CanReach(int i){
		if(mB - vx[i] > vv[i] * mT){
			return false;
		}
		return true;
	}
};
