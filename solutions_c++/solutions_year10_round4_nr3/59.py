#include <iostream>
#include <vector>
using namespace std;

bool nothing(vector<vector<bool> > &v)
{
  for (int i=0; i<=100; i++){
    for (int j=0; j<=100; j++){
      if (v[i][j]) return false;
    }
  }
  return true;
}

int main()
{
  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    int r; cin>>r;
    vector<vector<bool> > bd(101, vector<bool>(101, false));
    for (int i=0; i<r; i++){
      int x1, x2;
      int y1, y2;
      cin>>x1>>y1>>x2>>y2; 
      for (int x=x1; x<=x2; x++){
	for (int y=y1; y<=y2; y++){
	  bd[y][x]=true;
	}
      }
    }
    int turn=0;
    for (; ; turn++){
      if (nothing(bd)) break;
      vector<vector<bool> > nbd(101, vector<bool>(101, false));
      for (int i=1; i<=100; i++){
	for (int j=1; j<=100; j++){
	  if (bd[i][j]){
	    nbd[i][j]=bd[i-1][j]||bd[i][j-1];
	  }
	  else{
	    nbd[i][j]=bd[i-1][j]&&bd[i][j-1];
	  }
	}
      }
      bd=nbd;
    }
    cout<<"Case #"<<c<<": "<<turn<<endl;
  }
  return 0;
}
