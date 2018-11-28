#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <algorithm>


using namespace std;

int check(int A,int B,int t){
  if(A==B)return t;

  //cout<<"check:"<<A<<","<<B<<"t="<<t<<endl;

  int v1 = min(A,B);
  int v2 = max(A,B);

  int t2 = v2;
  while(v2-v1>v1)v2-=v1;
  int i = 0;
  if(t2==v2)++i;

  if(!t){
    while(v2-i*v1 > 0){
      if(v1==v2-i*v1)return 1;
      if(check(v1,v2-i*v1,t^1))return 1;
      ++i;
    }
    //cout<<"z";
    return 0;
  }
  else
  {
    while(v2-i*v1 > 0){
      if(v1==v2-i*v1)return 0;
      if(!check(v1,v2-i*v1,t^1))return 0;
      ++i;
    }
    //cout<<"o";
    return 1;
  }
}

int main(){
	int len;
	char tmp[256];

	//cout<<"res="<<check(2,3,0)<<endl;
	//return 0;

	cin.getline(tmp,256);
	sscanf(tmp,"%d",&len);
	for(int i=0;i<len;++i)
	{
	  int A1,A2,B1,B2;
	  cin.getline(tmp,256);
	  sscanf(tmp,"%d %d %d %d",&A1,&A2,&B1,&B2);

	  int count = 0;
	  for(int a=A1;a<=A2;++a){
	    for(int b=B1;b<=B2;++b){
	      if(check(a,b,0))
	      {
		//cout<<a<<":"<<b<<endl;
		count++;
	      }
	    }
	  }

	  cout<<"Case #"<<(i+1)<<": "<<count<<endl;
	}

	return 0;

}
