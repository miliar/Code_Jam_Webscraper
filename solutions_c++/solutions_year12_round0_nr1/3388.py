/*
ID: bryantr1
PROG: 3lines
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdio>
#include <math.h>
#include <cstring>

using namespace std;

struct Cow{
	int x, y;
	bool line;
};

int 
check(Cow *ab, int &a){
	for (int i=0;i<a;i++){
		if (ab[i].line==false){
			return i;
		}
	}
	return -1;
}

int
main()
{  
	int n;
	ofstream fout("3lines.out");
    ifstream fin("input.txt");
	fin>>n;
    Cow cows[n];
	Cow cows1[n];
	for (int i=0;i<n; i++){
		fin>> cows[i].x>> cows[i].y;
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows[i].line=false;
		cows1[i].line=false;
	}
	int a,b,c,a1;
	//KLSDHJFKLSDJFKLJSDKLFJDSkldfgdfghJKHSDJKHFUIDSHFJKHSDFHUIEWHF
	cows1[0].line=true;
	for (int i=1;i<n; i++){
		if(cows1[i].x==cows1[0].x){
			cows1[i].line=true;
				cout<<"dfs ";
			}
	}
	a=check(cows1, n);
	//cout<<a;
	if (a>0){
		cows1[a].line=true;
		for (int i=a;i<n;i++){
			if(cows1[i].x==cows1[a].x){
				cows1[i].line=true;
			}
		}
		a1=check(cows1,n);
		//cout<<a1;
		if (a1>0){
			for (int i=a1;i<n;i++){
				if(cows1[i].x==cows1[a1].x){
					cows1[i].line=true;
				}
			}
			if (check(cows1,n)<0)  {
				b=1;
				cout<<b;
				return 0;	
			}
		}
		else {
			b=1;
			cout<<b;
			return 0;
		}
		
	}
	else {
		b=1;
		cout<<b;
		return 0;
	}
	for (int i=0;i<n; i++){
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows1[i].line=false;
	}
	//JDHSFKSDJFHSDJKFHSDEJKFHSDJKFHSDJKFHD
		cows1[0].line=true;
	for (int i=1;i<n; i++){
		if(cows1[i].x==cows1[0].x){
			cows1[i].line=true;
				cout<<"dfs ";
			}
	}
	a=check(cows1, n);
	if (a>0){
		cows1[a].line=true;
		for (int i=a;i<n;i++){
			if(cows1[i].x==cows1[a].x){
				cows1[i].line=true;
			}
		}
		a1=check(cows1,n);
		if (a1>0){
			for (int i=a1;i<n;i++){
				if(cows1[i].y==cows1[a1].y){
					cows1[i].line=true;
				}
			}
			if (check(cows1,n)<0)  {
				b=1;
				cout<<b;
				return 0;	
			}
		}
		else {
			b=1;
			cout<<b;
			return 0;
		}
		
	}
	else {
		b=1;
		cout<<b;
		return 0;
	}
	for (int i=0;i<n; i++){
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows1[i].line=false;
	}
	//SDKFHJSDIOFHJSDJKFHJDJKSHFSDJHFDJSHFDJKSHF
		cows1[0].line=true;
	for (int i=1;i<n; i++){
		if(cows1[i].x==cows1[0].x){
			cows1[i].line=true;
				cout<<"dfs ";
			}
	}
	a=check(cows1, n);
	if (a>0){
		cows1[a].line=true;
		for (int i=a;i<n;i++){
			if(cows1[i].y==cows1[a].y){
				cows1[i].line=true;
			}
		}
		a1=check(cows1,n);
		if (a1>0){
			for (int i=a1;i<n;i++){
				if(cows1[i].x==cows1[a1].x){
					cows1[i].line=true;
				}
			}
			if (check(cows1,n)<0)  {
				b=1;
				cout<<b;
				return 0;	
			}
		}
		else {
			b=1;
			cout<<b;
			return 0;
		}
		
	}
	else {
		b=1;
		cout<<b;
		return 0;
	}
	for (int i=0;i<n; i++){
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows1[i].line=false;
	}
	//DSFHJKLSDJFJSDFKJSDKFJSDJFKSDJFKSDJFKLSDJFKLSDJFKLSDJFKLJ
		cows1[0].line=true;
	for (int i=1;i<n; i++){
		if(cows1[i].x==cows1[0].x){
			cows1[i].line=true;
				cout<<"dfs ";
			}
	}
	a=check(cows1, n);
	if (a>0){
		cows1[a].line=true;
		for (int i=a;i<n;i++){
			if(cows1[i].y==cows1[a].y){
				cows1[i].line=true;
			}
		}
		a1=check(cows1,n);
		if (a1>0){
			for (int i=a1;i<n;i++){
				if(cows1[i].y==cows1[a1].y){
					cows1[i].line=true;
				}
			}
			if (check(cows1,n)<0)  {
				b=1;
				cout<<b;
				return 0;	
			}
		}
		else {
			b=1;
			cout<<b;
			return 0;
		}
		
	}
	else {
		b=1;
		cout<<b;
		return 0;
	}
	for (int i=0;i<n; i++){
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows1[i].line=false;
	}
	// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	//KLSDHJFKLSDJFKLJSDKLFJDSkldfgdfghJKHSDJKHFUIDSHFJKHSDFHUIEWHF
	cows1[0].line=true;
	for (int i=1;i<n; i++){
		if(cows1[i].y==cows1[0].y){
			cows1[i].line=true;
				cout<<"dfs ";
			}
	}
	a=check(cows1, n);
	if (a>0){
		cows1[a].line=true;
		for (int i=a;i<n;i++){
			if(cows1[i].x==cows1[a].x){
				cows1[i].line=true;
			}
		}
		a1=check(cows1,n);
		if (a1>0){
			for (int i=a1;i<n;i++){
				if(cows1[i].x==cows1[a1].x){
					cows1[i].line=true;
				}
			}
			if (check(cows1,n)<0)  {
				b=1;
				cout<<b;
				return 0;	
			}
		}
		else {
			b=1;
			cout<<b;
			return 0;
		}
		
	}
	else {
		b=1;
		cout<<b;
		return 0;
	}
	for (int i=0;i<n; i++){
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows1[i].line=false;
	}
	//JDHSFKSDJFHSDJKFHSDEJKFHSDJKFHSDJKFHD
		cows1[0].line=true;
	for (int i=1;i<n; i++){
		if(cows1[i].y==cows1[0].y){
			cows1[i].line=true;
				cout<<"dfs ";
			}
	}
	a=check(cows1, n);
	if (a>0){
		cows1[a].line=true;
		for (int i=a;i<n;i++){
			if(cows1[i].x==cows1[a].x){
				cows1[i].line=true;
			}
		}
		a1=check(cows1,n);
		if (a1>0){
			for (int i=a1;i<n;i++){
				if(cows1[i].y==cows1[a1].y){
					cows1[i].line=true;
				}
			}
			if (check(cows1,n)<0)  {
				b=1;
				cout<<b;
				return 0;	
			}
		}
		else {
			b=1;
			cout<<b;
			return 0;
		}
		
	}
	else {
		b=1;
		cout<<b;
		return 0;
	}
	for (int i=0;i<n; i++){
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows1[i].line=false;
	}
	//SDKFHJSDIOFHJSDJKFHJDJKSHFSDJHFDJSHFDJKSHF
		cows1[0].line=true;
	for (int i=1;i<n; i++){
		if(cows1[i].y==cows1[0].y){
			cows1[i].line=true;
				cout<<"dfs ";
			}
	}
	a=check(cows1, n);
	if (a>0){
		cows1[a].line=true;
		for (int i=a;i<n;i++){
			if(cows1[i].y==cows1[a].y){
				cows1[i].line=true;
			}
		}
		a1=check(cows1,n);
		if (a1>0){
			for (int i=a1;i<n;i++){
				if(cows1[i].x==cows1[a1].x){
					cows1[i].line=true;
				}
			}
			if (check(cows1,n)<0)  {
				b=1;
				cout<<b;
				return 0;	
			}
		}
		else {
			b=1;
			cout<<b;
			return 0;
		}
		
	}
	else {
		b=1;
		cout<<b;
		return 0;
	}
	for (int i=0;i<n; i++){
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows1[i].line=false;
	}
	//DSFHJKLSDJFJSDFKJSDKFJSDJFKSDJFKSDJFKLSDJFKLSDJFKLSDJFKLJ
		cows1[0].line=true;
	for (int i=1;i<n; i++){
		if(cows1[i].y==cows1[0].y){
			cows1[i].line=true;
				cout<<"dfs ";
			}
	}
	a=check(cows1, n);
	if (a>0){
		cows1[a].line=true;
		for (int i=a;i<n;i++){
			if(cows1[i].y==cows1[a].y){
				cows1[i].line=true;
			}
		}
		a1=check(cows1,n);
		if (a1>0){
			for (int i=a1;i<n;i++){
				if(cows1[i].y==cows1[a1].y){
					cows1[i].line=true;
				}
			}
			if (check(cows1,n)<0)  {
				b=1;
				cout<<b;
				return 0;	
			}
		}
		else {
			b=1;
			cout<<b;
			return 0;
		}
		
	}
	else {
		b=1;
		cout<<b;
		return 0;
	}
	for (int i=0;i<n; i++){
		cows1[i].x=cows[i].x;
		cows1[i].y= cows[i].y;
		cows1[i].line=false;
	}
  //  system("Pause");
	cout<<0;
    return 0;
}


