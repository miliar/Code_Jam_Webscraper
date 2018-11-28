#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	ofstream fout("2.out");
    ifstream fin("2.in");
	
int numCase;
int numMove;
int Onow;
int Bnow;
int Owait;
int Bwait;
char nowRobot;
long long int time;
int nowNode;
int stepsToMove;


fin >> numCase;
for(int i=0; i<numCase; i++) {
	fin>> numMove;
	Onow=1;
	Bnow=1;
	Owait=0;
	Bwait=0;
	time=0;
	nowNode=0;
	for(int j=0; j<numMove; j++){
	      fin>> nowRobot;
	      fin>> nowNode;
	      if(nowRobot=='O'){
//          cout<<"O, nowNode="<<nowNode<<", Bnow="<<Bnow<<", Bwait="<<Bwait<<", Onow="<<Onow<<", Owait="<<Owait<<endl;                            
			   stepsToMove=(nowNode-Onow)>0? nowNode-Onow:Onow-nowNode;
			   if(Owait>=stepsToMove){time++; Bwait+=1;}
			   else{time+=(stepsToMove-Owait+1); Bwait+=(stepsToMove-Owait+1);}
			   Owait=0;
			   Onow=nowNode;
//		  cout<<"O,Nowtime= "<<time<<endl;	
		  }
		  else if(nowRobot=='B'){
//          cout<<"B, nowNode="<<nowNode<<", Bnow="<<Bnow<<", Bwait="<<Bwait<<", Onow="<<Onow<<", Owait="<<Owait<<endl; 
		       stepsToMove=(nowNode-Bnow)>0? nowNode-Bnow:Bnow-nowNode;
			   if(Bwait>=stepsToMove){time++; Owait+=1;}
			   else{time+=(stepsToMove-Bwait+1); Owait+=(stepsToMove-Bwait+1);}
			   Bwait=0;
			   Bnow=nowNode;
//		  cout<<"B,Nowtime= "<<time<<endl;
		  }
		  
	}
      fout<<"Case #"<<i+1<<": "<<time<<endl;  
}
	
	
	

	
   system("PAUSE");
    return EXIT_SUCCESS;
}
