#include<stdio.h>
#include<stdlib.h>


int main()
{
  FILE *fp,*fp1;
  fp = fopen("B-small-attempt3.in","r");
  fp1 = fopen("output.txt","w");
  if(fp == NULL || fp1 == NULL){
    exit(0);
  }
  int T;
  int output;
  fscanf(fp,"%d",&T);
  int count = T-1;
  int tCount = T;
  int subCount = 0;
  int C;
  int D;
  int N;
  
  char com[4];
  char opp[3];
  while( tCount > 0 )
  {
  	int comFlag = 0;
    int oppFlag = 0;
    int oppFlag1 = 0;
  	fscanf(fp,"%d",&C);
  	if ( C > 0)
  	{
	  	comFlag = 1;
	  	fscanf(fp,"%s",com);
  	}
  	fscanf(fp,"%d",&D);
  	if ( D > 0)
  	{
	  	oppFlag = 1;
	  	fscanf(fp,"%s",opp);
  	}
  	fscanf(fp,"%d",&N);
  	char str[N+1];
    fscanf(fp,"%s",str);
    subCount = N;
    char tmpStr[3*N+1];
    char tmpStr1[3*N+1];
    int tmpCount = 0;
    char tmpChar ='2';
    while( subCount > 0)
    {
    	   	tmpStr[tmpCount++] = str[N-subCount];
    	
    		if( comFlag == 1 && tmpCount >1 ){
		    	if( (tmpStr[tmpCount-1] == com[0] && tmpStr[tmpCount-2] == com[1]) ||
					(tmpStr[tmpCount-1] == com[1] && tmpStr[tmpCount-2] == com[0])){
						//if(tmpStr[tmpCount-2] == tmpChar  ){
						//	oppFlag1 =0;
					//		tmpChar = '2';//Reset
					//	}
						
						tmpCount -= 2;
	    			tmpStr[ tmpCount++] = com[2];
	    		}
		    }
		    if( oppFlag == 1 ){
		    	int cc = tmpCount ;
		    	oppFlag1=0;
		    	while(cc>0){
	    			if( tmpStr[	tmpCount-cc] == opp[0] || tmpStr[tmpCount-cc] == opp[1]){
			    	oppFlag1 = 1;
			    	tmpChar = tmpStr[tmpCount-cc];
			    	break;
			    }
			    cc--;
	    		}
		    	if( oppFlag1 == 1){
	    			if( (tmpStr[tmpCount-1] == opp[0] &&  tmpStr[tmpCount-1] != tmpChar ) || 
						(tmpStr[tmpCount-1] == opp[1] &&  tmpStr[tmpCount-1] != tmpChar	)){
			    		oppFlag1 = 0;//Reset
			    		tmpCount = 0;//Clear element list
			    		tmpChar = '2';//Reset
			    	}
	    			
	    		}//else if( tmpStr[tmpCount-1] == opp[0] || tmpStr[tmpCount-1] == opp[1]){
			    //	oppFlag1 = 1;
			    //	tmpChar = tmpStr[tmpCount-1];
			    //}
    		}
    
    	
    	subCount--;
    }
    tmpStr1[0]='[';
    int j = 1;
    for( int i = 0; i < tmpCount; i++){
    	tmpStr1 [ j++] = tmpStr[i];
    	tmpStr1[j++]=',';
    	tmpStr1[j++]=' ';
    }
    if( tmpCount > 0){
    	tmpStr1[j-2] =']';
    	tmpStr1[j-1]='\0';
    }    	
   	else{
    	tmpStr1[j] =']';
    	tmpStr1[j+1]='\0';
    }
    
    fprintf(fp1,"Case #%d: %s\n",(T-count),tmpStr1);
    count--;
    tCount--;
  }
  fclose(fp);
  fclose(fp1);
  return 1;
} 
