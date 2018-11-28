#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <stdlib.h>

int main()
{
    FILE *fpi, *fpo;
    char line_feed[100], se[100][100], q[1000][100], *pse[100], *pq[1000], temp_se[100][100];   // max 100 character for a search engine name
    int num_of_cases,num_of_se,num_of_q ,x=0,y=0,z=0, y1=0,y2=0,temp_num_of_se=0,temp_num_of_switch=0, charbychar=0,se_len=0,z2=0;
    
    
 // Search engine name and query array being reinitialised   
    for (x=0 ; x<100; x++)
     {
             *se[x] = '\0';
             pse[x] = se[x];
             }
     
    for (x=0 ; x<1000; x++)
     {
             *q[x] = '\0';
             pq[x] = q[x];
     }
     
     

    fpi=fopen("c:\\dev-cpp\\codejam\\input\\A-large.in","r");
    fpo=fopen("c:\\dev-cpp\\codejam\\output\\A-large.out","w");
    if (!fpi )
       {
        printf("failed");
        getch();
        return 1;
        }
//        num_of_cases = int (fgets(s,1000,fpi));
        fgets(line_feed,101,fpi);
    num_of_cases = atoi(line_feed);
    
    
    
    for(x=0;x<num_of_cases;x++)                  //cases start here
    {
//    fprintf(fpo,"\ncase number %d\n",x+1) ;                                                                     
    
    
                   {                                //reinitialise all the se and q to null     - done twice ... will remove if time remains.better do at the end. will require less reinitialization - will only require as many as the number of se and q present                                                   
                    for (z=0 ; z<100; z++)
     {
             *se[z] = '\0';
             pse[z] = se[z];
             }
     
    for (z=0 ; z<1000; z++)
     {
             *q[z] = '\0';
             pq[z] = q[z];
     }
                   }                                //reinitialise all the se and q to null - DONE                                                                     
              
              
              
              
              
              
              
                   
              
                                                 
      fgets(line_feed,101,fpi);                   // read number of search engine - integer
      num_of_se = atoi(line_feed);
      
      for(y1=0;y1<num_of_se;y1++)
                              {
                                  fgets(se[y1],101,fpi);
//                                fprintf(fpo,"%d - SE - %s",y1+1, se[y1]);
                                  }
  //                                fprintf(fpo,"\n");
                                  
                                  
                                  
                                  
      fgets(line_feed,101,fpi);                   // read number of queries - integer
      num_of_q = atoi(line_feed);
      
       for(y2=0;y2<num_of_q;y2++)
                              {
                                  fgets(q[y2],101,fpi);
    //                            fprintf(fpo,"%d - Q - %s",y2+1, q[y2]);
                                  }                                          









temp_num_of_se = 0;
temp_num_of_switch = 0;
// the real calculation begins

for(y2=0;y2<num_of_q;y2++)
{
                          
                          if(temp_num_of_se==0)                              //step 2: preparing again if switch just occured
                                  {
                                                                             
//                                                                             fprintf(fpo,"number of se = %d \n",num_of_se);
                                  for(z=0;z<num_of_se;z++)
                                  {
                                 // se_len=strlen(se[z]);
//                                  fprintf(fpo,"\n strlength = %d",se_len);
                                 // for(z2=0;z2<se_len;z2++);
                                 // {
                                                               // fprintf(fpo,"se[z] [char by char 1 ] = %s\n",temp_se[z]);
                                  strcpy(temp_se[z],se[z]);
                                                                //fprintf(fpo,"se[z] [char by char 2 ] = %s\n",temp_se[z]);
                                 // }
                                  }
                                  
                                  
                                  temp_num_of_se = num_of_se; 
                                  }
                                  
//                                  fprintf(fpo,"temp_se[0] = %s  BUT se[1] = %s and temp_num_of_se = %d",temp_se[0],se[1],temp_num_of_se);                                                // step 2 - DONE

                          
                          
  for(y1=0;y1<num_of_se;y1++)
                             {
                                                               
                             
                             
                             if(!strcmp(temp_se[y1],q[y2]  )) // if string comparison is successful!!!!
                             { 
                             temp_se[y1][0]= '\0';
                             temp_num_of_se=temp_num_of_se - 1;
                             if (temp_num_of_se==0)
                                {
                                temp_num_of_switch++;
                             
                                }
                             }
                             else
                             {
//                                 fprintf(fpo, "NEVER BEEN THERE FOR  temp_se:%s , q:%s\n",temp_se[y1],q[y2]);
                             }
                             
                             
                             
                             
                             
                             }
                             
  if (temp_num_of_se==0)
                                {
                                y2--;
                             
                                }
                          
}





fprintf(fpo,"Case #%d: %d\n",x+1 ,temp_num_of_switch);


    } // 20 cases loop end
    
    
    
    
    
        
        
        
        
        
    fclose(fpi);
    
    
    
    //for(x=0;x<10;x++)
//    printf("%s, - %s",temp_se[x],q[x]);
    
    
    fclose(fpo);
//    getch();
    return 0;
}
