//
//  main.cpp
//  codeJam_QualificationRound
//
//  Created by Jereneal Kim on 13. 4. 13..
//  Copyright (c) 2013년 Jereneal Kim. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char **argv)
{
	FILE *fp,*inp;
	int n,i,j,k,oWinFlag,xWinFlag,dotFlag=0;
	char arr[5][5]={'0'},tmp;
	fp=fopen(argv[1],"w");
	inp=fopen(argv[2],"r");
	
	fscanf(inp,"%d",&n);
//	scanf("%d",&n);
	
	for(i=1;i<=n;i++){
		for(j=1;j<=4;j++){
			for(k=1;k<=4;k++){
				fscanf(inp,"%c",&tmp);
//				scanf("%c",&tmp);
				if(tmp=='\n'){
					k--;
					continue;
				}
				arr[j][k]=tmp;
			}
		}
		
		
		for(j=1;j<=4;j++){
			oWinFlag=0;
			xWinFlag=0;
			for(k=1;k<=4;k++){
				if(arr[j][k]=='O'){
					oWinFlag++;
				}else if(arr[j][k]=='X'){
					xWinFlag++;
				}else if(arr[j][k]=='T'){
					oWinFlag++;
					xWinFlag++;
				}else{
					dotFlag=1;
				}
			}
			if(oWinFlag==4){
				break;
			}else if(xWinFlag==4){
				break;
			}
			//row
			
			oWinFlag=0;
			xWinFlag=0;
			for(k=1;k<=4;k++){
				if(arr[k][j]=='O'){
					oWinFlag++;
				}else if(arr[k][j]=='X'){
					xWinFlag++;
				}else if(arr[k][j]=='T'){
					oWinFlag++;
					xWinFlag++;
				}else{
					dotFlag=1;
				}
			}
			if(oWinFlag==4){
				break;
			}else if(xWinFlag==4){
				break;
			}
			//column
		}
		
		if(xWinFlag!=4&&oWinFlag!=4){
			oWinFlag=0;
			xWinFlag=0;
			for(k=1;k<=4;k++){
				if(arr[k][k]=='O'){
					oWinFlag++;
				}else if(arr[k][k]=='X'){
					xWinFlag++;
				}else if(arr[k][k]=='T'){
					oWinFlag++;
					xWinFlag++;
				}
			}
		}
		if(xWinFlag!=4&&oWinFlag!=4){
			oWinFlag=0;
			xWinFlag=0;
			for(k=1;k<=4;k++){
				if(arr[k][5-k]=='O'){
					oWinFlag++;
				}else if(arr[k][5-k]=='X'){
					xWinFlag++;
				}else if(arr[k][5-k]=='T'){
					oWinFlag++;
					xWinFlag++;
				}
			}			
		}
		
		fprintf(fp,"Case #%d: ",i);
		printf("Case #%d: ",i);
		if(xWinFlag==4||oWinFlag==4){
			if(xWinFlag==4){
				fprintf(fp,"X won\n");
				printf("X won\n");
			}else{
				fprintf(fp,"O won\n");
				printf("O won\n");
			}
		}else{
			if(dotFlag==1){
				fprintf(fp,"Game has not completed\n");
				printf("Game has not completed\n");
			}else{
				fprintf(fp,"Draw\n");
				printf("Draw\n");
			}
		}
		dotFlag=0;
		
//		for(j=1;j<=4;j++){
//			for(k=1;k<=4;k++){
//				arr[j][k]='0';
//				//initialize
//			}
//		}
	}
	
	
	return 0;
}

