#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <fstream>

using namespace std;

static long groups[2000001];
static long group_c[2000001];
static bool group_counted[2000001];


int num_digits(long l){
  long ll = l;
  int size = 0;
  
  while (ll > 0){
	ll /= 10;
	size += 1;
  }
  return size;
}

long sumN_(long l)
{
  long ll;
  long sum = 0;
  
  for (ll = 1; ll <= l-1 ; ll++){
	sum += ll;
  }
  return sum;
  
  //return (l*(l-1))/2;
}

long groupCount(long Val, long A, long B)
{
  long ll;
  long count = 0;
  
  for (ll = A; ll <= B; ll++){
	if (groups[ll] == Val){
	 count += 1;
	}
  }
  return count;
}

long numRotationsAB(long A, long B)
{
  long ll;
  long res = 0;
  long group_count;

  for (ll = A; ll <= B; ll++){
	if (groups[ll] > 0 && !group_counted[groups[ll]]){
	  group_count = groupCount(groups[ll],A,B);
	  res += sumN_(group_count);
	  group_count = 0;
      group_counted[groups[ll]] = true;
	}
  }
  
  //must set this to initial state..

  for (ll = A; ll <= B; ll++){
    group_counted[groups[ll]] = false;
  }
  
   /*for (ll = 1; ll <= 2000000; ll++){
	 group_counted[ll] = false;
   }*/
  
  return res;
}

long Rotate2(long l, int nr)
{
  int a[20];
  int i = 0, j, rotations = nr;
  long ll = l;
  while(ll > 0) {
   a[i] = ll % 10;
   ll /= 10;
   i++;
  }
  while (rotations){
	a[i] = a[0]; //posledny+1
	for (j = 0; j < i; j++){
	  a[j] = a[j+1];
	}
	rotations--;
  }
  long val=0;
  for (j = i-1; j >= 0; j--){
	val = (val*10) + a[j];
  }
  if (num_digits(val) != num_digits(l)){
	return -1;
  }
  else
  {
    return val;
  }
}


int main(int argc, char *argv[])
{
   const char SPACE[2] = " ";
   int N; //number of cases 
   char c;
   char c1;
   char output[120];
   int ii, jj, i1, j1; //iterators
   long li;
   
   long nA, nB, result;
   
   for (li = 1; li <= 2000000; li++){
	 groups[li] = 0;
	 group_c[li] = 0;
	 group_counted[li] = false;
   }
   /*coloring valid rotations*/
   
   for (li = 1; li <= 2000000; li++){
	 int ndig = num_digits(li);
	 long ln = li;
	 int ij;
	 for (ij = 1; ij <= ndig-1; ij ++){
	   ln = Rotate2(li,ij);
       if ((ln > 0) && (ln <= 2000000) && (groups[ln] == 0) && (ln != li)){
	     groups[ln] = li;
		 if (groups[li] == 0) {
		  groups[li] = li;
		 }
       }
	   //cout << ln;
	   //cin.get();
	 }
   }

   ifstream i_file1 ("inputs/C-large.in");
   ofstream o_file ("outputs/rotations.out");
   
   i_file1 >> N; //reading number of cases
   for(ii = 1; ii <= N; ii++) {
	 /*case input code*/
	 i_file1 >> nA >> nB;
	 //result = numRotationsAB(nA, nB); this was slow
	 
      long ll;
	  long res = 0;
	  long group_count;

	  for (ll = nA; ll <= nB; ll++){
		if (groups[ll] > 0){
			res+= group_c[groups[ll]];
			group_c[groups[ll]] += 1;
		}
	  }
	  
	  for (ll = nA; ll <= nB; ll++){
		group_c[groups[ll]] = 0;
	  }
	  
	  result = res;
	 
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


