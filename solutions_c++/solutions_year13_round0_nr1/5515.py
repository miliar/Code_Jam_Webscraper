/*
 * QA.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: BarbaraW
 */
#include <cstdio>
#include <stdio.h>
#include <string>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;

char checkRow(char map[4][4]){
	char result='N';
	char cur='\0';
	bool dot=false;
	for(int i=0;i<4;i++){
		cur='\0';
		for(int j=0;j<4;j++){
			dot|=map[i][j]=='.';
			if(cur=='\0'&&(map[i][j]=='X'||map[i][j]=='O')){
				cur=map[i][j];
				continue;
			}
			if(map[i][j]=='T'||map[i][j]==cur){
				if(j==3){
					if(result=='N')
						result=cur;
					else{
						return 'D';
					}
				}
				continue;
			}
			else{
				break;
			}
		}
	}
	if(!dot&result=='N') result='D';
	return result;
}

char checkCol(char map[4][4]){
	char result='N';
	char cur='\0';
	for(int j=0;j<4;j++){
		cur='\0';
		for(int i=0;i<4;i++){
			if(cur=='\0'&&(map[i][j]=='X'||map[i][j]=='O')){
				cur=map[i][j];
				continue;
			}
			if(map[i][j]=='T'||map[i][j]==cur){
				if(i==3){
					if(result=='N')
						result=cur;
					else{
						return 'D';
					}
				}
				continue;
			}
			else{
				break;
			}
		}
	}
	return result;
}

/**
 *  0123
 * 0XXXX
 * 1XXXX
 * 2XXXX
 * 3XXXX
 */
char checkDia(char map[4][4]){
	char result='N';
	char cur='\0';
	for(int j=0;j<4;j++){
		if(cur=='\0'&&(map[j][j]=='X'||map[j][j]=='O')){
						cur=map[j][j];
						continue;
					}
					if(map[j][j]=='T'||map[j][j]==cur){
						if(j==3){
							if(result=='N')
								result=cur;
							else{
								return 'D';
							}
						}
						continue;
					}
					else{
						break;
					}
	}
	cur='\0';
	for(int j=0;j<4;j++){
		int i=3-j;
		if(cur=='\0'&&(map[i][j]=='X'||map[i][j]=='O')){
			cur=map[i][j];
			continue;
		}
		if(map[i][j]=='T'||map[i][j]==cur){
			if(j==3){
				if(result=='N')
					result=cur;
				else{
					return 'D';
				}
			}
			continue;
		}
		else{
			break;
		}
	}
	return result;
}

int main(){
 int total2,total;
 FILE * fl=fopen("A-small-attempt2.in","r");
 FILE* fo= fopen("outA", "w");
 fscanf(fl,"%d",&total2);
 total=total2;
 char cr[4][4];
 for(int i=0;i<total;i++){
	 for(int j=0;j<4;j++){
		 fscanf(fl,"%4s",(cr[j]));
	 }
	 char r3[3];
	 r3[0]=checkRow(cr);
	 r3[1]=checkCol(cr);
	 r3[2]=checkDia(cr);
	 char cur='\0';
	 string line("");
	 for(int k=0; k<3;k++){
		 if(r3[k]=='D'){
			 fprintf(fo, "Case #%d: Draw\n",i+1);
			 line="Draw";
			 break;
		 }
	 	else if(r3[k]=='X'||r3[k]=='O'){
			 if(cur=='\0'){
				 cur=r3[k];
			 }else if(r3[k]!=cur){
				 fprintf(fo, "Case #%d: Draw\n",i+1);
				 line="Draw";
				 break;
			 }
		 }
	 }
	 if(cur=='\0'&&line.length()<=0){
		 fprintf(fo, "Case #%d: Game has not completed\n",i+1);
		 //line="Game has not completed";
	 }
	 else if(line.length()<=0){
		 if(cur=='X'){
			 fprintf(fo, "Case #%d: X won\n",i+1);
		 }
		 else{
			 fprintf(fo, "Case #%d: O won\n",i+1);
		 }
	 }
	 //printf("Line: %s",line.c_str());
 }
 fclose(fl);
 fclose(fo);

}


