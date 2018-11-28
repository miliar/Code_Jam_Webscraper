#include <iostream>
using namespace std;
int p[105][105];
int a[105][105];
int dx[4]={-1,0,0,1},dy[4]={0,-1,1,0};
char v[105][105];


int root(int x,int y){
  if (p[x][y]==x*1000+y)
    return p[x][y];
  
  p[x][y] = root(p[x][y]/1000,p[x][y]%1000);
  return p[x][y];
}

bool sameset(int x1,int y1,int x2,int y2){
  return (root(x1,y1)==root(x2,y2));
}

void unionset(int x1,int y1,int x2,int y2){
  int x3 = root(x1,y1);
  int x4 = root(x2,y2);
  int y4 = x4%1000;
  x4/=1000;
  p[x4][y4] = x3;
}

int main(){
  int n;
  int t;
  
  cin >> t;
  int cas = 0;
  while (t--){
    cout << "Case #"<<++cas<<":\n";
    int n,m;
    memset(v,0,sizeof v);
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
	cin >> a[i][j];
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j){
	p[i][j] = i*1000+j;
      }
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j){
	int testx,testy,testans;	
	testx=testy=0;
	testans = a[i][j];
	
	for (int k = 0; k < 4; ++k){
	  if (i+dx[k]>=0 && i+dx[k]<n && j+dy[k]>=0 && j+dy[k]<m)
	    if (a[i+dx[k]][j+dy[k]]<testans){
	      testx = dx[k];
	      testy = dy[k];
	      testans = a[i+dx[k]][j+dy[k]];
	    }
	}
	//	cout << i <<" "<<j <<" "<< i+testx<<" "<<j+testy<<endl;
	
	if (!sameset(i+testx,j+testy,i,j))
	  unionset(i+testx,j+testy,i,j);
      }
    char x = 'a';
    
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j){
	int x1,y1;
	y1 = root(i,j);
	x1 = y1/1000;
	y1%=1000;
	if (v[x1][y1]==0){
	  v[x1][y1] = x++;
	}
	//cout << i <<" "<<j << " " << x1 <<" "<<y1 <<endl;
      }
    for (int i = 0; i < n; ++i){
      for (int j = 0; j < m-1; ++j){
	int x1,y1;
	y1 = root(i,j);
	x1 = y1/1000;
	y1%=1000;
	cout << v[x1][y1] <<" ";
      }
      int x1,y1;
      y1 = root(i,m-1);
      x1 = y1/1000;
      y1%=1000;
      cout << v[x1][y1] <<endl;
    }
  }
}
