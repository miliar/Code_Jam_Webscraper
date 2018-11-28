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
	string solveC(string str){
		
		
		/*map<char, char>::iterator it = textmap.begin();
		while( it != textmap.end() )
		{
			cout << (*it).first << ":" << (*it).second << endl;
			++it;
		}*/

		string retword;
		char tmp;

		for(int i=0;i<str.size();i++){
			strncpy(&tmp,str.c_str()+i,1);
			map<char, char>::iterator it = textmap.begin();
			it=textmap.find(tmp);
			char a = it->second;

			retword.append(&a,1);
		}
		
		return retword;
	}
};



// このアプリケーションのエントリ ポイントです。
int _tmain(void)
{
    CodeJam *codejam;
	string retword;

	std::string str;
	std::ifstream ifs( "a.txt" );

	char a_m[]="qz";
	char a_n[]="zq";
	for(int i=0;i<strlen(a_m);i++){
		textmap.insert(map<char, char>::value_type(a_m[i],a_n[i]));
	}

	char b_m[]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char b_n[]="our language is impossible to understand";
	for(int i=0;i<strlen(b_m);i++){
		textmap.insert(map<char, char>::value_type(b_m[i],b_n[i]));
	}

	char c_m[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char c_n[]="there are twenty six factorial possibilities";
	for(int i=0;i<strlen(c_m);i++){
		textmap.insert(map<char, char>::value_type(c_m[i],c_n[i]));
	}

	char d_m[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char d_n[]="so it is okay if you want to just give up";
	for(int i=0;i<strlen(d_m);i++){
		textmap.insert(map<char, char>::value_type(d_m[i],d_n[i]));
	}

	

	getline(ifs, str);
	int output_no=1;

	while( !ifs.eof() ){
			getline(ifs, str);
			if(str.size()==0){
				break;
			}
			

			codejam=new CodeJam;
			retword = codejam->solveC(str);

			std::cout << "Case #" << output_no << ": " << retword << std::endl;
			output_no++;
	}
	
	

    return 0;
}
