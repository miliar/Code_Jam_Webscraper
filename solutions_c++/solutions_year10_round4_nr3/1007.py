#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<queue>
#include<stack>

using namespace std;

int tab[110][220];
int tmp[110][220];

int main(){
  int c;
  cin >> c;
  for(int id=1; id<=c; id++){
    int r;
    cin >> r;
    memset(tab,0,sizeof(tab));
    memset(tmp,0,sizeof(tmp));


    for(int i=0; i<r; i++){
      int x1,y1,x2,y2;
      cin >> x1 >> y1 >> x2 >> y2;
      if(x1>x2)swap(x1,x2);
      if(y1>y2)swap(y1,y2);    
      for(int y=y1; y <= y2; y++){
	for(int x = x1; x<=x2; x++){
	  tab[y][x] = 1;
	}
      }
    }
    int ans = 0;

    for(int t=0; t<250; t++){
      bool flg = true;
      memset(tmp,0,sizeof(tmp));
      for(int x=1; x<220; x++){
	for(int y=1; y<110; y++){
	  if(tab[y][x] == 0 && tab[y-1][x] == 1 && tab[y][x-1] == 1){
	    tmp[y][x] = 1;
	  }
	  else if(tab[y][x] == 1 && tab[y-1][x] == 0 && tab[y][x-1] == 0){
	    tmp[y][x] = 0;
	  }
	  else tmp[y][x] = tab[y][x];
	}
      }
      for(int x=1; x<220; x++){
	for(int y=1; y<110; y++){
	  tab[y][x] = tmp[y][x];
	  if(tab[y][x]==1)flg = false;
	}
      }
      if(flg){ans=t+1;break;}
    }

    cout << "Case #" << id << ": ";
    cout << ans << endl;
  }
return 0;
}

