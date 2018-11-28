#include <iostream>

using namespace std;

int z, n, a[100];;

int test(int k)
{ 
  int i, j;
  if (k==1) return 1;
  else {
  	j=n+2;
  	for (i=0; i<k; i++) 
    	if (a[i]==k) j=i;
	  if (j>n) return 0;
 		else return test(j);
  }
}

void gen(int k)
{
	int i;
	if (a[k-1]==n) {
		if (test(k-1)>0) z++;
		if (z==100003) z=0;
	}
	else {	
		for (i=a[k-1]; i<n; i++) {
			a[k]=i+1;
			gen(k+1);
			a[k]=0;
  	}
	 }
}


int main()
{
	int t, i, j, m, k;
	
	cin >> t;
	for (k=0; k<t; k++) {
		z=0;
		cin >> n;
		z=0;
		a[0]=1;
		gen(1);
  
	  cout << "Case #" << k+1 << ": " << z << endl;
	}
	return 0;
}
