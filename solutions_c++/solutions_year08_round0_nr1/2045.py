#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<iostream>
#include<string>
#include<sstream>
#include<map>

using namespace std;

int solve(vector<string>vq,int start,int end,vector<string> vs);
int find(vector<string> vq,int start,int end,string s);

int main(){

  int testCases = 0;

  cin>>testCases;
  

  for(int iter=1;iter<=testCases;iter++){

    int s,q;
    string t;
    cin>>s;
    //cout<<s<<endl;
    vector<string> vs;
    for(int i=0;i<=s;i++){
      getline(cin,t);
      //cout<<t<<endl;
      if(i>0)
	vs.push_back(t);
    }

    cin>>q;

    vector<string> vq;
    for(int i=0;i<=q;i++){
      getline(cin,t);
      //cout<<t<<endl;
      if(i>0)
	vq.push_back(t);
    }



    cout<<"Case #"<<iter<<": ";

    
      cout<<solve(vq,0,vq.size()-1,vs);

    if(iter<testCases)
      cout<<endl;
    
   
  }


}

int solve(vector<string>vq,int start,int end,vector<string> vs){

  int maxpos=start;

  for(int i=0;i<vs.size();i++){
    int pos = find(vq,start,end,vs[i]);
    if(pos==-1)
      return 0;
    else if(pos > maxpos)
      maxpos=pos;

  }

  return 1+solve(vq,maxpos,end,vs);


}

int find(vector<string> vq,int start,int end,string s){
  for(int i=start;i<=end;i++)
    {
      if(vq[i]==s)
	return i;
    }
  return -1;

}
