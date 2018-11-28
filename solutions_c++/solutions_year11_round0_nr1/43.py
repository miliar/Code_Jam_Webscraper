#include<iostream>
#include<vector>

using namespace std;

int main(){
  int T,N,t=1;
  cin>>T;
  while(T--){
    cin>>N;
    int time=0;
    vector<int> A;
    vector<int> B;
    char ch;
    int tmp;
    for (int i=0;i<N;i++){
      cin>>ch;
      cin>>tmp;
      if (ch=='O')
	A.push_back(tmp*1000+i);
      else
	B.push_back(tmp*1000+i);
    }
    vector<int>::iterator ia = A.begin();
    vector<int>::iterator ib = B.begin();
    int apos=1,bpos=1,next=0,moved=0;
    while(ia!=A.end() || ib!=B.end()){
      //      cout<<apos<<" "<<bpos<<endl;
      moved=0;
      time++;
      if (ia!=A.end()){
	if (apos==(*ia)/1000){
	  if (next==(*ia)%1000){
	    ia++;
	    next+=1;
	    moved=1;
	  }
	}
	else{
	  apos+=(*ia)/1000<apos?-1:1;
	}
      }
      if (ib!=B.end()){
	if (bpos==(*ib)/1000){
	  if (next==(*ib)%1000){
	    if (!moved){
	      ib++;
	      next+=1;
	    }
	  }
	}
	else{
	  bpos+=(*ib)/1000<bpos?-1:1;
	}
      }
    }
    cout<<"Case #"<<t++<<": "<<time<<endl;
  }
}
      

      
