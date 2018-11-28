#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cmath>
//#include <map>

using namespace std;




int shiftOneDigit(int a, int Ndigit)
{
	int lastDigit=a%10;
	return lastDigit*(int)(pow(10.0,double(Ndigit-1)))+(a-lastDigit)/10;
}



int  countPairEfficient(int start, int end)
{
   //int start=1000000;
   //int end=2000000;
   int Ndigit= log10((double) start)+1;
   int Ntotal=end-start+1;
   int Npair=0;
   int *flag=new int[Ntotal];
  
   //cout<<"Ndigit= "<<Ndigit<<endl;
   int *count=new int[Ndigit];
   vector<int> shift;

   for(int i=0; i<Ndigit; i++)
   {
	   count[i]=0;
	   //cout<<count[i]<<endl;
   }
   for(int i=0; i<Ntotal; i++)
   {
	   flag[i]=0;
   }

   for(int curr=start; curr<=end; curr++)
   {
	   if(flag[curr-start]==0){
	      shift.push_back(curr);
		  flag[curr-start]=1;
	      int n=0;
	      int temp=curr;
          for(int id=1; id<Ndigit; id++)
	      {    
			temp=shiftOneDigit(temp, Ndigit);
	        if(temp<=end && temp>=start)
			{
				int j=0;
				// make sure it won't duplicate after shift
				while(j<shift.size() && temp!=shift[j])
				{
	                j++;
			//		cout<<j<<endl;
				}
			//	cout<<"outj="<<j<<endl;
				if(j==shift.size()) 
				{
					n++;
					shift.push_back(temp);
					flag[temp-start]=1;
				}
			}	
	      }
	      shift.clear();

	      //cout<<"curr="<<curr<<", n="<<n<<endl;

	      count[n]+=n+1;
	      //cout<<"count[n]="<<count[n]<<endl;
	   }
   }

   Npair=Ntotal-count[0];
   for (int i=1; i<Ndigit; i++)
   {
       Npair+=count[i]*(i-1);
   }
   Npair=Npair/2;

   //cout<<"Npair="<<Npair<<endl;

   return Npair;
}





int main()
{

  int num_case;
  string line;
  string inFileName, outFileName;
  //cout<<"input data file name:"<<endl;
  //cin>>inFileName;
  //cout<<"input output file name:"<<endl;
  //cin>>outFileName;
  
  inFileName="C-large.in";
  outFileName="C-large.out";

  ifstream in_file(inFileName.c_str());
  ofstream out_file(outFileName.c_str());

  in_file>>num_case;
  getline(in_file, line);//ignore 1st line
  //cout<<num_case<<" test cases "<<endl;
    
  int caseNum=1;
  int start=0;
  int end=0;
  int Npair=0;

  
  
  while (getline(in_file, line))
  {
	  istringstream sline(line);
      sline>>start;
      sline>>end;

      int count=0;
      int temp=0;

	  Npair=countPairEfficient(start,end);


      out_file<<"Case #"<<caseNum<<": "<< Npair <<endl;        
      line.clear(); 
	
      caseNum++;       
  }    
    return 1;    
}

