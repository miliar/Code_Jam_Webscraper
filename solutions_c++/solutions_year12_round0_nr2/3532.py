#include <iostream>
#include <fstream>
using namespace std;

int main(){

  ifstream fin;
  fin.open("B-large.in");
  ofstream fout;
  fout.open("B-large.out");

  int scores[100] = {0};

  int nCase;
  fin >> nCase;
  for (int iCase = 1; iCase <= nCase; iCase++){
    int nDancer,nSurpri,pScore;

    fin >> nDancer >> nSurpri >> pScore;
    for (int i = 0; i < nDancer; i++)
      fin >> scores[i];

    int sQual = 3*pScore - 2; // t>=sQual, count one for result;
    // t = sQualWithSupri1 or 2, cout one for result with "suprise";
    int sQualWSurpri1 = 3*pScore - 3;
    int sQualWSurpri2 = 3*pScore - 4;

    //no need to sort, just find the number of
    // A = # of t>=3p-2; B = # of t = 3p-3 or 3p-4
    // then A + min(B,p)
    int nQual = 0, nQualWithSurpri = 0;

    if (pScore==1)
    {// 3p-3 = 0, total 0, then no use of suprise triplets -- they disqual!
      for (int i = 0; i < nDancer; i++)
        if (scores[i]>=sQual) nQual++;
    } else
      for (int i = 0; i < nDancer; i++)
      {
        if (scores[i]>=sQual) nQual++;
        else if (scores[i] == sQualWSurpri1 || scores[i] == sQualWSurpri2)
          nQualWithSurpri++;
      }

    int result = nQual + ((nQualWithSurpri>nSurpri)?nSurpri:nQualWithSurpri);

    fout << "Case #" << iCase << ": " << result << endl;
    cout << "Case #" << iCase << ": " << result << endl;
  }

  fin.close();
  fout.close();
  return 0;
}
