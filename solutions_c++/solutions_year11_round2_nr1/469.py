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

ofstream fout("OUT111.txt");
ifstream fin ("INP111.in");


//FILE* pFile;
//int c;
//pFile = fopen("ou.txt","w");
//pFile=fopen ("beads.txt","r");


int main() {

//FILE* pFile;
//pFile = fopen("ou.txt","w");

// string na;
// if (tt == 0)
//  getline(fin,na);

// getline(fin,na);

// istringstream sin(na); 
// string v; 
// while (sin>>v) 
//   names.push_back(v); 

//fprintf(pFile, "Case #%d: ", t+1);
//fprintf(pFile,"%d\n",res);

  int sco[110][110];
  double pla[110];
  double won[110];
  double res[110];
  double owp[110];

  fout.precision(30);

  int TT;
  fin >> TT;
  for (int tt=0; tt<TT; tt++)
  { 
     memset(sco, 0, sizeof(sco));
	 memset(pla, 0, sizeof(pla));
	 memset(won,  0, sizeof(won));
	 memset(res, 0, sizeof(res));
     memset(owp, 0, sizeof(owp));

	 int N;
	 fin >> N;
	 for (int i=0; i<N; i++)
	 {
        string s;
		fin >> s;
		for (int j=i+1; j<N; j++)
		{
           if (s[j] == '1')
		   {
              pla[i]++;
			  pla[j]++;
			  sco[i][j]=1;
			  sco[j][i]=-1;
			  won[i]++;
		   }
		   else if (s[j] == '0')
		   {
              pla[i]++;
			  pla[j]++;
			  sco[i][j]=-1;
			  sco[j][i]=1;
			  won[j]++;
		   }
		}
	 }

     for (int i=0; i<N; i++)
	 {
        res[i]=0.25*won[i]/pla[i];
		double lowp = 0;
		for (int j=0; j<N; j++)
		{
           if (i != j && ( (sco[i][j]==1) || (sco[i][j] == -1) ) )
		   {
             double xowp = 0;
			 if (sco[i][j] == 1)
				 xowp = (won[j]/(pla[j]-1));
			 else
                 xowp = ((won[j]-1)/(pla[j]-1));

             lowp = lowp + xowp;   			 
		   }
		}
		lowp = lowp/pla[i];
		owp[i] = lowp;
		res[i] = res[i] + 0.5*owp[i];
	 }

     for (int i=0; i<N; i++)
	 {
        double oowp = 0;
		for (int j=0; j<N; j++)
		{
           if (i != j && ( (sco[i][j]==1) || (sco[i][j] == -1) ) )
		   {
              oowp = oowp + owp[j];
		   }
		}
		oowp = oowp/pla[i];
		res[i] = res[i] + 0.25*oowp;
	 }

     fout << "Case #" << tt+1 << ": " << endl;
	 for (int i=0; i<N; i++)
	     fout << res[i] << endl;
  }

   return 0;
}
