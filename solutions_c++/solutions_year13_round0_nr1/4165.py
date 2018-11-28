//============================================================================
// Name        : test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>     // std::cout, std::ios
#include <sstream>      // std::stringstream

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
using namespace std;
/*
#include "CImg.h"
using namespace cimg_library;
*/
enum state{
  incomplete,
  draw,
  finished
};

int checkWinner(char* line){
    int pos=0;
    bool isDraw=false;
    if(line[pos]=='T')
       pos=1;
    
    if(line[pos]=='.')
        return incomplete;

    char person(line[pos]);
    pos+=1;
    while(pos<4){
        if(line[pos]=='.')
          return incomplete;
        if(line[pos]!=person && line[pos]!='T' )
          isDraw=true;
        pos++;
    }
       
    if(isDraw)
        return draw;
    std::cout << person << " won" << std::endl;
    return finished;    

}

 
void getCase(char* content){
    char col[4];
    memset(col,0,4);
    bool drawGame=true;
    
    for(int i=0;i<4;i++){
       int result= checkWinner(content+i*4);
       if(result==finished)
         return;
       if(result==incomplete)
         drawGame=false;

       for(int j=0;j<4;j++){       
         col[j]=content[i+j*4];
       } 
       if(checkWinner(col)==finished)
         return;
    }

      col[0]=content[0];
      col[1]=content[5];
      col[2]=content[10];      
      col[3]=content[15];
       if(checkWinner(col)==finished)
         return;

      col[0]=content[3];
      col[1]=content[6];
      col[2]=content[9];      
      col[3]=content[12];
       if(checkWinner(col)==finished)
         return;


    if(drawGame)
        std::cout << "Draw" << std::endl;
    else   
        std::cout << "Game has not completed" << std::endl;

}



int main(int argc, char *argv[]) {
string line;
  ifstream myfile(argv[1]);
  int number(0);
  int count(0);
  if (myfile.is_open())
  {
      char content[16];
      int pos=0;
      memset(content,0,16);
      while ( myfile.good() && count<=number)
      {
        getline (myfile,line);
        if(number==0)  
            number=atoi(line.c_str());
  
        if(line[0]=='X' || line[0]=='T' || line[0]=='O' || line[0]=='.'){
          for(int i=0;i<4;i++){
            content[pos]=line[i];
            pos++;
          }    
          if(pos==16){
            count++;
            std::cout << "Case #" << count<< ": " ; 
            getCase(content);
            pos=0;
            memset(content,0,16);
          }
        }
      }  
    myfile.close();
  }

  return 0;
}


/*
  for(int i=89;i<99;i++){  
    const char* temp("/home/thuha/workspace/test/src/image/img-%03d.jpg");
    char fileName[255],fileName2[255],fileName3[255];

    sprintf(fileName,temp,i);
    sprintf(fileName2,temp,i+1);    
    sprintf(fileName3,"/home/thuha/workspace/test/src/diff/img-%05d.jpg",i);    
    CImg<unsigned char> image(fileName);
    CImg<unsigned char> image2(fileName2);
    CImg<unsigned char> image3(image-image2);
    image3.save(fileName3);
    std::cout << fileName3 << std::endl;
//    CImg<unsigned char> imageDiffGrey(image.width(),image.height());
  }
  */
