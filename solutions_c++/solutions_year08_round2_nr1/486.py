#include <cstdio>
#include <vector>

using namespace std;
typedef unsigned long long int llu;
int main(){
  vector<pair<llu,llu> > tree;
  vector<pair<llu,llu> > tmp;
  llu X,Y,x0,y0,A,B,C,D,n,N,M,i,xsum,ysum,wynik;
  scanf("%llu",&N);
  for(unsigned int zest =1; zest<=N;zest++){

    scanf("%llu %llu %llu %llu %llu %llu %llu %llu",&n, &A, &B, &C, &D, &x0, &y0, &M);

    tree.push_back(make_pair<llu,llu>(x0,y0));
    X=x0;Y=y0;
    for(i=1;i<n;i++){
      X=((A*X)%M+B%M) % M;
      Y=((C*Y)%M+D%M) % M;
      tree.push_back(make_pair<llu,llu>(X,Y));
      //printf("drzewo %d %d size=%d\n",X,Y,tree.size());
    }

    wynik=0;
    for(unsigned int i=0;i<n;i++){
      for(unsigned int j=i+1;j<n;j++){
	if(j!=i){
	  for(unsigned int k=j+1;k<n;k++){
	    if(k!=j && k!=i){
	      xsum=(tree[i].first)%3+(tree[j].first)%3+(tree[k].first)%3;
	      ysum=(tree[i].second)%3+(tree[j].second)%3+(tree[k].second)%3;
	      if(xsum%3==0 && ysum%3==0){
		wynik++;
	      }
	    }
	  }
	}
      }
    }
    printf("Case #%d: %llu\n",zest,wynik);
    tree=tmp;
  }
  return 0;
}
