// GCJ2009_Round1B_probB.cpp : 定義主控台應用程式的進入點。
//

//String Test By Robert Jiang 2009.09.12

#include "stdafx.h"
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
string Left(string si,int m){
	string sL=si.substr(0,m);
	return sL;
}
string Mid(string si,int m,int n){
	string smn=si.substr(m-1, m-1+ n-1);
	return smn;
}
string MidTail(string si,int m){
	string sm=si.substr(m-1, si.length()-(m-1));
	return sm;
}

string GetToken(string &s,string sDelimitation){ //s為傳址呼叫！
	int iPos= -1;
	for (int pos=0;pos<s.length(); pos++){
		for (int ii=0;ii<sDelimitation.length();ii++){
			if (s[pos]==sDelimitation[ii]) {iPos=pos; break;}
		}
		if (iPos>-1) break;
	}
	//int i=s.find(" "); //※因由0開始找，所以找到後要+1

	//i 是分隔點  由0開始算，所以-1是找不到！
	int i=iPos;
	if (i==-1) {//若找不到
		string s2=s;
		s="";
		return s2;
	} else {
		string s2=Left(s,(i+1)-1);
		s=MidTail(s,(i+1)+1);
		return s2;
	}	
}
string NextPerm0(string si){
	string sAns="";
	if (si.length()==1) {
		sAns=si+"0";
		return sAns;
	}
	string s=si;
	// 檢查：若已由大->小，則要多加一個 0
	char d;
	d=si[si.length()-1];	
	int i;
	for (i=si.length()-2; i>=0 ; i--){//由"後"往前找第一個第一個 小<--大
		if (si[i]< d) break; //若發現任一個
		d=si[i];
	}
	if (i>=0) { //有發現 小 <- 大
		string ss=MidTail(si,i+1);
		next_permutation(ss.begin(),ss.end());
		//string ss2=
		sAns=Left(si,i);
		sAns+=ss;		
		return sAns;
	}else {
		sort(si.begin(),si.end());
		//找第一個非0放在開頭！		
		int inz=0;
		for (inz=0 ;inz<si.length();inz++){
			if (si[inz]!='0') break;
		}
		//string temp=si[i];
		//si[0]=si[i]; s[i]='0';
		sAns=si[inz];
		si[inz]='0';
		//sAns+='0';
		//string ss=Mid(si,inz+1);
		//string ss=MidTail(si,2);
		sAns+=si;
		return sAns;
	}
}
int _tmain(int argc, _TCHAR* argv[])
{

	char sBuf[256];
	int n_Testcase;  cin.getline(sBuf,256);	//cin >> n_Testcase;
	n_Testcase=atoi(sBuf);
	int ans;	
	for (int i_Testcase=0;  i_Testcase< n_Testcase;i_Testcase++){
		cin.getline(sBuf,256);
		string s=sBuf;
		string s2=NextPerm0(s);
		cout << "Case #" << i_Testcase+1 << ": " << s2 << endl;
	}	
	return 0;
}

