// writing on a text file
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main () {
  //open file 
  ifstream inf ("A-large.in");
  ofstream outf ("a-1.txt");
   int l , d, n,p;
   char temp;
    if (inf.is_open())
  {   
        
  }
    else cout << "Unable to open file";
 
 
 
  int i,we;
        i=0;
        char r[10];
        temp=inf.get();  
        
     //get l
      while(temp !=32 && temp!= 10)
       {  r[i]=temp;
                          temp=inf.get();  
                 i= i+1;                  
     }         
     i=0;
        l = atoi(r);
  
  //get d
   temp=inf.get();  
      while(temp !=32 && temp!= 10)
       {      
                  r[i]=temp;
                  temp=inf.get();  
                 i= i+1;                  
     }         
  i=0;
        d = atoi(r);
        
        //get n;
  temp=inf.get();  
       // l = atoi(temp.c_str());
      while(temp !=32 && temp!= 10)
       {    
                  r[i]=temp;        
                  temp=inf.get();  
                 i= i+1;                  
     }         
   i=0;
        n = atoi(r);
  
 //cout<<l<<endl;
  //cout<<d<<endl;
  //cout<<n<<endl;
    //good
    
 char w[6000][20];

// get the testing word
 for(int j=0; j<d; j++)
  {
        i=0;
      temp=inf.get();  
    //cout<<temp<<endl;      
           while(temp !=32 && temp!= 10) //space \n
       {
                
                  w[j][i]=temp;
                
                  temp=inf.get();  
                 i= i+1;                  
    }
    
           }
           //good
         
      i=0;
     int h, ii, iii,ee; 
      char test[30];
   char test2;
   char test3[30];
   int o[6000][30];
   int sos[6000][30];
   int ans, one;
  char ttemp;
  //get the constraint 
  int a,b,c,count;
  for (int ff=0; ff<500;ff++){
      ee=0;
for(int kwe=0; kwe<l; kwe++)
{
        ttemp=inf.get(); 
      //  cout<<ttemp<<endl;
//int o[600][100];
b=0;
a=0;
c=0;
count=0;
     if (ttemp==40)
     {
                   a=1;
          ttemp=inf.get();           
                    while (ttemp>96 && ttemp <123){
                        test[count]=ttemp;
                        count++;
                        
                         ttemp=inf.get();   
                          }//while
      //     ttemp=inf.get();                
           // cout<<temp<<endl;                     
                          
            //cout<<test<<endl;      
                   }  //if   
       else if(ttemp>96 && ttemp <123)
{
       b=1;
       test2=ttemp;
       
       }//else if
/*if (b==1)
{
       cout<<test2<<endl;
        }
else if (a==1)
{
     for (int jkl=0; jkl<count;jkl++)
       cout<<test[jkl];
        cout<<endl;
        }
*/
for(int yy=0; yy<d;yy++){
for(int yyy=0; yyy<l;yyy++){
        
        o[yy][yyy]=3;
 //cout<< o[yy][yyy];
       
        
        
        }
    //    cout<<endl;
        }
//check they are the same or not by each digit 
     if (a==1){
       for (int zw=0; zw<count; zw++)
       {
        for (int z=0; z<d; z++)
         { 
         if (w[z][kwe]==test[zw])        
                 {
                                      
                o[z][kwe]=1;   //row , which letter                  
                 }
           else if( o[z][kwe]==3){
                         o[z][kwe]=0; 
                     }
    //         cout<<o[z][k]<<endl;
            }//z

}   //zw
}//if
else if(b==1){
      for (int z=0; z<d; z++)
         { 
         if (w[z][kwe]==test2)        
                 {
                                      
                o[z][kwe]=1;   //row , which letter                  
                 }
           else {
                          o[z][kwe]=0; 
                      }
     
     
     }//z
     
     
     }//else
     /*
for(int yy=0; yy<d;yy++){
for(int yyy=0; yyy<l;yyy++){
        
       // o[yy][yyy]=3;
 cout<< o[yy][yyy];
       
        
        
        }
        cout<<endl;
        }
       */ 
  for(int yy=0; yy<d;yy++){

        
        sos[yy][ee]=o[yy][ee];
// cout<< sos[yy][ee];
       
        
        
        }
     
          /*
        for(int yy=0; yy<d;yy++){
for(int yyy=0; yyy<l;yyy++){
        
       // o[yy][yyy]=3;
 cout<< sos[yy][yyy];
       
        
        
        }
        cout<<endl;
        }
*/



//delete o;
ee++;
}//for kwe


ans=0;
one=0;
   for (int qw= 0; qw<d;qw++){



one=0;
for (int ed= 0; ed<l;ed++){
if (sos[qw][ed]==1){
                  one++;
                  }

}//for
if (one==l)
{ans++;
}


}//for

 outf << "Case #"<<ff+1<<": "<<ans<<endl;
cout<< "Case #"<<ff+1<<": "<<ans<<endl;

 ttemp=inf.get();




}//ff 
 
 outf.close();
 
 
 
 
 
 
  system ("pause");
  return 0;
}

  
  
