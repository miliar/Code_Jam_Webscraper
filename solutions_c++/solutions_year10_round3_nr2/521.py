#include <iostream>


using namespace std;

int load_con[32];



int setup(int load){
  if(load_con[load]!=-1)return load_con[load]; 
  if(load <= 1)return 0;
  int numb = 1 + setup((load +1)/2);
  load_con[load] = numb; 
  return numb;
}

int main(){
  int tstcses;
  cin>>tstcses;

  for(int i=0; i<20; i++){
    load_con[i] =-1;
  }

  for(int tst=1; tst<=tstcses; tst++){
    int l,p,c;
    cin>>l>>p>>c;

    int num_loads =0;
    while(l<p){
      l*=c;
      num_loads++;
    }


    cout<<"Case #"<<tst<<": "<<setup(num_loads)<<endl;
  }


}
