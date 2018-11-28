#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <map>
#include <string>

using namespace std;

int main (int argc, char * const argv[]) {
	
	ifstream myfile;
	
	myfile.open (argv[1]);
	 if(!myfile) { // file couldn't be opened
	 cerr << "Error: file could not be opened" << endl;
	 exit(1);
	 }
	 int T;	
	 
	 myfile >> T;
	 int* N = new int[T];
	 int* S = new int[T];
	 int* p = new int[T];
	 int* output = new int[T];
	 for (int i = 0; i<T;i++){
	 myfile>>N[i];
	 myfile>>S[i];
	 myfile>>p[i];
	 int cases = 0;
	 int* googler_total = new int[N[i]];
	 
	 	for (int j = 0; j < N[i]; j++){
	 	
			 myfile>>googler_total[j];
			 int base = googler_total[j]/3;
			 switch (googler_total[j]%3){
			 case 0:
			 	if (base>=p[i]){
			 		cases++;
			 	}
			 	else {
			 		if (S[i]>0 && base>0 && base+1>=p[i])
			 		{
			 			cases++;
			 			S[i]--;
			 		}
			 	}
			 	break;
			 case 1:
			 	if (base>= p[i] || base+1>=p[i]) {
			 		cases++;
			 	}
			 	else {
			 		if(S[i]>0 && base+1>=p[i])
			 		{
			 			cases++;
			 			S[i]--;
			 		}
			 	}
			 	break;
			 case 2:
			 
			 if(base+1>=p[i] || base>=p[i])
			 	cases++;
			 else
			 {
			 	if (S[i] >0 & base+2>=p[i])
			 	{
			 		cases++;
			 		S[i]--;
			 	}
			 }
			 break;
		 }
		 }
		 cout<<"Case #"<<i+1<<": "<<cases<<endl;
	 	
	}

}
 
