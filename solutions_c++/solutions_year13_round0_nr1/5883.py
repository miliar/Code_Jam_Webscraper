#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

int main()
{
   FILE *fp1;
   errno_t err1;
   if((err1=fopen_s(&fp1,"A-large.in","r"))!=0)
   {  printf("入力ファイルが開けません\n");
      return -1;
   }

   char line[1024];
   int T;
   fgets(line,sizeof(line),fp1);
   sscanf_s(line,"%d",&T);

   vector <string> M(4);
   string str;

   ofstream ofs("A-answer");

   for(int t=0; t<T;t++){  // T-Loop
	   int sign_X=0,sign_O=0,sign_D=1;
	  /*------ M ------------------*/
	   for(int i=0; i<4;i++){
	   fgets(line,sizeof(line),fp1);
       str=line;
	   M[i]=str;
	   }
	  /*---------------------------*/

	   for(int i=0; i<4;i++){ // column
		   if((M[i].substr(0,1)=="X" || M[i].substr(0,1)=="T") && (M[i].substr(1,1) =="X" || M[i].substr(1,1)=="T") && (M[i].substr(2,1)=="X" || M[i].substr(2,1)=="T") && (M[i].substr(3,1)=="X" || M[i].substr(3,1)=="T")){sign_X=1;goto result;} 
           if((M[i].substr(0,1)=="O" || M[i].substr(0,1)=="T") && (M[i].substr(1,1) =="O" || M[i].substr(1,1)=="T") && (M[i].substr(2,1)=="O" || M[i].substr(2,1)=="T") && (M[i].substr(3,1)=="O" || M[i].substr(3,1)=="T")){sign_O=1;goto result;} 
	   }

       for(int j=0; j<4;j++){ // row
		   if((M[0].substr(j,1)=="X" || M[0].substr(j,1)=="T") && (M[1].substr(j,1) =="X" || M[1].substr(j,1)=="T") && (M[2].substr(j,1)=="X" || M[2].substr(j,1)=="T") && (M[3].substr(j,1)=="X" || M[3].substr(j,1)=="T")){sign_X=1;goto result;} 
           if((M[0].substr(j,1)=="O" || M[0].substr(j,1)=="T") && (M[1].substr(j,1) =="O" || M[1].substr(j,1)=="T") && (M[2].substr(j,1)=="O" || M[2].substr(j,1)=="T") && (M[3].substr(j,1)=="O" || M[3].substr(j,1)=="T")){sign_O=1;goto result;} 
	   }

       //diagonal
		   if((M[0].substr(0,1)=="X" || M[0].substr(0,1)=="T") && (M[1].substr(1,1) =="X" || M[1].substr(1,1)=="T") && (M[2].substr(2,1)=="X" || M[2].substr(2,1)=="T") && (M[3].substr(3,1)=="X" || M[3].substr(3,1)=="T")){sign_X=1;goto result;} 
           if((M[0].substr(0,1)=="O" || M[0].substr(0,1)=="T") && (M[1].substr(1,1) =="O" || M[1].substr(1,1)=="T") && (M[2].substr(2,1)=="O" || M[2].substr(2,1)=="T") && (M[3].substr(3,1)=="O" || M[3].substr(3,1)=="T")){sign_O=1;goto result;} 
	       if((M[0].substr(3,1)=="X" || M[0].substr(3,1)=="T") && (M[1].substr(2,1) =="X" || M[1].substr(2,1)=="T") && (M[2].substr(1,1)=="X" || M[2].substr(1,1)=="T") && (M[3].substr(0,1)=="X" || M[3].substr(0,1)=="T")){sign_X=1;goto result;} 
           if((M[0].substr(3,1)=="O" || M[0].substr(3,1)=="T") && (M[1].substr(2,1) =="O" || M[1].substr(2,1)=="T") && (M[2].substr(1,1)=="O" || M[2].substr(1,1)=="T") && (M[3].substr(0,1)=="O" || M[3].substr(0,1)=="T")){sign_O=1;goto result;} 
	   
		   for(int i=0 ;i<4; i++){
			   for(int j=0; j<4; j++){
				   if(M[i].substr(j,1)=="."){sign_D=0; goto result;}
			   }
		   }

result:
        if(sign_X==1){ofs << "Case #" << t+1 << ": " << "X won" <<endl;}
		else if(sign_O==1){ofs << "Case #" << t+1 << ": " << "O won" <<endl;}
		else if(sign_D==1){ofs << "Case #" << t+1 << ": " << "Draw" << endl;}
		else{ofs << "Case #" << t+1 << ": " << "Game has not completed" << endl; }
	   fgets(line,sizeof(line),fp1); // 空白行を読む
   } // T-Loop fin
return 0;
}