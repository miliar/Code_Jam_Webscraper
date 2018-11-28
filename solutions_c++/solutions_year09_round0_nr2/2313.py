#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstdio>

using namespace std;

vector< vector<int> > tab;
vector< string > ans;
int idx;
int h,w;

inline bool check(int nh,int nw){
  return ( 0<=nh && nh<h && 0<=nw && nw<w);
}

char dfs(int nh,int nw){
  int dh[]={-1, 0, 0, 1};
  int dw[]={ 0,-1, 1, 0};
  if(ans[nh][nw] != '!')return ans[nh][nw];

  int now_high=(1<<29);
  int mh,mw;
  int hne=-1,wne=-1;

  for(int i=0;i<4;i++){
    mh=nh+dh[i];
    mw=nw+dw[i];
    if(!check(mh,mw))continue;

    if(tab[nh][nw] > tab[mh][mw] &&
       tab[mh][mw] < now_high ){

      hne=mh;
      wne=mw;
      now_high=tab[mh][mw];
    }
  }
  if( hne==-1){
    if( ans[nh][nw] == '!'){
      ans[nh][nw]='a'+idx;
      idx++;
      return ans[nh][nw];
    }
    else return ans[nh][nw];
  }
  else {

    ans[nh][nw]=dfs(hne,wne);
    return ans[nh][nw];
  }

}


int main(){
  int t;
  cin>>t;
  for(int id=1;id<=t;id++){

    cin>>h>>w;

    idx=0;
    tab.resize(h);

    string tmp="";
    for(int i=0;i<w;i++){
      tmp+='!';
    }

    ans.clear();
    for(int i=0;i<h;i++){
      tab[i].clear();
      tab[i].resize(w);
      ans.push_back(tmp);
    }

    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++){
	int a;
	cin>>a;
	tab[i][j]=a;
      }
    }

    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++){
	dfs(i,j);
      }
    }
    cout<<"Case #"<<id<<":"<<endl;
    for(int i=0;i<h;i++){
      for(int j=0;j<w;j++){
	if(j)cout<<" ";
	cout<<ans[i][j];
      }
      cout<<endl;
    }
  }
  return 0;
}
