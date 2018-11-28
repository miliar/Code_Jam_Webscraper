#include<iostream>
#include<fstream>

using namespace std;

int main(){
  ofstream outfile;
  outfile.open("output.txt",ios::app);
  long T;
  cin>>T;
  for(long t=1;t<=T;++t){
    long N,K,div;
    cin>>N;
    cin>>K;
    if(K==0){
      outfile<<"Case #"<<t<<": OFF\n";
    } else {
      ++K;
      div=1<<N;
      //cout<<K<<endl;
      //cout<<div<<endl;
      //cout<<(K%div)<<endl;
      if(0==(K%div)){       
	outfile<<"Case #"<<t<<": ON\n";
      }else{
	outfile<<"Case #"<<t<<": OFF\n";
      } 
    }
  }
  outfile.close();
  return 0;
}
