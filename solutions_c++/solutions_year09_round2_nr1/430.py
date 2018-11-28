#include<iostream>
#include<set>
#include<vector>
using namespace std;

const int N = 1000001;
int l,a,n;
string temp;
double pr[N];
vector<int> za[N]; 
set<string> zb;
string cech[N];
char tree[N];
int nr,poz;
int roz;

void wczyt(int kt){
  poz++;
  double k;
  int y=0;
  sscanf(tree+poz,"%lf",&k);
  while((tree[poz]>='0' && tree[poz]<='9') || tree[poz]=='.')
    poz++;
  pr[kt] = k;
  if(tree[poz] == ')'){
    poz++;
    return;
  }
  else{
    while(isalpha(tree[poz]))
      cech[kt] += tree[poz++];
    za[kt].push_back(nr+1);
    wczyt(++nr);
    za[kt].push_back(nr+1);
    wczyt(++nr);
    poz++;
  }
}

double go(int y){
  if(za[y].empty()) return pr[y];
  if(zb.find(cech[y]) != zb.end()){
    return go(za[y][0])*pr[y];
  }
  else
    return go(za[y][1])*pr[y];
}

main(){
char qwer;
  int t;
  cin >> t;
  scanf("\n");
  for(int q=1;q<=t;q++){
     cin >> l;
   scanf("\n");
     roz = 0;
     for(int i=1;i<=l;i++){
       getline(cin,temp);
       for(int j=0;j<temp.size();j++) {
         if(temp[j] != ' ') tree[roz++] = temp[j];
       }
     }
//     printf("tr : %s\n",tree);
//     printf("roz : %d\n",roz);
     nr = 0,poz=0;
     wczyt(++nr);
//     printf("poz : %d\n",poz);
     printf("Case #%d:\n",q);
     int w;
     cin >> w;
     string y;
     int qw;
     for(int i=1;i<=w;i++){
       cin >> y;
       cin >> qw;
       zb.clear();
       for(int j=1;j<=qw;j++){
         cin >> y;
         zb.insert(y);
       }
       printf("%.7lf\n",go(1));
     }
     for(int i=1;i<=nr;i++){
       za[i].clear();
       cech[i].clear();
     }
  }
}
