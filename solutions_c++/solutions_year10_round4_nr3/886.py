#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<set>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
int A[1000][1000];
int cont=0,lastX,lastY;


void update(){ //cout<<"UP"<<endl;
	set<pair<int,int> > born;
	set<pair<int,int> > death;
	int nextX=lastX,nextY =lastY; //born
	for (int i=1; i<=300; i++) {
		for (int j=1; j<=300 ; j++) {
			//if(A[j][i]) cout<<"("<<i<<","<<j<<")"<<endl;
			if(A[j][i] && A[j-1][i+1] && !A[j][i+1]){  // east
				born.insert(MP(j,i+1));
				nextX = MAX(nextX,i+1);
				nextY = MAX(nextY,j);
			}
			if(A[j][i] && A[j+1][i-1] && !A[j+1][i]){ //south
				born.insert(MP(j+1,i));
				nextX = MAX(nextX,i+1);
				nextY = MAX(nextY,j);
			}
		}
	}
	
	//cout<<" IN: "<<endl; int n; cin>>n; n++;
	
	for (int i=1; i<=300; i++) {
		for (int j=1; j<=300 ; j++) {
			if(A[j][i] && !A[j-1][i] && !A[j][i-1]) death.insert(MP(j,i));
		}
	}
	
	lastX = nextX; lastY = nextY;
	
	for (set<pair<int,int> >::iterator it = born.begin(); it!=born.end(); it++) {
		A[(*it).X][(*it).Y] = 1; cont++;
	}
	
	
	for (set<pair<int,int> >::iterator it = death.begin(); it!=death.end(); it++) {
		A[(*it).X][(*it).Y] = 0;cont--;
	}
}

int main(){
	int K; cin>>K; K++;
	for (int k=1; k<K ; k++) {
		int days = 0;
		for (int i=0; i<1000; i++) {
			for (int j=0; j<1000; j++) {
				A[i][j] = 0;
			}
		}
		int R,X1,Y1,X2,Y2;  cont=lastX =lastY = 0;
		cin>>R;
		for (int r=0; r<R; r++) {
			cin>>X1>>Y1>>X2>>Y2;
			for (int i=X1; i<=X2; i++) {
				for (int j=Y1; j<=Y2; j++) {
					if(!A[i][j]){cont++; A[i][j] = 1; lastX = MAX(lastX,i); lastY = MAX(lastY,j);}
				}
			}
		}
		
		
		while (cont>0) { //cout<<"CONT: "<<cont<<endl; cin>>days; cout<<days<<endl;
			days++;
			update();
		}
		
		cout<<"Case #"<<k<<": "<<days<<endl;
	}
}