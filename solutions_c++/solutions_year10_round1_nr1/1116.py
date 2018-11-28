#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class mati{
	int** mMat;
	int mRow;
	int mCol;

	mati(){
		mMat = NULL;
		mRow = 0;
		mCol = 0;
	}
public:
	mati(int row, int col){
		if(row < 1)
			row = 1;
		if(col < 1)
			col = 1;
		mRow = row;
		mCol = col;

		mMat = new int*[mRow];
		for(int i=0;i<mRow;i++){
			mMat[i] = new int[mCol];
		}

		init(0);
	}
	const int& Row() const {
		return mRow;
	}
	const int& Col() const {
		return mCol;
	}
	void init(int ini){
		for(int i=0;i<mRow;i++){
			for(int j=0;j<mCol;j++){
				mMat[i][j] = ini;
			}
		}
	}
	int& operator()(int row, int col){
		return mMat[row][col];
	}
};

class joink{
	mati *mMat;
	joink(){
		mMat = NULL;
	}
public:
	joink(int N){
		mMat = new mati(N,N);
	}
	mati& Mat(){
		return *mMat;
	}

	void Gravity(){
		for(int j=0;j<Mat().Col();j++){
			for(int i=0;i<Mat().Row();i++){
				if(Mat()(i,j) == 0){
					for(int k=i+1;k<Mat().Row();k++){
						if(Mat()(k,j) != 0){
							Mat()(i,j) = Mat()(k,j);
							Mat()(k,j) = 0;
							break;
						}
					}
				}
			}
		}
	}

	void CheckWin(int K, bool &bRed, bool &bBlue){
		Gravity();

		bRed = false;
		bBlue = false;

		//row
		for(int j=0;j<Mat().Col();j++){
			int iCont = 0;
			int iPrev = 0;
			for(int i=0;i<Mat().Row();i++){
				if(!CheckCont(Mat()(i,j), K, iCont, iPrev, bRed, bBlue))
					break;
			}
			if(bBlue && bRed)
				return;
		}
		//col
		for(int i=0;i<Mat().Row();i++){
			int iCont = 0;
			int iPrev = 0;
			for(int j=0;j<Mat().Col();j++){
				CheckCont(Mat()(i,j), K, iCont, iPrev, bRed, bBlue);
			}
			if(bBlue && bRed)
				return;
		}
		//diag1
		for(int i=0;i<Mat().Row() + Mat().Col();i++){
			int iCont = 0;
			int iPrev = 0;
			//if(i < K || i - (Mat().Row() + Mat().Col() - 1) < K)
			//	continue;
			for(int j=0;j<Mat().Row();j++){
				int k=i-j;
				if(k < 0)
					continue;
				if(k >= Mat().Row())
					continue;
				CheckCont(Mat()(j,k), K, iCont, iPrev, bRed, bBlue);
			}
			if(bBlue && bRed)
				return;
		}
		//diag2
		int iCnt = -1;
		for(int i=Mat().Row() - 1;i >= -Mat().Col() + 1;i--){
			int iCont = 0;
			int iPrev = 0;
			//iCnt++;
			//if(iCnt < K || iCnt - (Mat().Row() + Mat().Col() - 1) < K)
			//	continue;
			for(int j=0;j<Mat().Row();j++){
				int k=i+j;
				if(k < 0)
					continue;
				if(k >= Mat().Row())
					continue;
				CheckCont(Mat()(j,k), K, iCont, iPrev, bRed, bBlue);
			}
			if(bBlue && bRed)
				return;
		}

	}

	bool CheckCont(int iVal, int K, int& iCont, int& iPrev, bool &bRed, bool &bBlue){
		if(iVal == 0){
			iCont = 0;
			if(iPrev != iVal){
				iPrev = 0;
			}
			return false;
		}
		if(iVal > 0){
			if(bRed){
				iPrev = iVal;
				return true;
			}
			if(iPrev != iVal){
				iCont = 1;
				iPrev = iVal;
			}else{
				iCont++;
			}
			if(iCont >= K){
				bRed = true;
			}
		}
		if(iVal < 0){
			if(bBlue){
				iPrev = iVal;
				return true;
			}
			if(iPrev != iVal){
				iCont = 1;
				iPrev = iVal;
			}else{
				iCont++;
			}
			if(iCont >= K){
				bBlue = true;
			}
		}
		return true;
	}



};



