#include <stdio.h>
#include<iostream>
#include <fstream.h>
using namespace std;
int main(int argc, char* argv[])
{     
    int task;
    int run;
    int keep;
    int number;
  int *dane;
ifstream file;
ofstream out("out.txt"); 
file.open("test.txt");
	file>>task;
	for(int i=0;i<task;i++)
	{
 int money=0;
         int wsk=0;
         dane = new int[1000000];
         file>>run;
         file>>keep;
         file>>number;
	     for(int a=0;a<number;a++)       	
	        {     
                  file>>dane[a];
            }
         for(int x=0;x<run;x++)       	
	        {     
                  int count=0;
                  int z=0;
                  bool end=true;
                  do{          
                       if ((count+dane[wsk])<=keep)
                       {
                       count=count+dane[wsk];
                        wsk++;
                        z++;
                        if (wsk==number)
                        wsk=0;
                        }else
                        { 
                             end=false;
                        money=money+count;}
                        if (z==number)
                       { 
                             end=false;
                        money=money+count;}
                             }while(end);
            }
                          delete dane;      
                       out<<"\nCase #"<<1+i<<": "<<money;  
	}		
	return 0;
}
