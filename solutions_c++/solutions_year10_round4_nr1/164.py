#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
#define MAXP 200
vector<vector<int> > v;
vector<vector<int> > tmp;
int main() {
    int z;
    scanf("%d", &z);
    for(int te = 1; te <= z; te++) {
	v.clear();
	tmp.clear();
	v.resize(MAXP);
	tmp.resize(MAXP);
	for(int i=0; i<MAXP; i++) {
	    v[i].resize(MAXP,-1);
	    tmp[i].resize(MAXP, -1);
	}
	int size;
	scanf("%d", &size);
//	printf("Size to %d\n", size);
	/*
	    *  Line i (1 ≤ i ≤ k) contains k-i spaces, then i digits separated by single spaces.
    * Line i (k < i < 2k) contains i-k spaces, then 2k-i digits separated by single spaces.
	*/
	for(int j=1; j<=size; j++)
	    for(int l=1; l<=j; l++)
		scanf("%d", &v[j-l+1][l]);
	 for(int j=size+1; j<2*size; j++)
	    for(int l=1; l<=(2*size)-j; l++) {
		int a = size-l+1;
		int b = j-size+l;
		scanf("%d", &v[a][b]);
	    }
	/* cout << "DUPA\n";
	 for(int i=1;i<=size;i++) {
	     for(int j=1; j<=size; j++)
		 cout << v[i][j] << ' ';
	     cout << endl;
	 }
	 cout << "DUPA2\n";*/
	 int sol = -1;
	 for(int i=size; i<MAXP && sol == -1; i++) {
	     for(int j=1; j<=(i-size+1); j++)
		 for(int k=1; k<=(i-size+1) && sol == -1; k++) {
		     
		     for(int l=1; l<=size; l++)
			 for(int m=1; m<=size; m++)
			     tmp[j+l-1][k+m-1] = v[l][m];
		    

		     /*cout << "Sprawdzam:" << endl;
		     for(int l=1; l<=i; l++) {
			for(int m=1; m<=i; m++)
			    cout << tmp[l][m] << ' ';
			 cout << endl;
		     }*/
	             bool ok = true;
	             for(int l=1; l<=size && ok; l++)
			 for(int m=1; m<=size && ok; m++) {
			     int a = j+l-1;
			     int b = k+m-1;
			     if (! ( (tmp[a][b] == tmp[i-b+1][i-a+1] || (tmp[i-b+1][i-a+1] == -1)) && (tmp[a][b] == tmp[b][a] || tmp[b][a] == -1)) ) {
				//cout << "Blad na " << a << ' ' << b << endl;
				ok = false;
			     }
			 }
		     if(ok)
			sol = i;
			 
		     for(int l=1; l<=size; l++)
			 for(int m=1; m<=size; m++)
			     tmp[j+l-1][k+m-1] = -1;
		 }
	 }
//	 cout << sol << endl;
	 if(sol == -1)
	     printf("Case #%d: %d\n", te, MAXP*MAXP - size*size); // maybe :P
	 else
	     printf("Case #%d: %d\n", te, sol*sol - size*size);
    }
    return 0;
}