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

class CodeJam {
public:	vector<int> result;

public:
	vector<string> solveC(vector <string> mytiles){
		vector<string> ret;
		int i=0;
		int j=0;

		for(i=0;i<mytiles.size()-1;i++){
			for(j=0;j<mytiles[i].size()-1;j++){
				if(mytiles[i].compare(j,1,"#")==0 && 
					mytiles[i].compare(j+1,1,"#")==0 && 
					 mytiles[i+1].compare(j,1,"#")==0 && 
					  mytiles[i+1].compare(j+1,1,"#")==0){

					mytiles[i].replace(j,1,"/");
					mytiles[i].replace(j+1,1,"\\");
					mytiles[i+1].replace(j,1,"\\");
					mytiles[i+1].replace(j+1,1,"/");
				}
			}
		}

		ret=mytiles;

		for(i=0;i<mytiles.size();i++){
			int fd = mytiles[i].find("#",0);
			if(fd != string::npos ){
				ret.clear();
				ret.push_back("Impossible");
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

	int i=0;
	int j=0;
	int output_no = 1;
	int tmpint=0;
	string tmp;

	vector<string> mytiles;
	vector<string> ret;

	std::string str;
	std::ifstream ifs( "a.txt" );

	getline(ifs, str);
	while( !ifs.eof() ){
			getline(ifs, str);
			if(str.size()==0){
				break;
			}
			tmp.append(str.substr(0,1));
			tmpint = atoi(tmp.c_str());
			tmp.clear();

			for(i=0;i<tmpint;i++){
				getline(ifs, str);
				mytiles.push_back(str);
			}


			codejam=new CodeJam;
			ret = codejam->solveC(mytiles);

			std::cout << "Case #" << output_no << ":" << std::endl;
			output_no++;

			/*debug*/
			for(i=0;i<ret.size();i++){
				std::cout << ret[i] << std::endl;
			}

			mytiles.clear();

		}
	
	

    return 0;
}
