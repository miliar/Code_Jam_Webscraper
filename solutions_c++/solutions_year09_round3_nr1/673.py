#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

const string ltrs = "0123456789abcdefghijklmnopqrstuvwxyz";
class clsa{
public:
	//vector<bool> vflg;
	vector<int> vdgts;
	double getMinSec(string str){
		//vflg.clear();
		//vflg.resize(ltrs.length(),false);
		vdgts.clear();
		vdgts.resize(ltrs.length(),0);
		int iNum=0;
		for(int i=0;i<str.length();i++){
			size_t pos = ltrs.find_first_of(str[i]);
			if(pos == ltrs.npos)
				continue;
			if(!vdgts.at(pos)){
				iNum++;
				vdgts.at(pos) = iNum;
				//vflg.at(pos) = true;
				//dN += vdgts.at(pos) * pow(10.0, str.length() - i - 1);
			}else{
				//dN += vdgts.at(pos) * pow(10.0, str.length() - i - 1);
			}
		}
		long iSec = 0;
		double dN = 0.0;
		if(iNum==1)
			iNum++;
		for(int i=0;i<str.length();i++){
			size_t pos = ltrs.find_first_of(str[i]);
			if(pos == ltrs.npos)
				continue;
			int iTgt =  vdgts.at(pos);
			if(iTgt==2)
				iTgt = 0;
			else if(iTgt>2)
				iTgt--;
			cout << iTgt << " ";
			iSec += (long)(iTgt * pow((double)iNum, (double)(str.length() - i - 1)));
			dN += iTgt * pow((double)iNum, (double)(str.length() - i - 1));
			///dN += vdgts.at(pos) * pow(iNum, str.length() - i - 1);
		}
		//cout << dN << "  ";
		//long iSec = 0;
		//int iCnt = 0;
		//while(dN > iSec){
		//	iSec += (long)(dN%iNum * pow((double)iNum,iCnt));
		//	dN /= iNum;
		//	iCnt++;
		//}

		return dN;

	}
};
