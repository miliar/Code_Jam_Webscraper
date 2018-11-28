#include<iostream>
#include<vector>
#include<queue>
using namespace std;

class wire{
public:
  int A,B;
  int number;
  wire(int a,int b,int n){
    A=a;
    B=b;
    number=n;
  }
  bool operator<(const wire &obj)const{
    return A<obj.A;
  }
};

class wireB{
public:
  int A,B;
  int number;
  wireB(int a,int b,int n){
    A=a;
    B=b;
    number=n;
  }
  bool operator<(const wireB &obj)const{
    return A>obj.A;
  }
};

int main(){
  int round=1;
  int T;
  cin>>T;
  while(T--){
    int N;
    cin>>N;
    priority_queue<wire> WA;
    priority_queue<wireB> WB;
    
    for(int i=0;i<N;i++){
      int A,B;
      cin>>A>>B;
      WA.push(wire(A,B,i));
      WB.push(wireB(B,A,i));
    }
    vector<int> AO,BO;

    while(!WA.empty()){
      AO.push_back((WA.top()).number);
      BO.push_back((WB.top()).number);
      WA.pop();
      WB.pop();
    }
    int ans=0;
    vector<int>::iterator itri,itrj;
    
    for(itri=AO.begin();itri!=AO.end();itri++){
      int wn=(*itri);
      int ni=0;
      for(itrj=BO.begin();itrj!=BO.end();itrj++){
	if(wn==(*itrj)){
	  BO.erase(itrj);
	  break;
	}
	ni++;
      }
      ans+=BO.size()-ni;
      
    }
    cout<<"Case #"<<round<<": "<<ans<<endl;
    round++;
  }
  
  return 0;
}
