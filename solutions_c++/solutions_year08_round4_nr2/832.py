#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <pari/pari.h>




using namespace std;

char b[100];

GEN gp_string(string s)
{
  GEN r;
  char* cstr;
  cstr = new char [s.size()+1];
  strcpy (cstr, s.c_str());
  r = gp_read_str( cstr );
  delete[] cstr;
  return r;
}


vector<int> kan(int N,int M,int A)
{
  int i,x1,x2,y1,y2,Q;
  string Qs;
  GEN r;
  long num_div,d,e;
  vector<int> coor(4);
  for(x2=0; x2<=N; ++x2) {
    for(y1=0; y1<=M; ++y1) {
      Q = A+x2*y1;
      sprintf(b,"n = divisors(%d);",Q);
      gp_read_str( b );
      r = gp_string(string("#n"));
      num_div = gtolong(r);
      
      for(i=1; i<= num_div; ++i) {

	sprintf(b,"n[ %d ];", i );
	r = gp_read_str( b );
	d = gtolong(r);
	e = Q / d;
	//	cout <<"d "<<d<<" e "<<e<<endl;
	if((d<=N)&&(e<=M)){ 
	  coor[0] = d; //x1
	  coor[1] = y1;
	  coor[2] = x2;
	  coor[3] = e;
	  return coor;
	}
      }
    }
  }
  coor[0]=0;
  coor[1]=0;
  coor[2]=0;
  coor[3]=0;
  return coor;

}

typedef long long int64;



int main()
{
  vector<int> coor;
  cout <<setiosflags(ios::fixed) << setprecision(6);
  int i,j,k,C,N,M,A,x1,y1,x2,y2;
  cin >>C;
  
  pari_init(100000000,100000);

  
  //  for(j=0; j<100000000; ++j) k = k*3+1;


  for(i=0; i<C; ++i) {
    
    cin >>N >>M >>A;

    coor = kan(N,M,A);
    


    cout << "Case #" << i+1 << ": ";

    if((coor[0]==0)&&(coor[1]==0)&&(coor[2]==0)&&(coor[3]==0)) {
      cout <<"IMPOSSIBLE";
    }
    else {
      cout <<"0 0 "<<coor[0]<<" "<<coor[1]<<" "<<coor[2]<<" "<<coor[3];
    }
    cout <<endl;
  }


}
