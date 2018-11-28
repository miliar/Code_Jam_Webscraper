#include <cstdio>
#include <string>

using namespace std;
int esta,bx,by;

void determinar()
{
    if(bx==4) esta=1;
    else if(by==4) esta=2;
}


int main(int argc, char **argv) {
	int NN,in;
	int d,pu;
	char M[10][10];
	int i,j;
	char L,nada;

	in=1;
	
//	printf(" --------jajaja:gtrgdfvbdfvfd- %c ---", L); 
	
	NN=2;
  scanf("%d", &NN);
  //printf(" --------jajaja:----------"); 
  
  	
while (in<=NN)
{

	
	for(i=0;i<4;i++)
	  scanf("%s", &M[i]);
	
//	  printf(" --------Case #%c:----------",  M[1][3]); 






	esta=0;
    pu=0;
	i=0;
	while(i<4){
       j=0;
       bx=0;
       by=0;
       while(j<4){
          L=M[i][j];
          if (L=='X')bx++;
          else{
             if(L=='O') by++;
             else {
                  if(L=='T'){bx++;by++;}
                  else pu=1;
             }
          }
       j++;
       }     
    //   printf(" \n-- %d ----- %d ------ %d ----",  bx,by,pu); 
       	determinar();
  //    	 printf(" \nESTAdo:-- %d ----", esta); 
       	 
       	if ( esta>0) i=4;
       	
       i++;      
    }
	

////VERTICAL	 
	
	if(esta==0)
	{    
	         	i=0;
     while(i<4){
       j=0;
       bx=0;
       by=0;
       while(j<4){
          L=M[j][i];
          if (L=='X')bx++;
          else{
             if(L=='O') by++;
             else {
                  if(L=='T'){bx++;by++;}
                  else pu=1;
             }
          }
       j++;
       }   
       determinar();
       //printf(" \n-- %d ----- %d ------ %d ----",  bx,by,pu); 
       if ( esta>0) i=4;
       
       i++;      
     }

    }
    ////DIAGONAL
    if(esta==0)
	{    
	    i=0;
	    bx=0;
       by=0;
     while(i<4){
     
          L=M[i][i];
          if (L=='X')bx++;
          else{
             if(L=='O') by++;
             else {
                  if(L=='T'){bx++;by++;
                  }
                  else pu=1;
             }
          }
         i++;   
       }   
       determinar();          
      }
      
      //otra diagonal
       if(esta==0)
	{    
	    i=0;
	    bx=0;
       by=0;
     while(i<4){
     
          L=M[i][3-i];
          if (L=='X')bx++;
          else{
             if(L=='O') by++;
             else {
                  if(L=='T'){bx++;by++;
                  }
                  else pu=1;
             }
          }
         i++;   
       }   
       determinar();          
      }
    ///FINAL
    
    if(esta==0) { if (pu==1) esta=4; else esta=3;} 
  
  
  
     //	 printf(" \nESTAdofinAL:-- %d ----", esta); 
     	 
   printf("case %d:",in);  	 
  switch (esta)
  {
     case 1:  printf("X won\n");break;
     case 2:  printf("O won\n");break;
     case 3:  printf("Draw\n");break;
     case 4:  printf("Game has not completed\n");break;
  }
  in++;
  // scanf("%c",&nada);
}

    
    
    
	scanf("%d", &in);
		
	return 0;
}

