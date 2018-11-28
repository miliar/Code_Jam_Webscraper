#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>

using namespace std;
using std::cout;

using std::cin;
using std::endl;
int main() {

  const char* filename = "B-small-attempt11.in";
  std::ifstream inFile(filename);
  std::ofstream outFile("Solution.txt");
  // Make sure the file stream is good
  
  
  int n,s,p,i,j=0,k,l=1;
  long t;
  
  int arr[100];
  inFile>>t;
  //inFile.ignore(100, '\n');
  while(!inFile.eof())
  {
   inFile>>n>>s>>p;
   //outFile<<" n:"<<n<<" s:"<<s<<" p:"<<p<<"\n";
   for(i=0;i<n;i++){inFile>>arr[i];}
   for(i=0;i<n;i++)
   {     if(arr[i]==0 & p==0){j++; continue;}
         if(arr[i]==0) continue;
         k=arr[i]/3;
         //outFile<<arr[i]<<" ";
         if(k>=p ) j++;
         else if(k<p)
          { 
            t=arr[i]-(3*k);
            switch(t)
            {
            case 2:
            {
            if(k+t>=p & s>0){j++;s--;}
            else if((k+1)>=p) j++;
            break;
            }
            case 1:
            {
            if( (k+t)>p |(k+t)==p ){ j++;}
            break;
            }
            case 0:
            {     
            if((k+1)>=p & s>0){j++;s--;}
            break; 
            }
          }}
                      
   }
  outFile<<"Case #"<<l<<": "<<j;++l;
  outFile<<"\n";j=0;
  memset(arr, 0, 100);
  }

   system("PAUSE");
  
  
  return 0;
  
}
