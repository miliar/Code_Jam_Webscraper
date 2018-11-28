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
#include <map>
#include <string>
#include <iostream>
using namespace std;

map<char,char> textmap;

class CodeJam {
public:	vector<int> result;

public:
	int solveC(int S,int p,vector<int> inputnum){
		
		sort( inputnum.begin(), inputnum.end(), greater<int>());

		/*
		printf("%d:%d\n",S,p);
		for(int i=0;i<inputnum.size();i++){
		printf("%d",inputnum[i]);
		printf(" ");
		}
		printf("\n");*/
		
		int ret=0;

		for(int i=0;i<inputnum.size();i++){
			if(inputnum[i]/3 >= p){
				ret++;
			}else if(inputnum[i]/3 == p-1 && ( inputnum[i]%3 ==2 || inputnum[i]%3 ==1)){
				ret++;
			}else if(inputnum[i]/3 == p-1 && inputnum[i]%3 ==0 && S>0 && p>=2){
				ret++;
				S--;
			}else if(inputnum[i]/3 == p-2 && inputnum[i]%3 ==2 && S>0 && p>=2){
				ret++;
				S--;
			}else if(inputnum[i]/3 < p-2){
				break;
			}
		}
		return ret;
	}
};



// このアプリケーションのエントリ ポイントです。
int _tmain(void)
{
    CodeJam *codejam;
	vector <int> inputnum;

	std::string str;
	std::ifstream ifs( "a.txt" );

	getline(ifs, str);
	int output_no=1;

	while( !ifs.eof() ){

			getline(ifs, str);
			if(str.size()==0){
				break;
			}
			int i=0;
			string tmp;
			int tmpint=0;
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
				inputnum.push_back(tmpint);
			}

			vector<int>::iterator itr = inputnum.begin();
			inputnum.erase(itr);
			int S = *(itr);
			inputnum.erase(itr);
			int p = *(itr);
			inputnum.erase(itr);
			
			codejam=new CodeJam;
			int ret = codejam->solveC(S,p,inputnum);

			std::cout << "Case #" << output_no << ": " << ret << std::endl;
			
			output_no++;
			inputnum.clear();
	}
	
	

    return 0;
}
