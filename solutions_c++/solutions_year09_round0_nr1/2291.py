#include<iostream>
#include<regex.h>
using namespace std;

string arr[10000];

int main(){
   int L,D,N;
   scanf("%d%d%d",&L,&D,&N);
   for(int i=0;i<D;i++) cin>>arr[i];
   for(int i=0;i<N;i++)
   {
      //cerr<<"test case: "<<i<<endl;
      string test; cin>>test;
      for(int j=0;j<test.size();j++)
         if(test[j]=='(') test[j]='[';
         else if(test[j]==')') test[j]=']';
         
      int ans=0;
    	regex_t    re;
     	regcomp(&re, test.c_str(), REG_EXTENDED|REG_NOSUB);
      for(int j=0;j<D;j++)
      {
		    int status = regexec(&re, arr[j].c_str(), (size_t) 0, NULL, 0);
	       ans+= (status==0)?1:0;
       }
     	 regfree(&re);
      cout<<"Case #"<<i+1<<": "<<ans<<endl;
   }
}
