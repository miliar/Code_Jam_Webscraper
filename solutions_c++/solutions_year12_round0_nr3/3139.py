//
// Recyle number
// 2012 Apr 14, quantum
//
#include <iostream>
#include <cmath>
using namespace std;

int pow(int a,int b){
  int tmp=1;
  for(int i=0;i<b;i++){
    tmp*=a;
  }
  return tmp;
}
int ketasu(int n){
  int tmp,keta;
  keta=1;
  tmp=n;
  while(tmp/10 >0){
      keta++;
      tmp/=10;
  }
  return keta;
}
int main(int argc, char **argv){
  int T,A,B,tmp,kk,keta,colbit;
  int counter;
  int col[7];
  cin >>T; // first line
  //cout << "T="<<T<<endl;
  for(int j=1;j<=T;j++){
    counter=0;
    cin >> A;
    cin >> B;
    keta=ketasu(A);
    kk=pow(10,(keta-1));
    //    cout << "AB="<< A<<B<<endl;
    //   cout << "keta="<<keta <<endl;
    for(int i=A;i<=B;i++){ //n
      tmp=i;
      for(int k=0;k<keta;k++){	
	col[k]=tmp;
	tmp=tmp/10+(tmp%10)*kk; //m
	//	cout << "n=" << i <<" ;m=" <<tmp <<endl;
	if((tmp<=B) && (i<tmp)){
	  colbit=0;
	  for(int l=0;l<k;l++){
	    if(col[l]==tmp){colbit=1;}
	  }
	  //	  cout << "n=" << i <<" ;m=" <<tmp <<endl;
	  counter=counter+1-colbit;
	}
	for(int l=0;l<k;l++){
	  col[l]=0;
	}
      }
    }
    printf("Case #%d: %d \n",j,counter);
  }
  return 0;
}
