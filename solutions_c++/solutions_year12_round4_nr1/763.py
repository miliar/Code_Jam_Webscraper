/*
*  Javier Segovia
*  0.016
*/
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair
#define MIN(a,b) ((a)<(b)?(a):(b))

int N;
int D[10005],L[10005],J[10005];
int DEST;
int bfs[100000000];
bool seen[10005];

bool check(){
	int ac=0,total=0,li,ad,al,nd,nl;
	bfs[total++] = 0 ; //index
	//bfs[total++] = MIN(D[0],L[0]); //jump
	J[0] = MIN(D[0],L[0]);
	seen[0] = true;
	bool ok=false;
	int jump,dist;
	
	while(ac<total){
		li = bfs[ac++];
		jump = J[li];
		ad = D[li];
		al = L[li];
		if(ad + jump >= DEST){ ok=true; break;}
		for (int i=li+1; i<N ; i++) {
			nd = D[i];
			nl = L[i];
			if( (ad + jump >= nd) ){
				dist = nd - ad ;
				if(nl < dist){ dist = nl; }
				if(J[i] < dist){ bfs[total++] = i; J[i] = dist;}
			}
			else break;
		}
	}
	
	return ok;
}

int main(){
	int kases; cin>>kases;
	for (int k=1; k<=kases; k++) {
		cin>>N;
		for (int i=0; i<N ; i++) {
			seen[i] = false; J[i] = 0;
			cin>>D[i]>>L[i];
		}
		cin>>DEST;
		if(check()) cout<<"Case #"<<k<<": YES"<<endl;
		else cout<<"Case #"<<k<<": NO"<<endl;
	}
}