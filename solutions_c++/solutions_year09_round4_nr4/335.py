#include <iostream>  
#include <string>  
#include <vector>  
#include <set>  
#include <map>  
#include <algorithm>  
#include <math.h>  
#include <sstream>  
#include <ctype.h>  
#include <queue>  
#include <stack>  
#include <fstream>
#include <iomanip>
using namespace std;  

template<class Item>  
void display(vector<Item> v)  
{  
  for(int i=0; i<v.size(); i++)  
    cout << v[i] << ' ';  
  cout << '\n';  
}   

double d2(double X1, double Y1, double X2, double Y2)
{
	return sqrt((X2-X1)*(X2-X1) + (Y2-Y1)*(Y2-Y1) );
}


int main()
{

int L, D, N;

fstream In("d-small.in", ios::in);
fstream Out("d-small.out", ios::out);

int T;

In >> T;

for(int h=0; h<T; h++)
{
Out << "Case #" << h+1 << ": ";
In >> N;


vector<double> X(3, 0), Y(3, 0), R(3, 0);

for(int i=0; i<N; i++) In >> X[i] >> Y[i] >> R[i];

if(N ==1) Out << R[0] << endl;
if(N==2) Out << max(R[0], R[1]) << endl;

if(N==3)
{
	double d1 = max(R[0], (d2(X[1],Y[1],X[2],Y[2])+(R[1]+R[2]))/2.0);
	double da2 = max(R[1], (d2(X[0],Y[0],X[2],Y[2])+(R[0]+R[2]))/2.0);
	double d3 = max(R[2], (d2(X[1],Y[1],X[0],Y[0])+(R[1]+R[0]))/2.0);
	Out << setprecision(7) << min(d1,min(da2,d3)) << endl;


}

}
In.close();

Out.close();

return 0;

}
