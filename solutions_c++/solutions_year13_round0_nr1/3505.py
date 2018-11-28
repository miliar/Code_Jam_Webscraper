// googleCode.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include<iostream>
#include<stdio.h>
int matrix[4][4];
using namespace std;
int computeX(int i) {
	int sum=0;
	for(int j=0;j<4;j++) {
		sum += matrix[i][j];
	}
	return sum;
};
int computeY(int j) {
	int sum=0;
	for(int i=0;i<4;i++) {
		sum += matrix[i][j];
	}
	return sum;
};
int computeLR() {
	int sum=0;
	for(int i=0; i<4;i++) {
		sum += matrix[i][i];
	}
	return sum;
};
int computeRL() {
	int sum=0;
	for(int i=0; i<4;i++) {
		sum += matrix[3-i][i];
	}
	return sum;
};
int judge(int cases, int sum, bool &win) {
	if (sum >= 4 && sum <=5) {
		cout<<"Case #"<<cases<<": X won"<<endl;
		win = true;
		return 0;
	}
	if (sum >= 11) {
		cout<<"Case #"<<cases<<": O won"<<endl;
		win = true;
		return 0;
	}
	return 1;
};
int main()
{
	freopen("data.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取   
	freopen("data.out","w",stdout); //输出重定向，输出数据将保存在out.txt文件中   
	int t;
	cin>>t;

	char a[5];
	
	for (int x=1; x<=t; x++) {
		bool hasEmpty = false;
		bool win = false;
		for (int i=0; i<4; i++) {
			cin>>a;
			for (int j=0; j<4; j++) {
				if (a[j] == 'X') {
					matrix[i][j] = 1;
				}else if(a[j] == 'O') {
					matrix[i][j] = 3;
				}else if(a[j] == 'T'){
					matrix[i][j] = 2;
				}else {
					matrix[i][j] = -1000;
					hasEmpty = true;
				}
			}
		} //end for [initialize matrix]
		for(int index =0;index <4 ;index++) {
			int com = computeX(index);
			if (judge(x,com,win) == 0) break;
			com = computeY(index);
			if (judge(x,com,win) == 0) break;
		}
		//如果分出胜负  就返回
		if (win) continue;
		int com = computeLR();
		if (judge(x,com,win) == 0) continue;
		com = computeRL();
		if (judge(x,com,win) == 0) continue;
		if (hasEmpty) {
			cout<<"Case #"<<x<<": Game has not completed"<<endl;
			continue;
		}
		cout<<"Case #"<<x<<": Draw"<<endl;
	}
//	fclose(stdin);//关闭文件   
//	fclose(stdout);//关闭文件  
	return 0;
}
/*
char s1[50001],s2[50001];
int compare(int index) {
	int sum = 0;
	for (int i=0; i<strlen(s2); i++ ) {
		if (s1[i+index] != s2[i]) sum ++;
	}
	return sum;
}
int main() {
	int t;
	cin>>t;
	
	for (int cases = 1; cases<=t; cases++) {
		memset(s1,0,50001*sizeof(char));
		memset(s2,0,50001*sizeof(char));
		cin>>s1>>s2;
		int s1len = strlen(s1);
		int s2len = strlen(s2);
		int start = 0,end = s1len-s2len;
		int min = s2len,temp;
		for(int i=0; i<=end; i++ ) {
			temp = compare(i);
			if (temp< min) min = temp;
		}
		cout<<"Case #"<<cases<<": "<<min<<endl;

	}
	return 0;
}
*/