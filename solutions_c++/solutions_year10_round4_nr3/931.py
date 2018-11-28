#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define S 101
int bd[200][200] = {0};
int bd2[200][200] = {0};

int main(){
  char tmp[256];

  int cases;
  cin.getline(tmp,256);
  sscanf(tmp,"%d",&cases);

  int R,X1,X2,Y1,Y2;
  for(int i=1;i<=cases;++i)
  {
    cin.getline(tmp,256);
    sscanf(tmp,"%d",&R);
    for(int y=0;y<S;++y)for(int x=0;x<S;++x){bd[y][x] = 0;bd2[y][x]=0;}

    for(int j=0;j<R;++j){
      cin.getline(tmp,256);
      sscanf(tmp,"%d %d %d %d",&X1,&Y1,&X2,&Y2);

      //printf("%d %d %d %d\n",X1,Y1,X2,Y2);

      for(int y=Y1;y<=Y2;++y)for(int x=X1;x<=X2;++x){bd[y][x] = 1;}
    }

    int t = 0;
    while(1){

      //for(int y=0;y<20;++y){for(int x=0;x<20;++x){cout<<(bd[y][x]);}cout<<endl;}
      //cout<<endl;
      int f=1;
      for(int y=0;y<S;++y)for(int x=0;x<S;++x){if(bd[y][x]){f=0;break;}}
      if(f)break;

      for(int y=0;y<S;++y)for(int x=0;x<S;++x){bd2[y][x]=bd[y][x];}

      for(int y=1;y<S;++y)for(int x=1;x<S;++x){
	    if(bd2[y][x] && !bd2[y][x-1] && !bd2[y-1][x])bd[y][x]=0;
	    else if(!bd2[y][x] && bd2[y][x-1] && bd2[y-1][x])bd[y][x]=1;
	    else bd[y][x]=bd2[y][x];
	}

      ++t;
    }

    //for(int y=0;y<20;++y){for(int x=0;x<20;++x){cout<<(bd[y][x]);}cout<<endl;}
    
    cout<<"Case #"<<i<<": "<<t<<endl;
  }

  return 0;
}
