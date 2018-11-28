#include <iostream>
#include <math.h>
#include <algorithm>

#define  rep(i,a,b) for(int i=a; i<=b; i++) 

using namespace std; 
int o[1000],b[1000]; 
int t[1000],tt=1; 
int ot=1, bt= 1; 

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout); 
	int T; 
	cin >> T; 
	int N; 
	char ch;
	int x, y; 


	rep(k,1,T){
		cin >> N; 
		ot = 0; bt = 0; 
		tt = 0; 
		rep(i,1,N) {
			cin >> ch >> x; 
			tt++; 
			if (ch=='O') {
				ot ++; 
				o[ot]=x; 
				t[tt]=0; 
			}
			else {
				bt++;
				b[bt]=x; 
				t[tt]=1; 
			}
		}
		int vo=1, vb=1; 
		int time=0;  
		int m; 

		ot = 1; bt = 1; 
		rep(i,1,N){
			if (t[i]==0){
				m = abs(vo-o[ot])+1;
				time+=m;
				vo = o[ot]; 
				if (abs(b[bt]-vb)<=m) vb=b[bt]; 
				else {
					if (b[bt]>vb) vb += m; 
					else vb -= m; 
				}
				ot++; 
			}	
			else {
				m = abs(vb-b[bt])+1;
				time+=m;
				vb = b[bt]; 
				if (abs(o[ot]-vo)<=m) vo=o[ot]; 
				else {
					if (o[ot]>vo) vo += m; 
					else vo -= m; 
				}
				bt++; 
			}
		}
		cout << "Case #"<<k<< ": "<<time<<endl; 
	}

}