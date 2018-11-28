#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;


const int maxpoint1=100+1;  // maximum point number on side 1
const int maxpoint2=100+1;  // maximum point number on side 2

bool g[maxpoint1][maxpoint2];// whether two point can match, point start from 1 !!
int match1[maxpoint1];      // match from side 1 to side 2
int match2[maxpoint2];      // match from side 2 to side 1
int tp1,tp2;                // total point on both sides
int ansmatch;               // the answer

bool findmatch(int pntstart) // If found return true, otherwise false.
{
  int newm2[maxpoint2];       // new match from side 2
  int list[maxpoint1];        // for BFS using
  int lr, lw;                 // read/write pointer in list[]
  int i, j, k;
  memset(newm2,0,sizeof(newm2));
  list[1]=pntstart;
  lr=0;
  lw=1;
  while (lr<lw)
  {
    lr++;
    i=list[lr];
    for (j=1;j<=tp2;j++)
      if (g[i][j] && newm2[j]==0)
        if (match2[j]==0)
        {
          // point (j) on side 2 hasn't matched
          while (true)
          {
            match2[j]=i;
            k=match1[i];
            match1[i]=j;
            if (k==0) break;
            j=k;
            i=newm2[j];
          }
          return true;  // findmatch succeeded
        }
        else
        {
          newm2[j]=i;    // save path
          lw++;
          list[lw]=match2[j];
        }
  }
  return false;
}



#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int n,k;
		fin >> n >> k;
		int pr[101][30];
		FI(i,0,n) FI(j,0,k) fin >> pr[i][j];

		tp1 = n;
		tp2 = n;
		mset(g, 0);
		ansmatch = 0;
		mset(match1, 0);
		mset(match2, 0);

		//cout << endl;
		FI(i,0,n) FI(j,0,n) {
			int z = 0;
			while (z < k && pr[i][z] < pr[j][z]) z++;
			if (z >= k) {
				g[i+1][j+1] = true;
			}
			//cout << "m " << i << ' ' << j << endl;
		}

		for (int pnt1=1;pnt1<=tp1;pnt1++)
		    if (match1[pnt1]==0)
		      if (findmatch(pnt1))
				ansmatch++;

		int ans = n-ansmatch;
		fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
