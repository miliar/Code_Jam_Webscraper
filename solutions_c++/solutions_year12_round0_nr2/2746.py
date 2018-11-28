#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <fstream>
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{
   const char SPACE[2] = " ";
   int T; //number of cases
   int N; //number of googlers
   int S; //number of surprising triplets
   int p; //treshold
   int ii, i,  j; //iterators
   int scores[150];
   int scores1[150];
   int values[150];
   int c; //whole part of number - floor
   double k;
   bool resolved[150];
   long result;
   double eps = 0.000001;
   
   ifstream i_file1 ("inputs/B-small-attempt0.in");
   ofstream o_file ("outputs/dance.out");
   
   i_file1 >> T; //reading number of cases
   for(ii = 1; ii <= T; ii++) {
	 /*case input code*/
	 i_file1 >> N >> S >> p;

	 for (j = 1; j <= N; j++){
	   i_file1 >> scores[j];
	   resolved[j] = false;
	 }
	 result = 0;
	 
	 for (j = 1; j <= N; j++){
	   k = scores[j] / 3.0;
	   c = floor(k);
      if (abs(k - c) < eps) //k=c
	   {
		  if (c >= p) {
			result += 1;
			resolved[j] = true;
	      }
	   }else {
		 if (c+1 >= p){
		   result += 1;
		   resolved[j] = true;
		 }
	   }
	}
	
	int nn= 0;
	for (j = 1; j <= N; j++){
	 if (!resolved[j]){
       nn++;
       k = scores[j] / 3.0;
	   c = floor(k);
	   scores1[nn] = scores[j];
	   if (abs(k - c) < eps){
		 if (c+1 <= 10 && c-1 >= 0) {
		  values[nn] = c+1;
		 }else{
          values[nn] = c;
		 }
	   }else{
          if (c+2 <= 10) {
		   values[nn] = c+2;
		  }else{
           values[nn] = c+1;
		  }
	   }
	 }
	}
	
	/*sort values descending*/
	int max, pom;
	for (i = 1; i <= nn-1; i++){
	   max = i;
	   for (j = i+1; j <= nn; j++){
		 if(values[j] > values[max]){
		   max = j;
		 }
	   }
	   pom = values[i];
	   values[i] = values[max];
	   values[max] = pom;
	  /* pom = scores1[i];
	   scores1[i] = scores1[max];
	   scores1[max] = pom;*/
	}
	/************************************/

	for (i = 1; i <= min(nn,S); i++){
	  if (values[i] < p){
		break;
	  }
	  result += 1;
	}
	
	 /*case output code*/
	 //file output
	 o_file << "Case #" << ii << ": " << result << "\n";
	 //console output
	 cout << "Case #" << ii << ": " << result << "\n";
   }
   i_file1.close();
   o_file.close();

   cin.get();

   return 0;
}

