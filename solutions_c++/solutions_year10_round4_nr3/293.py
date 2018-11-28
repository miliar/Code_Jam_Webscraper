#include <iostream>
#include <cstring>
using namespace std;
bool arr[2][256][256];
int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		memset(arr,0,sizeof(arr));
		int R;cin>>R;
		for(int i=0; i<R; ++i) {
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			for(int y=y1; y<=y2; ++y)
				for(int x=x1; x<=x2; ++x)
					arr[0][y][x]=1;
		}
		int p=0;
		int r=0;
		for(; ; ++r) {
			bool alive=0;
			for(int i=1; i<101; ++i)
				for(int j=1; j<101; ++j)
					alive |= arr[p][i][j];
			if (!alive) break;

			for(int i=1; i<101; ++i)
				for(int j=1; j<101; ++j) {
					int pn=arr[p][i-1][j], pw=arr[p][i][j-1], pp=arr[p][i][j];
					arr[!p][i][j] = (pn&pw) | (pp & (pn|pw));
				}
			p=!p;
		}
		cout<<"Case #"<<a<<": "<<r<<'\n';
	}
}
