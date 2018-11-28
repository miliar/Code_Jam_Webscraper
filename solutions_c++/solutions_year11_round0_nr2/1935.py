#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class combi{
public:
	char sfrom1;
	char sfrom2;
	string sto;
	combi(string str){
		sfrom1 = str[0];
		sfrom2 = str[1];
		sto = str.substr(2, 1);
	}
	bool isMatch(char c1, char c2){
		if(c1 == sfrom1 && c2 == sfrom2){
			return true;
		}
		if(c2 == sfrom1 && c1 == sfrom2){
			return true;
		}
		return false;
	}
};

class oppose{
public:
	char sfrom1;
	char sfrom2;
	string sto;
	bool ap1;
	oppose(string str){
		sfrom1 = str[0];
		sfrom2 = str[1];
		sto = str.substr(2, 1);
	}
	bool isMatch1(char c1){
		if(c1 == sfrom1){
			ap1 = true;
			return true;
		}
		if(c1 == sfrom2){
			ap1 = false;
			return true;
		}
		return false;
	}
	bool isMatch2(char c1){
		if(ap1){
			if(c1 == sfrom2){
				return true;
			}
		}else{
			if(c1 == sfrom1){
				return true;
			}
		}
		return false;
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
		int C=0, D=0, N=0;
		vector<combi> vcom;
		vector<oppose> vopp;

		ifs >> C;
		for(int in=0;in<C;in++){
			string str;
			ifs >> str;
			vcom.push_back(combi(str));
		}

		ifs >> D;
		for(int in=0;in<D;in++){
			string str;
			ifs >> str;
			vopp.push_back(oppose(str));
		}

		ifs >> N;
		string els;
		ifs >> els;

		string ret = "";
		for(int in=0;in<N;in++){
			string stgt = els.substr(in, 1);
			if(ret.length() == 0){
				ret += stgt;
				//for(int io=0;io < vopp.size();io++){
				//	vopp[io].isMatch1(stgt[0], in);
				//}
			}else{
				bool bcom = false;
				for(int ic=0;ic < vcom.size();ic++){
					if(vcom[ic].isMatch(ret[ret.length()-1], stgt[0])){
						bcom = true;
						ret.erase(ret.length() -1,1);
						ret += vcom[ic].sto;
						break;
					}
				}
				if(!bcom){
					for(int io=0;io < vopp.size();io++){
						if(vopp[io].isMatch1(stgt[0])){
							//for(int ir = ret.length() - 1; ir>=0;ir--){
							for(int ir = 0; ir<ret.length();ir++){
								if(vopp[io].isMatch2(ret[ir])){
									bcom = true;
									//ret.erase(ir,ret.length() - ir);
									ret.clear();
									break;
								}
							}
						}
					}
				}
				if(!bcom){
					ret += stgt;
					//for(int io=0;io < vopp.size();io++){
					//	vopp[io].isMatch1(stgt[0], in);
					//}
				}
			}
		}

		cout << "Case #" << i+1 << ": [";
		ofs << "Case #" << i+1 << ": [";
		for(int ir=0;ir<ret.length();ir++){
			if(ir!=0){
				cout << ", ";
				ofs << ", ";
			}
			cout << ret[ir];
			ofs << ret[ir];
		}
		cout << "]" << endl;
		ofs << "]" << endl;
	}

	ifs.close();
	ofs.close();

	return 0;
}
