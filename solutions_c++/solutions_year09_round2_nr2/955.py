#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

string num;

int main(){
  
  int t;
  scanf("%d",&t);
  for(int tt=0;tt<t;tt++){
    cin>>num;
    int L=num.size();
    bool flag=false;
    for(int i=L-1;i>=0 and !flag;i--){
      int ans=-1;
      for(int j=i+1;j<L;j++){
	if(num[j]>num[i] and (num[j]<num[ans] or ans==-1)){
	  ans=j;
	  flag=true;
	}
      }
      if(flag){
	char temp;
	temp=num[i];
	num[i]=num[ans];
	num[ans]=temp;
	sort(num.begin()+i+1,num.end());
      }
    }
    if(flag){
      cout<<"Case #"<<tt+1<<": "<<num<<endl;
    }
    else {
      //cout<<num<<endl;
      vector<int> C(10,0);
      for(int i=0;i<L;i++)C[num[i]-'0']++;
      int ind=1;
      while(!C[ind])ind++;
    
      cout<<"Case #"<<tt+1<<": "<<ind;
      cout<<0;
      C[ind]--;
      ind=0;
      while(ind<10){
	while(C[ind]){
	  cout<<ind;
	  C[ind]--;
	}
	ind++;
      }
      cout<<endl;
    }
    
  }

}
