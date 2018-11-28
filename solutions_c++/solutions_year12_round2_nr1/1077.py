#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(){

  int T;cin>>T;
  for(int t=0;t<T;t++){//# of test;
    int N;cin>>N;//# of contestants;
    int J[200];
    int X=0;
    for(int i=0;i<N;i++){cin>>J[i];X+=J[i];}
    
    double res[200];
    for(int i=0;i<N;i++){res[i]=0.0;}
    
    //binary serach;
    for(int i=0;i<N;i++){// for each contestant;
      double lb=0.0;
      double ub=200.0*(double)N;
      int n=0;
      while(n<100){n++;
	double m=(lb+ub)/2.0;
	double room=0.0;
	for(int k=0;k<N;k++)if(double(J[k])<m)room+=(m-(double)J[k]);
	//	cout<<m<<' '<<room<<endl;
	if(room>(double)X)ub=m;else lb=m;
      }
      if(lb>J[i])res[i]=(double)(lb-J[i])/(double)X;//³ÎÇ§¡ª
    }
    
    string g="Case #";
    int L=t+1;
    if(L<10)g+=(char)(L+'0');else{g+=(char)(L/10+'0');g+=(char)(L%10+'0');}
    g+=":";
    cout<<g;
    for(int i=0;i<N;i++)printf(" %f",res[i]*100.0);
    cout<<endl;
  }
  return 0;
}
