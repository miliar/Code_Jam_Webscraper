 
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

void readTestCase(ifstream& f, int& N, int& S, int& p, int** arr)
{
  f >> N;
  f >> S;
  f >> p;
  *arr = new int[N];
  int c=0; 
  while(c<N)
  {
   f >> (*arr)[c];
   c++;
  }
}


int min(int a, int b)
{
  if(a<b)
  { return a;}
  else{return b;}
}

int max(int a, int b)
{
 if(a > b )
 {
	return a;
 }else { return b;}
}

int surprise(int a, int b, int c)
{
  if(abs(a-b)==2) return 1;
  if(abs(a-c)==2) return 1;
  if(abs(b-c)==2) return 1;
  return 0;
}


void processTestCase(int N, int S, int p, int** arr, int& googlerReached)
{
  int* pointarr = arr[0];
  googlerReached=0;
  for(int person=0; person < N; person++){
	 if( pointarr[person] < p ) continue;
	 int possibleReaches = 0;
	 int surpriseCounter = 0;
// 	 cout << "++++++++ " << person << " ++++++++" << endl;
	 for(int x1=p; x1<=10; x1++){
		 int min2 = max(0    , x1-2);
		 int max2 = min(x1+2 ,10);
		  for(int x2=min2; x2<= max2; x2++){
			 int min3 = max(x2-2, max(x1-2, 0 ) );
			 
			 int max3 = min(x2+2, min(x1+2, 10) );
			 for(int x3=min3; x3<=max3; x3++){
			   if(x1+x2+x3==pointarr[person]) {
					 possibleReaches++;
				    surpriseCounter += surprise(x1,x2,x3);
//  					 cout << p << ": "<<  pointarr[person] << " = " << x1 << " + " << x2 << " + " << x3 << "\t" << surprise(x1,x2,x3) << endl;
				}
		   }
		  }
	 }
// 	 cout << surpriseCounter << " : " << possibleReaches << endl;
	 if(possibleReaches > 0){
	 if( surpriseCounter < possibleReaches ){
		googlerReached++;
// 		cout << "googlerReached NO: " << googlerReached << endl;
	 }else{
		if( S > 0) {
			 googlerReached++;
// 			 cout << "googlerReached S: " << googlerReached << endl;
			 S--;
		}
	 }
	 }
  }
}



int main(int argc, char** argv)
{

 int* inputData;
 int T;
 
 ifstream file;
 file.open(argv[1]);
 if(!file) return 0;
 
 file >> T;
 
 for(int t=1; t<=T; t++){
  int N, S, p, result;
  int* arr;
  readTestCase(file, N, S, p, &arr);
//    cout << "\n\nTESTSET " << t << endl;
  processTestCase(N, S, p, &arr, result);
  cout << "Case #" << t << ": " << result << endl;
  delete[] arr;
 }
 
//  readInput(argv[1], &inputData, n);
 
 return 0;
}
