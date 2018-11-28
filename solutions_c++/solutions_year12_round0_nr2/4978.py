#include <stdio.h>
#define LENGTH 3


int main()
{
 int T,i,j,triplet[LENGTH],N,surprises_left,p,out;
 int hold,div;
 char line[25];
 FILE *fpin,*fpout;   
 fpin = fopen("B-large.in","r");
 
 fpout = fopen("A-out.txt","w");
 
 fscanf(fpin,"%d",&T);
 
 
 for(i=0;i<T;i++)
 {
    fgets(line,100,fpin);//clears the line feed from the stream             
    out = 0;
    
    fscanf(fpin,"%d",&N);
    fscanf(fpin,"%d",&surprises_left);
    fscanf(fpin,"%d",&p);
    
    for(j=0;j<N;j++)
                    {
                         fscanf(fpin,"%d",&hold);
                         switch(hold)
                         {
                                     case 30:
                                     case 29:
                                     case 28:
                                          out++;
                                          break;
                                     case 27:
                                     case 26:
                                          if((p==10)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 25:
                                          if(p<10){out++;}
                                          break;
                                     case 24:
                                     case 23:
                                          if((p==9)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 22:
                                          if(p<9){out++;}
                                          break;
                                     case 21:
                                     case 20:
                                          if((p==8)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 19:
                                          if(p<8){out++;}
                                          break;
                                     case 18:
                                     case 17:
                                          if((p==7)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 16:
                                          if(p<7){out++;}
                                          break;
                                     case 15:
                                     case 14:
                                          if((p==6)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 13:
                                          if(p<6){out++;}
                                          break;
                                     case 12:
                                     case 11:
                                          if((p==5)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 10:
                                          if(p<5){out++;}
                                          break;
                                     case 9:
                                     case 8:
                                          if((p==4)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 7:
                                          if(p<4){out++;}
                                          break;
                                     case 6:
                                     case 5:
                                          if((p==3)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 4:
                                          if(p<3){out++;}
                                          break;
                                     case 3:
                                     case 2:
                                          if((p==2)&&(surprises_left!=0)){out++;surprises_left--;}
                                     case 1:
                                          if(p<2){out++;}
                                          break;
                                     case 0:
                                          if(p==0){out++;}
                                          break;
                                          
                                     
                         }
    
                    }
    
    
    fprintf(fpout,"Case #%d: %d\n",i+1,out);
 }
 
 fclose(fpin);
 fclose(fpout);
 return 0;
}

