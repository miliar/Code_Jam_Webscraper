// これは、アプリケーション ウィザードを使って生成された、VC++ アプリケーション プロジェクトの 
// メイン プロジェクト ファイルです。

#include "stdafx.h"
#using <mscorlib.dll>
#include <tchar.h>
using namespace System;







#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class CodeJam {
public:
	int solveA(vector <string> bostr, vector <int> bint, vector <int> oint){

		int i=0;
		int cnt=0;
		int bnowpoint=1;
		int onowpoint=1;
		int with=0;

		vector<int>::iterator it;

		for(i=0;i<bostr.size();i++){
			if(bostr[i].compare("B")==0){
				with=bint[0]-bnowpoint;
				bnowpoint = bnowpoint + with;
				
				it=bint.begin();//クリア処理
				bint.erase(it);

				if(with<0){
					with=-with;
				}

				cnt=cnt+with+1;//拾う分も含め
				with=with+1;//拾う時間
				
				if(oint[0]-onowpoint>0){
					if(with < oint[0]-onowpoint){
						onowpoint=onowpoint+with;
					}else{
						onowpoint=oint[0];
					}
				}else if(oint[0]-onowpoint<0){
					if(with < -(oint[0]-onowpoint)){
						onowpoint=onowpoint-with;
					}else{
						onowpoint=oint[0];
					}
				}

			}else{
				with=oint[0]-onowpoint;
				onowpoint = onowpoint + with;
				
				it=oint.begin();//クリア処理
				oint.erase(it);

				if(with<0){
					with=-with;
				}

				cnt=cnt+with+1;//拾う分も含め
				with=with+1;//拾う時間
				
				if(bint[0]-bnowpoint>0){
					if(with < bint[0]-bnowpoint){
						bnowpoint=bnowpoint+with;
					}else{
						bnowpoint=bint[0];
					}
				}else if(bint[0]-bnowpoint<0){
					if(with < -(bint[0]-bnowpoint)){
						bnowpoint=bnowpoint-with;
					}else{
						bnowpoint=bint[0];
					}
				}

			}

		}
		return cnt;
	}
};



// このアプリケーションのエントリ ポイントです。
int _tmain(void)
{
    CodeJam *codejam;
	int flag=0;
	int i=0;
	int j=1;

	string tmp;
	vector<string> bostr;

	int tmpint=0;
	vector<int> bint;
	vector<int> oint;

	std::ifstream ifs( "C:\\Documents and Settings\\kyouko\\My Documents\\Visual Studio Projects\\codejam\\Debug\\a.txt" );
	std::string str;
	std::ofstream ofs( "C:\\Documents and Settings\\kyouko\\My Documents\\Visual Studio Projects\\codejam\\Debug\\b.txt" );

	while( !ifs.eof() ){
		if(flag==0){
			getline(ifs, str);
			flag=1;
		}else{
			getline(ifs, str);
			i=0;
			while(i< str.size()){
				if(str.compare(i,1,"B")==0){
					tmp=str.substr(i,1);
					i=i+2;//スペース分含め
					bostr.push_back(tmp);
					tmp.clear();
					
					while(str.compare(i,1," ")!=0){
						tmp.append(str.substr(i,1));
						i=i+1;
						if(i==str.size()){
							break;
						}
					}
					tmpint = atoi(tmp.c_str());
					bint.push_back(tmpint);
					tmp.clear();

				}else if(str.compare(i,1,"O")==0){
					tmp=str.substr(i,1);
					i=i+2;
					bostr.push_back(tmp);
					tmp.clear();

					while(str.compare(i,1," ")!=0){
						tmp.append(str.substr(i,1));
						i=i+1;
						if(i==str.size()){
							break;
						}
					}
					tmpint = atoi(tmp.c_str());
					oint.push_back(tmpint);
					tmp.clear();

				}
				i=i+1;
			}

			if(bint.empty()){
				bint.push_back(0);
			}
			if(oint.empty()){
				oint.push_back(0);
			}
			codejam=new CodeJam;
			int ret = codejam->solveA(bostr,bint,oint);
			
			ofs << "Case #" << j << ": " << ret << std::endl;
			j++;

			/*debug
			for(i=0;i<bint.size();i++){
				printf("%d\n",bint[i]);
			}
			for(i=0;i<bostr.size();i++){
				std::cout << bostr[i] << std::endl;
			}*/

			bostr.clear();
			bint.clear();
			oint.clear();
		}
	}
	
	

    return 0;
}
