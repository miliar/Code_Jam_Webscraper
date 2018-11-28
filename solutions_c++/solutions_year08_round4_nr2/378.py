#include<iostream>
#include<cstdlib>
#include<cmath>

using namespace std;
int N, M, A; 
void find(int &x2, int &x3, int &y2, int &y3){
	for(x2=0; x2<=N; x2++)for(x3=0; x3<=N; x3++)for(y2=0;y2<=M;y2++)for(y3=0;y3<=M;y3++)
		if(abs(x2*y3-x3*y2)==A)return;
	x2=-1;
}
int main(){
	int C; cin >> C;
	for(int t=1; t<=C; t++){
		cin >> N >> M >> A;
		int x2,x3,y2,y3;
		find(x2,x3,y2,y3);
		cout << "Case #" << t << ": ";
		if(x2==-1)cout << "IMPOSSIBLE\n";
		else{
			cout << "0 0 " << x2 << " " << y2 << " " << x3 << " " << y3 << "\n";
		}
	}
}	
