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

using namespace std;


    ofstream fout("ou.txt");
    //ofstream fout ("fence4.out");
    //ifstream fin ("fence4.in");
    ifstream fin ("beads.txt");

	//FILE* pFile;
    //int c;
    //pFile = fopen("ou.txt","w");
    //pFile=fopen ("beads.txt","r");

vector <string> depfra;
vector <string> arrfra;
vector <string> depfrb;
vector <string> arrfrb;

vector <vector<int> > Q;

int comp(string s)
{
  int x = 0;
  x += s[4] - '0';
  x += 10*(s[3]-'0');
  x += 60*(s[1]-'0');
  x += 600*(s[0]-'0');
  return x;
}

int main() {

FILE* pFile;
pFile = fopen("ou.txt","w");

int N;

fin >> N;

for (int t=0; t<N; t++)
{
  depfra.clear();
  arrfra.clear();
  depfrb.clear();
  arrfrb.clear();
  Q.clear();
 
  int turn, na, nb;

  fin >> turn >> na >> nb;

  for (int i=0; i<na; i++)
  {
    string t1, t2;
	fin >> t1 >> t2;
	depfra.push_back(t1);
    arrfra.push_back(t2);
  }

  for (int i=0; i<nb; i++)
  {
    string t1, t2;
	fin >> t1 >> t2;
	depfrb.push_back(t1);
    arrfrb.push_back(t2);
  }
 
  //priority_queue<vector<int>,vector<vector<int> >, greater<vector<int> > > Q; 

  vector <int> L(2);
  int x = 0;
  //int h = 0;
  //int m = 0;
  for (int i=0; i<na; i++)
  {
	//sscanf(depfra[i],"%d:%d",&h,&m);
    x=comp(depfra[i]);
    L[0]=x;
	L[1]=2;
	Q.push_back(L);

	//sscanf(arrfra[i],"%d:%d",&h,&m);
    x=comp(arrfra[i])+turn;
    L[0]=x;
	L[1]=0;
	Q.push_back(L);

	//x=x+turn;
    //L[0]=x;
	//L[1]=5;
	//Q.push(L);
  }

  for (int i=0; i<nb; i++)
  {
	//sscanf(depfrb[i],"%d:%d",&h,&m);
    x=comp(depfrb[i]);
    L[0]=x;
	L[1]=3;
	Q.push_back(L);

	//sscanf(arrfrb[i],"%d:%d",&h,&m);
    x=comp(arrfrb[i])+turn;
    L[0]=x;
	L[1]=1;
	Q.push_back(L);

	//x=x+turn;
    //L[0]=x;
	//L[1]=4;
	//Q.push(L);
  }

  sort(Q.begin(), Q.end());

  int cura = 0;
  int curb = 0;
  int ma   = 0;
  int mb   = 0;

  for (int i=0; i<Q.size(); i++)
  {
    L = Q[i];
	if (L[1] == 2)
	{
      cura--;
	  ma=min(ma,cura);
	}
	else if (L[1] == 3)
	{
      curb--;
	  mb=min(mb,curb);
	}
	else if (L[1] == 0)
	{
      curb++;
	}
	else
	{
      cura++;
	}
  }

   ma = -1*ma;
   mb = -1*mb;

 //fprintf(pFile, "Case #%d: ", t+1);
 //fprintf(pFile,"%d\n",res);

  fout << "Case #" << t+1 << ": " << ma << " " << mb << endl;
}

   return 0;
}
