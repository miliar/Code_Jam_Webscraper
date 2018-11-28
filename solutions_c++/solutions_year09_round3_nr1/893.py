// GCJ2009_Round1C_probA.cpp : 定義主控台應用程式的進入點。
//String Test By Robert Jiang 2009.09.12
// Decision Tree
// 我的範本，字串 <->數值，含vector.
#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;


#define MAX_CheckNum 9999999  ////!!!!!! ※10000是不夠大！
int mask[MAX_CheckNum];
#define MAX_testNumber 10000


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

string LTrim(string si){
	int i;
	for (i=0;i<si.length(); i++){
		if (si[i]!=' ')break;
	}
	if (i<si.length()){
		si=MidTail(si,i+1);
	}
	return si;
}
string GetToken(string &s,string sDelimitation){ //s為傳址呼叫！
	s=LTrim(s);
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

#define MAX_getline 256
typedef long long LL;  //int64

LL atoiBase(string s,int base){
	LL L2=0;

	return L2;
}
int main(){	

	char sBuf[MAX_getline];	
	cin.getline(sBuf,MAX_getline);
	int n_Testcase=atoi(sBuf);
	set<char> se;
	for (int i_Testcase=0;i_Testcase < n_Testcase; i_Testcase++){
		cin.getline(sBuf,MAX_getline);
		string sLine=sBuf;
		string s=sLine;
		se.clear();
		for (int i=0;i<s.length();i++){
			se.insert(s[i]);
		}
		//先處理所有的字元，按左到右順序，放入imap，最後再複製imap到imap2並把
		// 最前兩個1,0對調，以後就不會有找不到的情形了 
		int Hash[256];
		for (int i=0;i<256;i++)Hash[i]=-1;
		int HCount=0;
		for (int i=0;i<s.length();i++){
			if (Hash[s[i]] == -1) {Hash[s[i]]=HCount; HCount++;}
		}
		// 01對調
		for (int i=0;i<256;i++){
			if (Hash[i]==0) Hash[i]=1;else if (Hash[i]==1)Hash[i]=0;

		}
		
		
		//cout << "相異字元共有幾個" << se.size() << endl;		
		//第一個字元必是1，第二個字元必是0，以後, 第三個必是3,..
		
		//cout << "相異字元共有幾個" << se.size() << endl;		
		//第一個字元必是1，第二個字元必是0，以後, 第三個必是3,...
		int base; //至少。也應該會是最小！
		int DiffDig=0;
		for (int i=0;i<256;i++){
			if (Hash[i]>-1)  DiffDig++;
		}
		if (DiffDig==1) base =2;
		if (DiffDig==2) base =2;
		if (DiffDig>2) base =DiffDig;		
		LL i64=Hash[s[0]];
		for (int i=1;i<s.length();i++){
			i64=i64*base;
			i64+=Hash[s[i]];
		}		
		cout << "Case #" << 1+i_Testcase << ": " << i64 << endl;	
	}
	return 0;		
}


