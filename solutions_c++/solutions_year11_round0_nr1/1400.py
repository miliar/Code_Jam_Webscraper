#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int diff(int a,int b){
    if(a>b)
      return a-b;
    return b-a;
}

int main(){
    int t,buttons,i,j,k,button[100],ans=0,orangepos,bluepos;
    int nextorangepos,nextbluepos,nextbutton,stepsneeded;
    bool sign;
    char space;
    char colour[100];
    //FILE *fp=fopen("F:/jaminput2.txt","r");
    //FILE *fp2=fopen("F:/jamoutput2.txt","w");
    cin>>t;
    //fscanf(fp,"%d",&t); 
    for(k=1;k<=t;k++){
                     
         orangepos=1; bluepos=1;  ans=0;    
        cin>>buttons;
       //  fscanf(fp,"%d",&buttons);
         for(i=0;i<buttons;i++){
           cin>>colour[i]>>button[i];
           // scanf("%c%d",&colour[i],&button[i]);
           //    fscanf(fp,"%c",&space);
             //  fscanf(fp,"%c",&colour[i]);
               //fscanf(fp,"%d",&button[i]);
            //   cout<<colour[i]<<" "<<button[i]<<endl;
         }
          
         for(i=0;i<buttons;i++){
               if(colour[i]=='O')
               {
                   nextorangepos=button[i];
                   break;                  
               }                
              if(buttons==i) nextorangepos=0;
         }       
         for(i=0;i<buttons;i++){
               if(colour[i]=='B')
               {
                   nextbluepos=button[i];
                   break;                  
               }           
               if(buttons==i) nextbluepos=0;
         } 
         for(i=0;i<buttons;i++){
            nextbutton=button[i];                                        
        
       //     cout<<nextbutton<<" "<<nextorangepos<<" "<<nextbluepos<<endl;
         //   cout<<orangepos<<" "<<bluepos<<endl<<endl;                    
            if(nextbutton==nextorangepos){
                  stepsneeded=diff(orangepos,nextbutton)+1;
                  orangepos=button[i];
                  
                  if(nextbluepos>bluepos)
                      sign=1;
                  else
                      sign=0;
                      
                 if(stepsneeded>=diff(nextbluepos,bluepos)){
                     bluepos=nextbluepos;     
                 }   
                  else
                       {
                        if(sign==1)
                          bluepos+=stepsneeded;
                        else
                           bluepos-=stepsneeded;                       
                      
                      }                  
                  ans+=stepsneeded;    
                                               
                 for(j=i+1;j<buttons;j++){
                 if(colour[j]=='O')
                 {
                   nextorangepos=button[j];
                   break;                  
                 } 
                 if(buttons==i) nextorangepos=0;}
            
            }
            else{
                  stepsneeded=diff(bluepos,nextbutton)+1;
                  bluepos=button[i];
                  if(nextorangepos>orangepos)
                      sign=1;
                  else
                      sign=0;
                      
                 if(stepsneeded>=diff(nextorangepos,orangepos))
                     orangepos=nextorangepos;
                  else
                       {
                        if(sign==1)
                          orangepos+=stepsneeded;
                        else
                           orangepos-=stepsneeded;                       
                      
                      }                  
                 ans+=stepsneeded;    
                 
               for(j=i+1;j<buttons;j++){
               if(colour[j]=='B')
               {
                   nextbluepos=button[j];
                   break;                  
               } 
               if(buttons==i) nextbluepos=0;
               }
                 
                                               
            }                              
            
            
     //        cout<<"steps covered="<<ans<<endl;                   
                                
                                
         
         
                              
                       
         
              //   nextbutton=button[i+1];
         
         
         }    
   //      cout<<"totalsteps="<<ans<<endl<<endl;
                                  
         cout<<ans<<endl;                 
                    
      //   fprintf(fp2,"Case #%d: %d\n",k,ans);      
               
    }          
//    fclose(fp);
  //  fclose(fp2);      
    
    cin>>t;
    
    return 0;
}
