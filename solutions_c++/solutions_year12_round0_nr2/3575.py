#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int T,N,S,p,t,r;
    ifstream myfile("input.txt");
    ofstream myOfile("output.in");
    if(myfile.is_open()&&myOfile.is_open()){
          myfile>>T;
          for(int i=0; i<T; i++){
                  myfile>>N>>S>>p;
                  r=0;
                  for(int j=0; j<N; j++){
                          myfile>>t;
                          if(t>1){
                                  if((t+2)/3>=p) r++;
                                         else if(S>0&&(t+4)/3>=p){r++; S--;}
                          }else{
                                if(t>=p) r++;
                                        }
                  }
                  myOfile<<"Case #"<<i+1<<": "<<r<<endl;
          }
          myfile.close();
          myOfile.close();
    }else{
          cout<<"Uneable to open files!";
    }
    return 0;
}
