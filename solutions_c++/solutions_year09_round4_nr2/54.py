#include <iostream>
#include <vector>

using namespace std;

const int infinity=999999999;
const char ground='#',air='.';
int answer();

int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    int d=answer();
    if(d<infinity)
      cout<<"Case #"<<i<<": Yes "<<d<<'\n';
    else
      cout<<"Case #"<<i<<": No\n";
  }
}

int fall,key=0;
vector<string> map;

int rights(int r,int c,char type){
  assert(map[r][c]==type);
  while(c+1<map[r].size() && map[r][c+1]==type) c++;
  return c;
}

int lefts(int r,int c,char type){
  assert(map[r][c]==type);
  while(c-1>=0 && map[r][c-1]==type) c--;
  return c;
}

const int N=64;
int cached[N][N][N][N];
int cache[N][N][N][N];
int memo(int r,int c,int left,int right);

int jump(int r,int c,int left,int right){
  //cout<<"jumping: "<<r<<','<<c<<": "<<left<<','<<right<<'\n';
  int f=1;
  while(r+1<map.size() && map[r+1][c]==air){
    r++;
    f++;
  }
  if(f>fall)
    return infinity;
  if(f>1)
    return memo(r,c,lefts(r,c,air),rights(r,c,air));
  int la=left;
  //cout<<"la: "<<la<<'\n';
  if(la>0 && map[r][la-1]==air)
    la=lefts(r,la-1,air);
  int ra=right;
  //cout<<"ra: "<<ra<<'\n';
  if(ra+1<map[r].size() && map[r][ra+1]==air)
    ra=rights(r,ra+1,air);
  //cout<<"jumped\n";
  return memo(r,c,la,ra);
}

int memo(int r,int c,int left,int right){
  if(cached[r][c][left][right]==key)
    return cache[r][c][left][right];
  cached[r][c][left][right]=key;
  //cout<<r<<','<<c<<": "<<left<<','<<right<<'\n';
  int& ret=cache[r][c][left][right]=infinity;
  if(r+1==map.size())
    return ret=0;
  assert(map[r+1][c]==ground);
  int rg=rights(r+1,c,ground),lg=lefts(r+1,c,ground);
  lg=max(left,lg);
  rg=min(right,rg);
  //cout<<"grounds: "<<lg<<','<<rg<<'\n';
  if(left<lg)
    ret=min(ret,jump(r+1,lg-1,lg-1,lg-1));
  if(right>rg)
    ret=min(ret,jump(r+1,rg+1,rg+1,rg+1));
  for(int spot=lg;spot<=rg;spot++){
    //cout<<"a good spot: "<<spot<<'\n';
    int ls=spot-lg,rs=rg-spot;
    for(int d=1;d<=ls;d++)
      ret=min(ret,d+jump(r+1,spot-1,spot-d,spot-1));
    for(int d=1;d<=rs;d++)
      ret=min(ret,d+jump(r+1,spot+1,spot+1,spot+d));
  }
  return ret;
}


int answer(){
  int r,c;
  cin>>r>>c>>fall;
  map=vector<string>(r);
  for(int i=0;i<map.size();i++)
    cin>>map[i];
  key++;
  return memo(0,0,0,rights(0,0,air));
}
