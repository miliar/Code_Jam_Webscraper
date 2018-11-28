
#include<iostream>
#include<vector>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<list>
#include<algorithm>

using namespace::std;

int main(){
  
  int T;
  
  cin>>T;
  
  for(int t=0;t<T;t++){
    int N;
    cin>>N;
    
    vector<char> c_bottun;
    vector<int> n_bottun;
	
    for(int n=0;n<N;n++){
      char temp1;
      int temp2;
      
      cin>>temp1;
      cin>>temp2;
      
      c_bottun.push_back(temp1);
      n_bottun.push_back(temp2);
    }
    
    int time=0;
    int p=0;
    int robo1=1;
    int robo2=1;
    while(p<c_bottun.size()){
      int robo1_next=-1;
      int robo2_next=-1;
      bool push=false;
      for(int i=p;i<c_bottun.size();i++){
	if(c_bottun[i]=='O'){
	  robo1_next=n_bottun[i];
	  break;
	}	  
      }
      for(int i=p;i<c_bottun.size();i++){
        if(c_bottun[i]=='B'){
          robo2_next=n_bottun[i];
          break;
        }
      }


      if(robo1_next!=-1){
	if(robo1==robo1_next){
	  if(c_bottun[p]=='O'){
	    push=true;
	  }
	}else{
	  if(robo1>robo1_next)
	    robo1--;
	  else
	    robo1++;
	}
      }

      if(robo2_next!=-1){
        if(robo2==robo2_next){
          if(c_bottun[p]=='B'){
            push=true;
          }
        }else{
          if(robo2>robo2_next)
            robo2--;
          else
            robo2++;
        }
      }




      
	if(push)
	  p++;
	time++;
    }
    
    cout<<"Case #"<<t+1<<": "<<time<<endl;
  }

  
  return 0;
  
}
