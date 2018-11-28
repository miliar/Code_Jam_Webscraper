#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <stdio.h>

#include <math.h>

using namespace std;


    ofstream fout("ou.txt");
    ifstream fin ("beads.txt");

    //FILE* pFile;
    //int c;
    //pFile = fopen("ou.txt","w");
    //pFile=fopen ("beads.txt","r");



int main() {

//FILE* pFile;
//pFile = fopen("ou.txt","w");

int NN;

fin >> NN;

for (int tt=0; tt<NN; tt++)
{
 
// string na;
// if (tt == 0)
//  getline(fin,na);

// getline(fin,na);

// istringstream sin(na); 
// string v; 
// while (sin>>v) 
//   names.push_back(v); 


//sscanf(stringHM,"%d:%d",&h,&m);


 //fprintf(pFile, "Case #%d: ", t+1);
 //fprintf(pFile,"%d\n",res);

long long n, m, a;

fin >> n >> m >> a;

double tol = 0.000001;

bool fou = false;
int ri, rj, rk, rp;

for (int i=0; i<=n && !fou; i++)
{
  for (int j=0; j<=m && !fou; j++)
  {
    for (int k=0; k<=n && !fou; k++)
	{
       for (int p=0; p<=m && !fou; p++)
	   {
          double d01 = i*i+j*j;
		  d01=sqrt(d01);
		  double d02 =  k*k+p*p;
		  d02=sqrt(d02);
          double d12 = (k-i)*(k-i)+(p-j)*(p-j);
		  d12=sqrt(d12);
		  double s = (d01+d02+d12)/2;
		  double ps = s*(s-d01)*(s-d02)*(s-d12);
		  double aa = a;
		  aa = aa/2;
		  aa = aa*aa;

		  if ( abs(ps-aa) < tol)
		  {
			  fou = true;
			  ri=i;
			  rj=j;
			  rk=k;
			  rp=p;
			  //fout << "Case #" << tt+1 << ": " << i << " " << j << " " << k << " " << p << endl;
			  //fout << d01 << " " << d02 << " " << d12 << endl;
		  }
	   }
	}
  }
}

//long long res = 0;

  if (!fou)
    fout << "Case #" << tt+1 << ": " << "IMPOSSIBLE" << endl;
  else
	fout << "Case #" << tt+1 << ": " << 0 << " " << 0 << " " << ri << " " << rj << " " << rk << " " << rp << endl;
}

   return 0;
}
