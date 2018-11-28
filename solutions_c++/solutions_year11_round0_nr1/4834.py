#include <iostream>
#include <cstdio>
#include <fstream>
#include <string.h>
#include <cstdlib>
using namespace std;

#define MAX(a,b) ((a > b) ? a : b)
#define MOD(a) (((a) > 0) ? (a) : -(a))

typedef struct {
  char color;
  int gtp;
  int blic;
  int olic;
  int bpp ;
  int opp;
  int time_add;
} ins;

int main (int argc, char* argv[]) {
  ifstream input ("A-large.in");
  ofstream output ("robot_test_output_large.txt");
  string line;
  getline(input, line);
  int no_of_test_cases = atoi(line.c_str()); 
  int index;

  cout << "No of testcases " << no_of_test_cases << endl;
  /* For each test case */
  for (index = 1; index<=no_of_test_cases; index++) {
    getline(input, line);
    int no_of_buttons = 0, ip  = 0, total_no_of_seconds = 0;
    /* Tokenize each test case into Ri,Pi pairs */
    char delims[] = " ";
    char *testcase = strtok((char *)line.c_str(), delims);
    no_of_buttons = atoi(testcase);
    
    ins instructions[100];    

    // For each button press
    while (testcase != NULL) {
      
      testcase = strtok(NULL, delims);
      if (testcase != NULL) {
	instructions[ip].color = testcase[0];
      }
      
      if (testcase != NULL) {
	testcase = strtok(NULL, delims);
	if (testcase != NULL) {
	  instructions[ip].gtp = atoi(testcase);
	}
	ip++;
      }
    }
  

    instructions[0].bpp = instructions[0].opp = 1;
    instructions[0].blic=instructions[0].olic = -1;

    for (ip=0; ip<no_of_buttons; ip++) {      
      int sum_prev = 0;
      if (instructions[ip].color == 'B') 
	{
	  if (ip < no_of_buttons-1) {
	      instructions[ip+1].blic = ip;
	      instructions[ip+1].bpp = instructions[ip].gtp;
	      instructions[ip+1].opp = instructions[ip].opp;
	      instructions[ip+1].olic = instructions[ip].olic;
	  }
	  
	  //	  cout << "ip: "<< ip << "|instructions[ip].blic : " << instructions[ip].blic << endl;
	  for (int i=instructions[ip].blic+1; i< ip; i++) {
	    //	    cout << "i: = " << i << ", bsp+=" << instructions[i].time_add << endl;
	    sum_prev += instructions[i].time_add;
	  }
	  
	  //	  cout << "B: gtp - bpp = " << instructions[ip].gtp << "- " <<instructions[ip].bpp<< endl;
	  //	  cout << "MOD : "<< MOD(instructions[ip].gtp - instructions[ip].bpp) <<endl;
	  instructions[ip].time_add = MAX(MOD(instructions[ip].gtp - instructions[ip].bpp) - sum_prev, 0) + 1 ;
	  
	}
      else 
	{ //Orange
	  if (ip < no_of_buttons-1) {
	      instructions[ip+1].olic = ip;
	      instructions[ip+1].opp = instructions[ip].gtp;
	      instructions[ip+1].bpp = instructions[ip].bpp;
	      instructions[ip+1].blic = instructions[ip].blic;
	  }
	  
	  //	  cout <<"ip: " << ip << "|instructions[ip].olic : " << instructions[ip].olic << endl;
	  for (int i=instructions[ip].olic+1; i< ip; i++) {
	    //	    cout << "i: = "<< i << ", osp+=" << instructions[i].time_add << endl;
	    sum_prev += instructions[i].time_add;
	  }
	  
	  instructions[ip].time_add = MAX(MOD(instructions[ip].gtp - instructions[ip].opp) - sum_prev, 0) + 1 ;
	  
	  //cout << "oip = " << ip << ", time_add =" << instructions[ip].time_add << endl;
	  
	}
      
      //            cout << ip << ":" << endl << instructions[ip].color << "|" << instructions[ip].gtp << "|" << instructions[ip].blic << "|" << instructions[ip].olic << "|" << instructions[ip].bpp << "|" << instructions[ip].opp << "|(" << sum_prev << ")"<< instructions[ip].time_add << endl << endl;
      total_no_of_seconds += instructions[ip].time_add;
      }
    //cout << "Test case : " << index << " | total_no_of_seconds : " << total_no_of_seconds << endl;
    
    output << "Case #" << index <<": " << total_no_of_seconds << endl;
  }
  return 0;
}
