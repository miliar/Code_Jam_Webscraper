#include <iostream>
#include <vector>

using namespace std;

const int infinity=999999999;

int solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int n=solve();
    cout<<"Case #"<<i+1<<": ";
    if(n==infinity)
      cout<<"IMPOSSIBLE\n";
    else
      cout<<n<<'\n';
  }
}

int gates;
vector<int> gate,changeable;
vector<vector<int> > value;

//1== AND
void evaluate(int n);

int solve(){
  int m,v;
  cin>>m>>v;
  gates=(m-1)/2;
  gate=changeable=vector<int>(gates);
  value=vector<vector<int> >(m,vector<int>(2,infinity));
  for(int i=0;i<gates;i++)
    cin>>gate[i]>>changeable[i];
  for(int i=gates;i<m;i++){
    int x;
    cin>>x;
    value[i][x]=0;
  }
  //for(int i=0;i<m;i++) cout<<i<<": "<<value[i][0]<<"<->"<<value[i][1]<<'\n';
  evaluate(0);
  return value[0][v];
}

int eval(int l,int r,int gate){
  if(gate==1)
    return l && r;
  return l || r;
}

void evaluate(int n){
  if(n>=gates)
    return;
  int left=n*2+1;
  int right=left+1;
  evaluate(left);
  evaluate(right);
  for(int c=0;c<=changeable[n];c++)
    for(int l=0;l<2;l++)
      for(int r=0;r<2;r++){
        int g=gate[n];
        if(c) g=!g;
        int cost=c+ value[left][l]+ value[right][r];
        int v=eval(l,r,g);
        value[n][v]=min(value[n][v],cost);
      }
  //cout<<n<<": "<<value[n][0]<<'-'<<value[n][1]<<'\n';
}
