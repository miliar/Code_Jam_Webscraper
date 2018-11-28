#include<iostream>
#include<vector>
using namespace std;

int main(){
  int i,j;
  int poso,posb;
  int t,n,time;
  vector<int> p;
  vector<char> r;
  int tmpi;
  char tmpc;
  int dis,tdis;
  int dif;

  cin >> t;

  for(i=0;i<t;i++){
    cin >> n;
    r.clear();
    p.clear();
    for(j=0;j<n;j++){
      cin >> tmpc >> tmpi;
      r.push_back(tmpc);
      p.push_back(tmpi);
    }
    poso = 1;
    posb = 1;
    time = 0;
    for(j=0;j<n;j++){
      tdis = 0;
      dif = 0;
      while(j+dif<n && r[j+dif] == r[j]){
	if(r[j] == 'O')dis = poso - p[j+dif];
	else dis = posb - p[j+dif];
	if(dis<0)dis *= -1;
	dis++;
	tdis += dis;
	if(r[j] == 'O')poso = p[j+dif];
	else posb = p[j+dif];
	dif++;
      }
      if(r[j] == 'O'){
	time += tdis;
	if(j+dif>=n)break;
	dis = posb-p[j+dif];
	if(dis<0)dis *= -1;
	if(dis<=tdis)posb = p[j+dif];
	else if(posb>p[j+dif]){
	  posb -= tdis;
	}else{
	  posb += tdis;
	}
      }else{
	time += tdis;
	if(j+dif>=n)break;
	dis = poso-p[j+dif];
	if(dis<0)dis *= -1;
	if(dis<=tdis)poso = p[j+dif];
	else if(poso>p[j+dif]){
	  poso -= tdis;
	}else{
	  poso += tdis;
	}
      }
      j += dif-1;
    }
    cout << "Case #" << i+1 << ": " << time << endl;
  }
}

