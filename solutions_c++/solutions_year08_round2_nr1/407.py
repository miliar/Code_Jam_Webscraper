#include <iostream>
#include <fstream>

using namespace std;

long long int b[3][3];

int main(int argc, char* argv[]){
  ifstream fin (argv[1]);
  ofstream fout (argv[2]);
 
  int testcase=0;
  fin>>testcase;
  for(int test=1;test<=testcase;test++){
    //cout<<"Test"<<test<<endl;
    for(int i=0;i<3;i++)
      for(int j=0;j<3;j++)
	b[i][j]=0;
    long long n,A,B,C,D,x0,y0,M;
    fin>>n>>A>>B>>C>>D>>x0>>y0>>M;
    long long X = x0, Y = y0;
    //cout<<X<<" "<< Y<<endl;
    b[X%3][Y%3]++;
    for(int i = 1; i<= n-1;i++){
      X = (A * X + B)% M;
      Y = (C * Y + D)% M;
      b[X%3][Y%3]++;
      //cout<<X<<" "<< Y<<endl;
    }
    /*
    for (int i=0;i<3;i++){
      for(int j=0;j<3;j++)
	cout<<b[i][j]<<" ";
      cout<<endl;
      }*/


    long long int num=0;
    //perm
    num+=b[0][0]*b[1][1]*b[2][2]+
      b[0][1]*b[1][2]*b[2][0]+
      b[0][2]*b[1][0]*b[2][1]+
      b[0][2]*b[1][1]*b[2][0]+
      b[0][1]*b[1][0]*b[2][2]+
      b[0][0]*b[1][2]*b[2][1];
    
    //col
    num+=b[0][0]*b[0][1]*b[0][2]+
      b[1][0]*b[1][1]*b[1][2]+
      b[2][0]*b[2][1]*b[2][2]+
      b[0][0]*b[1][0]*b[2][0]+ 
      b[0][1]*b[1][1]*b[2][1]+
      b[0][2]*b[1][2]*b[2][2];

    //pow
    for(int i=0;i<3;i++)
      for(int j=0;j<3;j++)
	num+=b[i][j]*(b[i][j]-1)*(b[i][j]-2)/6;
    cout<<"Case #"<<test<<": "<<num<<endl;


    fout<<"Case #"<<test<<": "<<num<<endl;
  }
}
