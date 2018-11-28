#include <iostream.h>

int N;
long int Frequences[1000];

void main() {
  int I,J;
  int Q;

  cin>>N;
  for (Q=1;Q<=N;++Q) {
    int P,K,L;
    cin>>P>>K>>L;
    cout<<"Case #"<<Q<<": ";
    if (L<=P*K) {
      for (I=0;I<L;++I) cin>>Frequences[I];
      for (I=0;I<L-1;++I)
	for (J=I+1;J<L;++J)
	  if (Frequences[I]<Frequences[J]) {
	    long int Temp=Frequences[I];
	    Frequences[I]=Frequences[J];
	    Frequences[J]=Temp;
	  }
      long int Result=0;
      int Counter=0;
      for (int I=0;I<L;++I) {
	Result+=((long int)(Counter/K)+1)*Frequences[I];
	++Counter;
      }
      cout<<Result;
    } else cout<<"Impossible";
    cout<<endl;
  }
}