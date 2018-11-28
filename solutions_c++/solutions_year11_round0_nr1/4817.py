#include<conio.h>
#include<iostream.h>
#include<stdio.h>
#include<stdlib.h>
#include<fstream.h>
#include<math.h>

void main(){
 ifstream in;
 ofstream out;
 int tcase=0,boPosButton=1,bbPosButton=1,timeTotal=0,pairs=0,moveTo=0,lastMoveo=0,lastMoveb=0;
 char bot='A';
	out.open("output2.txt",ios::binary);
 	 in.open("A-large.in",ios::binary);
    in>>tcase;
    for(int i=1;i<=tcase;i++){
				in>>pairs;
            timeTotal=0;
            lastMoveb=0;lastMoveo=0;
            boPosButton=1;bbPosButton=1;
            for(int j=1;j<=pairs;j++){
               in>>bot;
               in>>moveTo;
               switch(bot){
               case 'O':
                  if(abs(boPosButton-moveTo)<=lastMoveo){
                  	timeTotal+=1;
                     lastMoveb+=1;
                     lastMoveo=0;
                     boPosButton=moveTo;
                  }
                  else
                  {
                  	timeTotal+=abs(moveTo-boPosButton)-lastMoveo+1;
                     lastMoveb+=abs(moveTo-boPosButton)-lastMoveo+1;
                     lastMoveo=0;
                     boPosButton=moveTo;
                  }
               break;
               case 'B':
                  if(abs(bbPosButton-moveTo)<=lastMoveb){
                  	timeTotal+=1;
                     lastMoveo+=1;
                     lastMoveb=0;
                     bbPosButton=moveTo;
                  }
                  else
                  {
                  	timeTotal+=abs(moveTo-bbPosButton)-lastMoveb+1;
                     lastMoveo+=abs(moveTo-bbPosButton)-lastMoveb+1;
                     lastMoveb=0;
                     bbPosButton=moveTo;
                  }
               break;

               }
            }
				out<<"Case #"<<i<<": "<<timeTotal<<endl;
    }
// */

	in.close();
   out.close();

}