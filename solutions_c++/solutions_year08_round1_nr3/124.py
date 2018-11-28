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

using namespace std;

void printmat( vector<int> A )
{
  cout <<A[0]<<","<<A[1]<<endl<<A[2]<<","<<A[3]<<endl;
}

vector<int> matsqr( vector<int> A ) 
{
  vector<int> As(4);

  int a = A[0];
  int b = A[1];
  int c = A[2];
  int d = A[3];


  As[0] = (a*a + c*b) % 1000; 
  As[1] = (b*a + d*b) % 1000;
  As[2] = (c*a + d*c) % 1000; 
  As[3] = (c*b + d*d) % 1000;

  return As;
}

int tracem1( vector<int> A ) 
{
  int a;
  a = (A[0] + A[3] - 1) % 1000;
  if(a<0) a+=1000;
  return a;
}

vector<int> matmul( vector<int> A, vector<int> B )
{

  vector<int> C(4);
  int a = A[0];
  int b = A[1];
  int c = A[2];
  int d = A[3];
  int e = B[0];
  int f = B[1];
  int g = B[2];
  int h = B[3];
  
  C[0] = (e*a + g*b) % 1000;
  C[1] = ( f*a + h*b) % 1000;

  C[2] = (e*c + g*d) % 1000;
  C[3] = ( f*c + h*d) % 1000;
  return C;


}

vector<int> matpow( vector<int> A, long n )
{
  vector<int> C(4);
  C[0] = 1;
  C[1] = 0;
  C[2] = 0;
  C[3] = 1;

  while(n) {
    if( n & 1 ) {
      C = matmul(C,A);
    }
    A = matsqr(A);
    n >>=1;
    //    cout <<"n "<<n<<endl;
    //printmat(C);
    //cout<<"--------"<<endl;
  }
  return C;
}

int main()
{
  cout <<setiosflags(ios::fixed) << setprecision(6);
  int i,j,k,N,r;
  cin >>N;

  vector<int> A(4),B(4);
  A[0] = 0;
  A[1] = -4;
  A[2] = 1;
  A[3] = 6;

  //  printmat(A);
  //cout <<"++++++"<<endl;
  //B =   
  //cout <<"lllllllllll"<<endl;
  //  printmat(matpow(A,10000));
  
  for(i=0; i<N; ++i) {

    cin >>k;



    cout << "Case #" << i+1 << ": ";
    r = tracem1( matpow(A,k));
    if(r < 10) cout <<"00";
    else if (r < 100) cout <<"0";
    cout <<r;
    cout <<endl;
  }


}
