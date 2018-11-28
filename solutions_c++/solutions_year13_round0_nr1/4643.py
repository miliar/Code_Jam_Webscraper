#include <stdio.h>
#include <conio.h>
#include<iostream>
#include<fstream>
#include<string.h>
#define S scanf
#define P printf

using namespace std;
int main()

{
    char a[4][4],c;
    int k,d,i,j,n,b=0,m,y;
    ifstream ifile("C:/New folder/ip1.txt");
    ofstream ofile("C:/New folder/out1.txt");
    ifile>>n;
    //ifile>>c;
    y=n;
 while(n>0){
           d=0;k=0;
            for(i=0;i<4;i++){
                             for(j=0;j<4;j++){
                                              ifile>>a[i][j];
                                             
                                              }
                                              
                                              //ifile>>c;
                                              //P("\n");
                                              }
                                              m=0;
     //printf("%s",a[0]);
     for(i=0;i<4;i++)
     { //P("\n%c%c",a,a+1);
     
 //    P("HI%cBUURAAAAAA!!!\n",a[i][0]);
    if((a[i][0]=='X' || a[i][0]=='T')&& (a[i][1]=='X' || a[i][1]=='T') && (a[i][2]=='X' || a[i][2]=='T') && (a[i][3]=='X' || a[i][3]=='T'))
    {
       ofile<<"Case #"<<y-n+1<<": X won"<<endl;
       ++d;
       break;
     //  P("%d\n",d);
       }  
          
    else if((a[i][0]=='O' || a[i][0]=='T')&& (a[i][1]=='O' || a[i][1]=='T') && (a[i][2]=='O' || a[i][2]=='T') && (a[i][3]=='O' || a[i][3]=='T'))
    {
       ofile<<"Case #"<<y-n+1<<": O won"<<endl;
       ++d;
       break;
       }    
    else if((a[0][i]=='X' || a[0][i]=='T') && (a[1][i]=='X' || a[1][i]=='T') && (a[2][i]=='X' || a[2][i]=='T')&& (a[3][i]=='X' || a[3][i]=='T'))
    {   ofile<<"Case #"<<y-n+1<<": X won"<<endl;  
        ++d;
        break;
        }
         
    else if((a[0][i]=='O' || a[0][i]=='T') && (a[1][i]=='O' || a[1][i]=='T') && (a[2][i]=='O' || a[2][i]=='T')&& (a[3][i]=='O' || a[3][i]=='T'))
     {  //printf("1 %d",i);
         ofile<<"Case #"<<y-n+1<<": O won"<<endl;
       ++d;
       break;
       }
    else if((a[0][0]=='O'|| a[0][0]=='T') && (a[1][1]=='O'|| a[1][1]=='T') && (a[2][2]=='O'|| a[2][2]=='T') && (a[3][3]=='O'|| a[3][3]=='T'))    
      {
         ofile<<"Case #"<<y-n+1<<": O won"<<endl;
         ++d;
         break;
         }    
    else if((a[0][0]=='X'|| a[0][0]=='T') && (a[1][1]=='X'|| a[1][1]=='T') && (a[2][2]=='X'|| a[2][2]=='T') && (a[3][3]=='X'|| a[3][3]=='T'))    
       {
       ofile<<"Case #"<<y-n+1<<": X won"<<endl;
        ++d;
        break;
        }
        else if((a[3][0]=='O'|| a[3][0]=='T') && (a[2][1]=='O'|| a[2][1]=='T') && (a[1][2]=='O'|| a[1][2]=='T') && (a[0][3]=='O'|| a[0][3]=='T'))    
      {
         ofile<<"Case #"<<y-n+1<<": O won"<<endl;
         ++d;
         break;
         }    
    else if((a[3][0]=='X'|| a[3][0]=='T') && (a[2][1]=='X'|| a[2][1]=='T') && (a[1][2]=='X'|| a[1][2]=='T') && (a[0][3]=='X'|| a[0][3]=='T'))    
       {
       ofile<<"Case #"<<y-n+1<<": X won"<<endl;
        ++d;
        break;
        }      
           for(j=0;j<4;j++){
                     if(a[i][j]=='.')
                     ++m;
                     }
                     
//P("%d",d);       
}

   if (m==0 && d==0)
   {
            ofile<<"Case #"<<y-n+1<<": Draw"<<endl;
            ++k;
}
   else if(m!=0 && d==0 && k==0)
   ofile<<"Case #"<<y-n+1<<": Game has not completed"<<endl;

             
         //    if(a[0][0]=='X')
           //  P("BURRRRRAAAAAAA\N");
           
          // check(a);                                                 
                                              
     
 n--;
 }


     
    getch();
    return 0;
}




