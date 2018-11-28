#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class candy{
public:
	int val;
	vector<int> bits;
	candy(int v){
		val = v;
		setBits();
	}
private:
	void setBits(){
		bits.clear();
		int idval = 1;
		while(idval <= val){
			if((idval & val) == idval){
				bits.push_back(1);
			}else{
				bits.push_back(0);
			}
			idval *= 2;
		}
	}
};

class pile{
public:
	vector<candy> candies;
	int sval;
	vector<int> pval;
	int pvali;
	pile(){
		sval = 0;
		pvali = 0;
		candies.clear();
		pval.clear();
	}
	void addCandy(candy &c){
		candies.push_back(c);
		sval += c.val;
		for(int i=0;i<c.bits.size();i++){
			if(i>=pval.size()){
				pval.push_back(c.bits[i]);
			}else{
				pval[i] = (pval[i] + c.bits[i]) % 2;
			}
		}
		calcpvali();
	}
private:
	void calcpvali(){
		pvali = 0;
		for(int i=0;i<pval.size();i++){
			pvali += pval[i] * (int)pow(2.0, (double)i);
		}
	}
};



int main(int argc , char** argv){

	ifstream ifs;
	if(argc>1){
		ifs.open(argv[1]);
	}else{
		ifs.open("input.txt");
	}
	if(!ifs.good())
		return -1;

	int iSize=0;
	ifs >> iSize;

	ofstream ofs("output.txt");
	for(int i=0;i<iSize;i++){
		int N=0;
		ifs >> N;

		pile inp;
		int iVal = 0;
		int iMinVal = 99999999;
		for(int in=0;in<N;in++){
			ifs >> iVal;
			if(iVal < iMinVal)
				iMinVal = iVal;
			inp.addCandy(candy(iVal));
		}

		if(inp.pvali == 0){
			cout << "Case #" << i+1 << ": " << inp.sval - iMinVal << endl;
			ofs << "Case #" << i+1 << ": " << inp.sval - iMinVal << endl;
		}else{
			cout << "Case #" << i+1 << ": NO" << endl;
			ofs << "Case #" << i+1 << ": NO" << endl;
		}
	}

	ifs.close();
	ofs.close();

	return 0;
}
