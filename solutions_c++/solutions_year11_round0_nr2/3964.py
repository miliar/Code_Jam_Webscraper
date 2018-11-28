#include <iostream> 
#include <string>
using namespace std;


int zl(char c){
  switch (c){
    case 'Q': return 0;
    case 'W': return 1;
    case 'E': return 2;
    case 'R': return 3;
    case 'A': return 4;
    case 'S': return 5;
    case 'D': return 6;
    case 'F': return 7;
    default: return c;
  }
}

char lz(int i){
  switch (i){
    case 0: return 'Q';
    case 1: return 'W';
    case 2: return 'E';
    case 3: return 'R';
    case 4: return 'A';
    case 5: return 'S';
    case 6: return 'D';
    case 7: return 'F';
    default: return i;
  }
}

void wycz(bool t[8]){
  for(int i=0;i<8;i++)
    t[i]=false;
}

bool wyst(int i, bool opp[8][8], bool occ[8]){
  for(int j=0;j<8;j++)
    if ((occ[j])&&(opp[j][i]))
      return true;
  return false;
}

void rozwiaz(int Case, int com[8][8], bool opp[8][8], int inv[100], int C, int D, int N){
  int w[100];
  bool occ[8];
  int p_occ[8];
  int ind=0;
  w[0]=inv[0];
  wycz(occ);
  occ[w[0]]=true;
  p_occ[w[0]]=0;
  for(int i=1;i<N;i++){
    if ((w[ind]<8)&&(com[inv[i]][w[ind]]>=0)){
      if (p_occ[w[ind]]==ind)
	occ[w[ind]]=false;
      w[ind]=com[inv[i]][w[ind]];
      if ((w[ind]<8)&&(!occ[w[ind]])){
	occ[w[ind]]=true;
	p_occ[w[ind]]=ind;
      }
    }
    else if (wyst(inv[i],opp,occ)){
      if (i<N-1){
	wycz(occ);
	ind=0;
	i++;
	w[ind]=inv[i];
	occ[w[ind]]=true;
	p_occ[w[ind]]=ind;
      }
      else 
	ind=-1;
    }
    else {
      ind++;
      w[ind]=inv[i];
      if (!occ[w[ind]]){
	occ[w[ind]]=true;
	p_occ[w[ind]]=ind;
      }
    }
  }
  cout<<"Case #"<<Case<<": [";
  for(int i=0;i<=ind;i++){
    cout<<lz(w[i]);
    if (i<ind)
      cout<<", ";
  }
  cout<<"]"<<endl;
}

void przep(int inv[100], string s){
  for(int i=0;i<s.length();i++){
    inv[i]=zl(s[i]);
  }
}

int main(){
  int com[8][8];
  int inv[100];
  bool opp[8][8];
  char p1,p2,p3;
  string s;
  int T,C,D,N;
  cin>>T;
  for(int i=1;i<=T;i++){
    for(int j=0;j<8;j++)
      for(int k=0;k<8;k++){
	com[j][k]=-1;
	opp[j][k]=false;
      }
   cin>>C;
   for(int j=0;j<C;j++){
     cin>>p1;
     cin>>p2;
     cin>>p3;
     com[zl(p1)][zl(p2)]=zl(p3);
     com[zl(p2)][zl(p1)]=zl(p3);
   }
   cin>>D;
   for(int j=0;j<D;j++){
     cin>>p1;
     cin>>p2;
     opp[zl(p1)][zl(p2)]=true;
     opp[zl(p2)][zl(p1)]=true;
   } 
   cin>>N;
   cin>>s;
   przep(inv,s);
   rozwiaz(i,com,opp,inv,C,D,N);
  }
}