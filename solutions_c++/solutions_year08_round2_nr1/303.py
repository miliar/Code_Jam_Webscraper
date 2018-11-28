#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
  int n,i,j,k,l,T;
  long long A,B,C,D,x0,y0,X,Y,M;
  long long x[100000],y[100000];
  long long xy[3][3];
  long long wyn;
  cin>>T;
  for(i=1;i<=T;i++)
  {
	cin>>n;cin>>A;cin>>B;cin>>C;cin>>D;cin>>x0;cin>>y0;cin>>M;
	wyn=0;
	xy[0][0]=0;
	xy[0][1]=0;
	xy[0][2]=0;
	xy[1][0]=0;
	xy[1][1]=0;
	xy[1][2]=0;
	xy[2][0]=0;
	xy[2][1]=0;
	xy[2][2]=0;
	x[0]=x0;y[0]=y0;
	xy[x0%3][y0%3]++;
	for(j=1;j<n;j++){
		x[j]=(x[j-1]*A+B)%M;
		y[j]=(y[j-1]*C+D)%M;
		k=x[j]%3;
		l=y[j]%3;
		xy[k][l]++;
//cout << x[j] << " " << y[j] << endl;
	}
	for(j=0;j<3;j++){
		for(k=0;k<3;k++){
//cout<<xy[j][k]<<" ";
			wyn+=xy[j][k]*(xy[j][k]-1)*(xy[j][k]-2)/6;
		}
			wyn+=xy[j][0]*xy[j][1]*xy[j][2];
	}
	for(k=0;k<3;k++)
		wyn+=xy[0][k]*(xy[1][k])*(xy[2][k]);
	wyn+=xy[0][0]*xy[1][1]*xy[2][2];
	wyn+=xy[0][1]*xy[1][2]*xy[2][0];
	wyn+=xy[0][2]*xy[1][0]*xy[2][1];
	wyn+=xy[0][2]*xy[1][1]*xy[2][0];
	wyn+=xy[0][0]*xy[1][2]*xy[2][1];
	wyn+=xy[0][1]*xy[1][0]*xy[2][2];

    cout<<"Case #"<<i<<": "<<wyn<<endl;
  }

  return 0;
}
