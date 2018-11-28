#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

typedef struct snapperConf{
  unsigned int n;
  unsigned long long int k;
  bool result;
} snapperConf;

bool isOn(unsigned int n, unsigned long long int k)
{
  if ( ( (k+1)% ((unsigned long long int)pow(2,(long double)n)) )  == 0) 
     return true;    
  else
     return false;
}

int main (void)
{
 fstream inputFile;
 inputFile.open ("snapperin",ios::in);
 fstream outputFile;
 outputFile.open ("snapperout",ios::out);
 
 unsigned long int numTests = 0;
 //vector <snapperConf> numCases (numTests);
 
 if(!inputFile) {
    cout << endl << "Failed to open file " << endl;
    return 1;
  }
 inputFile >> numTests;       
 
 int iter = 1;
 while (!inputFile.eof())
 {
       snapperConf instance;
       inputFile >> instance.n;
       inputFile >> instance.k;
       instance.result = isOn(instance.n,instance.k);
       //numCases.push_back(instance);
       //cout << iter <<" "<<instance.n<<" "<<instance.k<<" "<<instance.result<< endl;
  
       if (!inputFile.eof())
       {
       if (instance.result)
          outputFile << "Case #" << iter <<": ON"<<endl;
       else
          outputFile << "Case #" << iter <<": OFF"<<endl; 
       }
           
       ++iter;
 }
 
 //if (iter != numTests) 
   //{
    //  outputFile << "Error in inputFile. numTests specified:" << numTests << " Num Cases found:" << iter-1 << endl;       
 //  }
   
   
 inputFile.close();
 outputFile.close();
 
 return 0;   
}
