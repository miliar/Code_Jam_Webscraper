// jam1.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>

#include <set>
#include <cstdio>
#include <algorithm>
#include <math.h>
using namespace std;

void fun(char buf[],int n, int i);
int MAX(int* tn, int i, int j){
	int mix = 0;
	for(int k=i; k<=j; k++){
		if(mix<tn[k])
			mix = tn[k];
	}
	return mix;
}

int Find(char* buf, int i, int j, char c){
	for(int k=i; k<=j; k++){
		if(buf[k] == c)
			return k;
	}
	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* infile = fopen("a.in", "r");
	char buf[300];
	int n = 0;
	fgets(buf, 300, infile);
	
	int cases = atoi(buf);
	
	for(int i=1; i<=cases; i++){
		memset(buf, 0, 300);
		n = strlen(fgets(buf, 300, infile));
		if(n==2)
			cout<< "Case #" << i << ": " << 1 <<endl; 
		else
			fun(buf, n-1, i);
	}

	return 0;
}

void fun(char buf[], int n, int kk){
	//cout<< "Case #" << i << ": " << res[i-1] <<endl; 
	int b[36]={0};
	for(int i=0; i<n; i++){
		if(buf[i]>='0' && buf[i]<='9'){
			b[buf[i]-'0'] += 1;
		}else if(buf[i]>='a' && buf[i]<='z'){
			b[buf[i]-'a'+10] += 1;
		}
	}
	
	int base = 0;
	for(int j=0; j<36; j++){
		if(b[j] != 0)
			++base;
	}

	if(base == 1)
		base = 2;
	

	//set<char,int> p;
	
//	string num = "1";
//	int l = 0;
	//p.insert(buf[0], 1);
	int* tn = (int*)malloc(4*n);
	memset(tn, 0, 4*n);
	tn[0] = 1;
	bool flag = 0;
	char p = -1;
	for(int k=1; k<n; k++){
		if((p=Find(buf,0,k-1,buf[k]))!=-1){
				tn[k] = tn[p];

		}else{
			if(!flag){
				tn[k] = 0;
				flag = true;
			}else{
				tn[k] = MAX(tn, 0, k-1)+1;
				
			}
			
		}
	}
	unsigned int mnum = 0;
	for(int i=0; i<n; i++){
	//	cout<<"tn ="<<tn[i]<<endl;
		mnum += (tn[i]*pow((double)base, n-i-1));
	}
	
	cout<< "Case #" << kk << ": " << mnum <<endl; 

	
}
