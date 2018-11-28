#include <iostream>
#include <vector>

using namespace std;

int answer(const vector<vector<int> >& square,int n);
vector<vector<int> > squarize(const vector<vector<int> >& diamond,int k);
int row_size(int n,int r);
void print(string s,vector<vector<int> >& v);

int main(){
  int t;
  cin>>t;
  for(int z=0;z<t;z++){
    int n;
    cin>>n;
    vector<vector<int> > diamond(2*n-1);
    for(int i=0;i<diamond.size();i++){
      int row=row_size(n,i);
      diamond[i].resize(row);
      for(int j=0;j<row;j++)
        cin>>diamond[i][j];
    }
    vector<vector<int> > square=squarize(diamond,n);
    print("diamond",diamond);
    print("square",square);
    cout<<"Case #"<<z+1<<": "<<answer(square,n)<<'\n';
  }
}

bool works(const vector<vector<int> >& square,int n,int k);
bool works(const vector<vector<int> >& square,int n,int k,int r,int c);

int answer(const vector<vector<int> >& square,int n){
  for(int k=n;;k++)
    if(works(square,n,k))
      return k*k-n*n;
}

bool works(const vector<vector<int> >& square,int n,int k){
  for(int r=0;r+n<=k;r++)
    for(int c=0;c+n<=k;c++)
      if(works(square,n,k,r,c))
        return true;
  return false;
}

const pair<int,int> bad(-1,-1);
pair<int,int> inside(pair<int,int> p,int n,int k,int r,int c);
pair<int,int> main_diagonal(int k,int r,int c);
pair<int,int> cross_diagonal(int k,int r,int c);

bool works(const vector<vector<int> >& square,int n,int k,int r,int c){
  for(int lr=0;lr<n;lr++)
    for(int lc=0;lc<n;lc++){
      int br=lr+r,bc=lc+c;
      pair<int,int> mp=main_diagonal(k,br,bc);
      mp=inside(mp,n,k,r,c);
      if(mp!=bad && square[mp.first][mp.second]!=square[lr][lc])
        return false;
      pair<int,int> cp=cross_diagonal(k,br,bc);
      cp=inside(cp,n,k,r,c);
      if(cp!=bad && square[cp.first][cp.second]!=square[lr][lc])
        return false;
    }
  return true;
}

int row_size(int n,int r){
  int ret=r+1;
  if(ret>n)
    ret=2*n-ret;
  return ret;
}

pair<int,int> inside(pair<int,int> p,int n,int k,int r,int c){
  int lr=p.first-r;
  int lc=p.second-c;
  if(lr>=0 && lr<n && lc>=0 && lc<n)
    return make_pair(lr,lc);
  return bad;
}

pair<int,int> main_diagonal(int k,int r,int c){
  return make_pair(c,r);
}

pair<int,int> cross_diagonal(int k,int r,int c){
  return make_pair(k-1-c,k-1-r);
}

vector<vector<int> > squarize(const vector<vector<int> >& diamond,int n){
  vector<vector<int> > square(n,vector<int>(n));
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++){
      int r=i+j;
      int c=j;
      if(r>=n){
        int rs=row_size(n,r);
        int ii=n-1-i;
        c=ii;
        //c=rs-1-ii;
      }
      square[i][j]=diamond[r][c];
    }
  return square;
}

void print(string s,vector<vector<int> >& v){
  return;
  cout<<s<<":\n";
  for(int i=0;i<v.size();i++){
    for(int j=0;j<v[i].size();j++)
      cout<<v[i][j]<<' ';
    cout<<'\n';
  }
}
