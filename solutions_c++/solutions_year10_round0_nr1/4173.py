#include <iostream>
#include <string>
#include <assert.h>
#include <stdlib.h>
#include <math.h>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]){


  if(argc < 3){
    cout <<"Please enter the input and output file name :\n<executable><input-file><output-filename>\n";
    exit(-1);
  }
  
  int num_inputs;
  //int *stages, *clicks;
  ifstream ip;
  ofstream op;
  ip.open(argv[1]);
  op.open(argv[2]);
  assert(!ip.fail());
  while(!ip.eof()){
    
    string temp;
    ip >> temp;
    num_inputs = atoi(temp.c_str());
    if (num_inputs > 10000){
      cout <<"Illegal Number of inputs\n";
      exit(-1);
    }
    // stages = new int[num_inputs];
    //clicks = new int[num_inputs];
    for (int k = 0; k< num_inputs;k++){
      ip >> temp;
      int n_value = atoi(temp.c_str());
      //      cout <<n_value<<" ";
      assert( !(n_value < 0) );
      ip >> temp;
      int k_value = atoi(temp.c_str());
      //cout << k_value<<"\n";
      assert(!( k_value < 0));
      //stages[k] = n_value;
      // clicks[k] = k_value;
      op << "Case #" <<k+1 <<": ";
      if(((k_value+1)%(int)(pow(2,n_value))) == 0){
       op <<"ON" << endl;
      }
      else
	op <<"OFF" <<endl;
    }
    
    
    
    
  }

    
  
}
