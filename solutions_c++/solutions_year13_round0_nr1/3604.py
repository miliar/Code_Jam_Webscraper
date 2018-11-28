// 2013.cpp : 定义控制台应用程序的入口点。
//
//a=b==1&&*p+++d*e;
//#include "stdafx.h"
#include <iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include <iomanip>
#include <fstream>
 using namespace std;
 int main()
 {
	 ifstream inFile;  
	 ofstream outFile;  
	 inFile.open("A-large.in");  
	 outFile.open("outData.out");
	 int T;
	 inFile>>T;
	 int a[4][4],t;
	 string strt;
	 bool isdraw,isover;
	 for(int icases=1;icases<=T;icases++)
	 {
		 memset(a,0,4*16);
		 isdraw=true;
		 isover=false;
		 for(int i=0;i<4;i++)
		 {
			 inFile>>strt;
			 for(int j=0;j<4;j++)
			 {
				 if(strt[j]=='T')strt[j]=1;
				 else if(strt[j]=='.')strt[j]=0;
				 else if(strt[j]=='X')strt[j]=2;
				 else strt[j]=3;
			 }
			 a[i][0]=strt[0];
			 a[i][1]=strt[1];
			 a[i][2]=strt[2];
			 a[i][3]=strt[3];
		 }
		 for(int i=0;i<4;i++)
		 {
			t=a[i][0]*a[i][1]*a[i][2]*a[i][3];
			if(t!=0)
			{
				if(t==8||t==16){outFile<<"Case #"<<icases<<": X won"<<endl;isover=true;break;}
				if(t==81||t==27){outFile<<"Case #"<<icases<<": O won"<<endl;isover=true;break;}
			}
			else isdraw=false;
			t=a[0][i]*a[1][i]*a[2][i]*a[3][i];
			if(t!=0)
			{
				if(t==8||t==16){outFile<<"Case #"<<icases<<": X won"<<endl;isover=true;break;}
				if(t==81||t==27){outFile<<"Case #"<<icases<<": O won"<<endl;isover=true;break;}
			}
			else isdraw=false;
		 }
		 if(!isover)
		 {
		 		t=a[0][0]*a[1][1]*a[2][2]*a[3][3];
			if(t!=0)
			{
				if(t==8||t==16)
				{
					outFile<<"Case #"<<icases<<": X won"<<endl;
					isover=true;
				}
				if(t==81||t==27){outFile<<"Case #"<<icases<<": O won"<<endl;isover=true;}
			}
			else isdraw=false;
				t=a[0][3]*a[1][2]*a[2][1]*a[3][0];
			if(t!=0)
			{
				if(t==8||t==16){outFile<<"Case #"<<icases<<": X won"<<endl;isover=true;}
				if(t==81||t==27){outFile<<"Case #"<<icases<<": O won"<<endl;isover=true;}
			}
			else isdraw=false;
		 }
		 if(!isover&&isdraw)outFile<<"Case #"<<icases<<": Draw"<<endl;
		 if(!isover&&!isdraw)outFile<<"Case #"<<icases<<": Game has not completed"<<endl;
	 }
	  inFile.close();  
	  outFile.close();
 }
