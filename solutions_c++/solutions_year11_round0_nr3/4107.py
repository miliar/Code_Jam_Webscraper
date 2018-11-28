// これは、アプリケーション ウィザードを使って生成された、VC++ アプリケーション プロジェクトの 
// メイン プロジェクト ファイルです。

#include "stdafx.h"
#using <mscorlib.dll>
#include <tchar.h>
#include <math.h>
using namespace System;







#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class CodeJam {
public:	vector<int> result;

public:
	int solveC(vector <int> cand){
		int ret=-1;
		int j=0;
		int outcand=0;
		int zeroc=0;

		std::sort(cand.rbegin(),cand.rend());
		for(j=0;j<cand.size();j++){
			zeroc = zeroc + cand[j];
		}
		
		for(j=0;j<128;j++){
			recsub(0,cand.size(),cand,0,0,outcand,zeroc);
		}
		
		for(j=0;j<result.size();j++){
			if(ret<result[j]){
				ret=result[j];
			}
		}
		result.clear();
		
		return ret;
	}

	bool recsub(int i, int max, vector <int> cand, int left, int right, int outcand, int zeroc){
		bool flag;
		int j=0;
		if(i==max){
			if(left==right && outcand!=zeroc){
				flag=true;
				for(j=0;j<result.size();j++){
					if(result[j]==outcand){
						flag = false;
						break;
					}
				}
				if(flag==true){
					result.push_back(outcand);
				}
			}
			return flag;
		}
		if(recsub(i+1,max,cand,kakezan(left,cand[i]),right,outcand+cand[i],zeroc)){
			return true;
		}
		if(recsub(i+1,max,cand,left,kakezan(right,cand[i]),outcand,zeroc)){
			return true;
		}
		return false;
	}

	int kakezan(int a, int b){
		return a ^ b;
	}
};



// このアプリケーションのエントリ ポイントです。
int _tmain(void)
{
    CodeJam *codejam;
	int flag=0;
	int i=0;
	int j=0;
	int k=1;
	int ret=0;

	string tmp;
	int tmpint=0;
	vector<int> cand;

	std::string str;
	std::ifstream ifs( "C:\\Documents and Settings\\kyouko\\My Documents\\Visual Studio Projects\\codejam\\Debug\\a.txt" );
	std::ofstream ofs( "C:\\Documents and Settings\\kyouko\\My Documents\\Visual Studio Projects\\codejam\\Debug\\b.txt" );

	while( !ifs.eof() ){
		if(flag==0){
			getline(ifs, str);
			flag=1;
		}else if(flag==1){
			getline(ifs, str);
			flag=2;
		}else{
			i=0;
			getline(ifs, str);
			flag=1;
			
			while(i<str.size()){
				while(str.compare(i,1," ")!=0){
					tmp.append(str.substr(i,1));
					i++;
					if(i==str.size()){
						break;
					}
				}
				i++;//スペース分
				tmpint = atoi(tmp.c_str());
				tmp.clear();
				cand.push_back(tmpint);
			}

			codejam=new CodeJam;
			ret = codejam->solveC(cand);
			
			/*debug
			for(j=0;j<cand.size();j++){
				std::cout << cand[j] << std::endl;
			}*/
			
			cand.clear();
			
			if(ret != -1){
				ofs << "Case #" << k << ": " << ret << std::endl;
			}else{
				ofs << "Case #" << k << ": NO" << std::endl;
			}
			k++;

			
			
		}
	}
	
	

    return 0;
}
