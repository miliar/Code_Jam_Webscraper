/*****

  Project      :  CodeJam
  Filename     :  Main.cpp
  Author       :  Srikanth Addepalli  
  Purpose      :  To Perfrom CodeJam Algorthim for Google
  Complier	   :  VC++ 6
********/
#define DATALENGTH 7
#include <iostream>
#include <string>
#include <windows.h>
#include <fstream>
#include "AlienWords.h"
using namespace std;
/*** Starting Logging ***/
#define LOG(str) WriteLog(str);
void WriteLog(string str)
{
	SYSTEMTIME st;
	GetLocalTime(&st);
	char sBuf[20];
	sprintf(sBuf,"%02d/%02d %02d:%02d:%02d:%03d",st.wMonth,st.wDay,st.wHour,st.wMinute,st.wSecond,st.wMilliseconds);
	sBuf[18]='|';
	sBuf[19]='\0';
	cout<<sBuf<<str<<std::endl;
}
/*** Ending Logging ***/


/*
Main Routine of the Program
*/
void main(int argc,char *argv[])
  {	
	string InputFileName,OutputFileName;
	if(argc >= 3)
	{
		InputFileName=argv[1];
		OutputFileName=argv[2];
		LOG(string("Using Input File=")+InputFileName.c_str());
		LOG(string("Using Output File=")+OutputFileName.c_str());
	}
	else
	{
		InputFileName="Input.txt";
		OutputFileName="Output.txt";
		LOG(string("Using Default Input File=")+InputFileName.c_str());
		LOG(string("Using Default Output File=")+OutputFileName.c_str());
	}
	CAlienWords Obj(InputFileName,OutputFileName);
	Obj.Start();
}