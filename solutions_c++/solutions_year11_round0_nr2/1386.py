
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
  
  for(int i=0;i<T;i++){
    
    int C;
    cin>>C;
    
    vector<char> combine1;
    vector<char> combine2;
    vector<char> combine_result;
    
    
    for(int j=0;j<C;j++){
      string temp;
      cin>>temp;

      combine1.push_back(temp[0]);
      combine2.push_back(temp[1]);
      combine_result.push_back(temp[2]);
      
      combine1.push_back(temp[1]);
      combine2.push_back(temp[0]);
      combine_result.push_back(temp[2]);
			 
    }

    /*cout<<"combine"<<endl;
    
    for(int j=0;j<combine1.size();j++){
      cout<<combine1[j]<<combine2[j]<<combine_result[j]<<endl;
      }*/

    int D;
    
    cin>>D;
    
    vector<char> opp1;
    vector<char> opp2;
    for(int j=0;j<D;j++){
      string temp;
      cin>>temp;
      
      opp1.push_back(temp[0]);
      opp2.push_back(temp[1]);

      opp1.push_back(temp[1]);
      opp2.push_back(temp[0]);
     }/*
    cout<<"remove"<<endl;
    for(int j=0;j<opp1.size();j++){
      cout<<opp1[j]<<opp2[j]<<endl;
      }*/

    
    list<char> element;
    int N;
    cin>>N;

    for(int k=0;k<N;k++){
      char temp;
      cin>>temp;

      
      bool inv=false;
      
      for(int j=0;j<combine1.size();j++){ 
	
	if(combine1[j]==temp){
	  //cout<<combine2[j]<<":"<<element.back()<<endl;
	  if(combine2[j]==element.back()){
	    element.pop_back();
	    element.push_back(combine_result[j]);
	    inv=true;
	    break;
	  }
	}
      }

      bool van=false;
      if(!inv){

	for(int j=0;j<opp1.size();j++){
	  if(opp1[j]==temp){
	    list<char>::iterator pos;
	    
	    pos=find(element.begin(),element.end(),opp2[j]);
	    
	    if(pos!=element.end()){
	      element.clear();
	      van=true;
	    }
	  }
	}

      }


      if(!inv && !van){
	element.push_back(temp);
      }


    }
    
    cout<<"Case #"<<i+1<<": [";
    bool dot=false;
    for(list<char>::iterator res=element.begin();
	res!=element.end();
	res++){
      
      if(dot)
	cout<<", ";
      cout<<*res;
      dot=true;
      
    }
    cout<<"]"<<endl;
  }
  
  
  return 0;
  
}
