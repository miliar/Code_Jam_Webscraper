#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;




int main()
{
  int num_case;
  string line;
  string inFileName, outFileName;
  cout<<"input data file name:"<<endl;
  cin>>inFileName;
  cout<<"input output file name:"<<endl;
  cin>>outFileName;
  

  ifstream in_file(inFileName.c_str());
  ofstream out_file(outFileName.c_str());

  in_file>>num_case;
  getline(in_file, line);//ignore 1st line
  //cout<<num_case<<" test cases "<<endl;
    
  int caseNum=1;
  int Ngoogler=0;
  int Nsurprise=0;
  int pBest=0;
  int sum=0;
  //vector<int> googlerScore;
  
  while (getline(in_file, line))
  {
	  istringstream sline(line);
      sline>>Ngoogler;
      sline>>Nsurprise;
	  sline>>pBest;

      int count=0;
      int temp=0;

	  for (int i=0; i<Ngoogler; i++){
		  sline>> sum;
	//	  googlerScore.push_back(sum);
		 
	     if(sum>=3*pBest-2)
		 {
			count++;
		 }
		 else if(sum<3*pBest-2 && sum>=3*pBest-4 && pBest>=2)
		 {
			 temp++;
		 }
	  }

	 //  cout<<count<<" ,"<<temp<<endl;

      count+=min(temp,Nsurprise);

      out_file<<"Case #"<<caseNum<<": "<< count <<endl;        
      line.clear(); 
	//  googlerScore.clear();
      caseNum++;       
  }    
    return 1;    
}
