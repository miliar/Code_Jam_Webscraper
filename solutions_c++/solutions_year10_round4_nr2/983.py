#include <iostream>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>

using namespace std;

vector<string> MS(1024);
int M[1024];

int main(){
  char tmp[10240];

  int cases;
  cin.getline(tmp,1024);
  sscanf(tmp,"%d",&cases);

  int P;
  for(int i=1;i<=cases;++i)
  {
    cin.getline(tmp,1024);
    sscanf(tmp,"%d",&P);

    //cout<<P<<endl;

    cin.getline(tmp,10240);
    string s = tmp;
    boost::algorithm::split(MS,s,boost::is_any_of(" "));
   
    
    cin.getline(tmp,10240);
    //cout<<tmp<<endl;
    int cost;
    sscanf(tmp,"%d",&cost);
    for(int p=1;p<P;++p){
      cin.getline(tmp,10240);
    }

    for(int p=0;p<MS.size();++p){sscanf(MS[p].c_str(),"%d",M+p);}

    int sum = 0;
    for(int p=0;p<P;++p){
      int step = 1<<p;
      //cout<<(1<<P)<<endl;
      for(int q=0;q<1<<P;q+=2*step){
	//printf("(%d:%d,%d:%d)",q,M[q],q+step,M[q+step]);
	M[q] = min(M[q],M[q+step]);
	if(M[q]>0)M[q]--;
	else sum+=cost;
      }
    }

    //int mins = 100000000;
    //for(int p=0;p<MS.size();++p)mins = min(mins,M[p]);
    //cout<<cost<<" "<<mins<<endl;
    
    cout<<"Case #"<<i<<": "<<sum<<endl;
  }

  return 0;
}
