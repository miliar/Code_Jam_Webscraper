#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<utility>
#include<algorithm>
#include<cmath>
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) ((a)>0?(a):(-(a)))
#define EPS (0.000000001)
#define EQ (a,b) ((ABS(a)-(b))<(EPS))
using namespace std;
double bo[1000][1000];

double compx (int x, int y, double cx, double cy){
	double f= bo[x][y];
	double lx = x-cx;
	double ly = y-cy;
	double ld = sqrt(lx*lx+ly*ly);
	return f*lx/ld;
}

double compy (int x, int y, double cx, double cy){
	double f= bo[x][y];
	double lx = x-cx;
	double ly = y-cy;
	double ld = sqrt(lx*lx+ly*ly);
	return f*ly/ld;
}

int main(){
	int cas;
	cin>>cas;
	for(int ca = 1; ca<=cas; ++ca){
		int n;
		int m;
		int X;
		cin>>n>>m>>X;
		string s;
		for(int i=0; i<n; ++i){
			cin>>s;
			for(int j=0; j<m; ++j){
				bo[i][j] = (double)(s[j]-'0'+X);
			}
		}
		int curmax = 3;
		bool found = false;
		for(int i=0; i<n; ++i){
			for(int j=0; j<m; ++j){
				for(int k=found?curmax+1:3; k<=n; ++k){
					if(i+k-1>=n ||j+k-1>=m) break;
					double cx = i+i+k-1;
					double cy = j+j+k-1;
					cx/=2; cy/=2;
					double sumx = 0;
					double sumy = 0;
					for(int t=0; t<k; ++t){
						for(int tt=0; tt<k; ++tt){
							if( (t==0 && tt==0) || (t==k-1 && tt==0) || (t==0 && tt==k-1) ||(t==k-1 && tt==k-1) )
								continue;
							if(i+t ==cx && j+tt==cy) continue;
							
							double tx = (cx-(i+t))*bo[i+t][j+tt];
							double ty = (cy-(j+tt))*bo[i+t][j+tt];
							//double tx = compx(i+t,j+tt, cx, cy);
							//double ty = compy(i+t,j+tt, cx, cy);
							sumx+=tx;
							sumy+=ty;
							//if(i==0 && j==0 && k==3) cout<<i+t<<" "<<j+tt<<" "<<cx<<" "<<cy<<" "<<tx<<" "<<ty<<" "<<sumx<<" "<<sumy<<endl;
						}
					}
					
					if ( ABS(sumx) < EPS && ABS(sumy) < EPS){
						found=true;
						curmax = MAX(k,curmax);
					//	cout<<i<<" "<<j<<endl;
					}
				}
			}
		}
		if (!found)
			cout<<"Case #"<<ca<<": IMPOSSIBLE"<<endl;
		else 
			cout<<"Case #"<<ca<<": "<<curmax<<endl;
	}
}