#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

   void gameStat(int i);
   int whoWon(char symbole);
     int isNoCompleted();
 


 
    char lines[4][4];
	FILE * in;
	FILE * out;

 main(){
 	 
	int T=-1;


	
	in=fopen("A-large-0.in","r");
	out=fopen("A-large-0.out","w");
	//if( (in!=NULL) && (out!=NULL) )
	fscanf(in,"%d\n",&T);
	
       
    for(int i=0;i<T;i++){
    	for(int j=0;j<4;j++){
    		fscanf(in,"%c%c%c%c\n",&lines[j][0],&lines[j][1],&lines[j][2],&lines[j][3]); 
    	
    	}
    	
    	gameStat(i);
    		fscanf(in,"\n");
    		printf("\n");
    	
    	
    }
	     
	

 }
 
 
 //*************************************************
     int isNoCompleted(){
        
        for(int i=0;i<4;i++)
        { for(int j=0;j<4;j++){
          if( lines[i][j]=='.'){
               return 1;
           }
         }
        
        } 
       return 0;
     
    }
  //********************************************  
    int whoWon(char symbole){
      
      int xNumber=0;
      int tNumber=0;
      
     
      
      //searching in lines
         for(int i=0;i<4;i++)
        { for(int j=0;j<4;j++){
          if(lines[i][j]==symbole) {xNumber++;}
           
          if(lines[i][j]=='T'){tNumber++;}
     
         }
        
        if((xNumber==4)|| (xNumber==3 && tNumber==1)){
                      return 1;}
       xNumber=0;
       tNumber=0;
    
      }
         
       //searching in columns
       xNumber=0;
       tNumber=0;
       for(int i=0;i<4;i++)
        {  for(int j=0;j<4;j++){
           if(lines[j][i]==symbole) {xNumber++;}
           if(lines[j][i]=='T') {tNumber++;}
     
          }
        
        if((xNumber==4)|| (xNumber==3 && tNumber==1)){
                      return 1;
					   }
       xNumber=0;
       tNumber=0;
    
        }
        
         //searching in diag 1
       xNumber=0;
       tNumber=0;
       for(int i=0;i<4;i++){
        
          if(lines[i][i]==symbole){xNumber++;}
          if(lines[i][i]=='T'){tNumber++;}
     
         }
        
        if((xNumber==4)|| (xNumber==3 && tNumber==1)){
                      return 1; 
					  }
       
         //searching in diag 2
       xNumber=0;
       tNumber=0;
       for(int i=0;i<4;i++){
        
          if(lines[i][3-i]==symbole) {xNumber++;}
          if(lines[i][3-i]=='T') {tNumber++;}
     
         }
        
        if((xNumber==4)|| (xNumber==3 && tNumber==1)){
                      return 1;
					   }
        
    
     
     return 0;
  }//end of whoWon
    
    
    //*************************************
     void gameStat(int i){
     if(whoWon('X')){
     
         fprintf(out,"Case #%i: X won\n",i+1);
    }
     else {
		    if(whoWon('O')==1){
		     
		         fprintf(out,"Case #%i: O won\n",i+1);
		     }
		     else{
		            if(isNoCompleted()==1){
		              fprintf(out,"Case #%i: Game has not completed\n",i+1);
		             }
		             else {
		                  fprintf(out,"Case #%i: Draw\n",i+1);
			              }
		      
		      
		         }
        }
    
    }
 
 
