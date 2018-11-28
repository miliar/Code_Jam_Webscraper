#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
  int n=0,N,Nmilk,Ncust;
  cin>>N;
  vector<vector<int> > T (2001);
  while(n++<N){
    cin>>Nmilk>>Ncust;
    for (int i=0;i<Ncust;i++){
      T[i].resize(2*Nmilk);
      for (int j=0;j<Nmilk*2;j++){
	T[i][j]=0;
      }
      int x,y,p;
      cin>>p;
      for (int j=0;j<p;j++){
	cin>>x>>y;
	x--;
	T[i][x*2+y]=1;
      }
    }
    /*
    for (int i=0;i<5;i++){
      cout<<T[1][2*i]<<' '<<T[1][2*i+1]<<endl;
    }
    /**/
    int minbits=30;
    int bestbits;
    int curbits;
    vector<int> test(Nmilk*2);
    for (int i=0;i<(1<<Nmilk);i++){
      curbits=0;
      for (int j=0;j<Nmilk;j++){
	if (i&(1<<j))
	  curbits++;
      }
      if (curbits>=minbits) continue;
      for (int j=0;j<Nmilk;j++){
	if (i&(1<<j)){
	  test[2*j]=0;
	  test[2*j+1]=1;
	}
	else{
	  test[2*j]=1;
	  test[2*j+1]=0;
	}
      }
      /*
      for (int j=0;j<Nmilk;j++){
	if (i&(1<<j)){
	  cout<<"0 ";
	}
	else
	  cout<<"1 ";
      }
      */
      int ok=1;
      int valid=0;
      for (int j=0;j<Ncust;j++){
	valid=0;
	for (int k=0;k<2*Nmilk;k++){
	  if (test[k]&&T[j][k]){
	    valid=1;
	    break;
	  }
	}
	if (!valid){
	  ok=0;
	  break;
	}
      }
      if (ok){
	minbits = curbits;
	bestbits = i;
      }
    }
    if (minbits == 30){
      printf("Case #%d: IMPOSSIBLE\n",n);
    }
    else{
      printf("Case #%d: ",n);
      for (int i=0;i<Nmilk;i++){
	if (bestbits&(1<<i)){
	  printf("1 ");
	}
	else{
	  printf("0 ");
	}
      }
      printf("\n");

    }
  }
}
