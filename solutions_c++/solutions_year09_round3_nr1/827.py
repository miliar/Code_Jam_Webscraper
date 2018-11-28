#include<iostream>
#include<string>
#include<algorithm>
#include<map>
using namespace std;
long long power(int n , int a ){
	long long val=1;
	for(int i=0;i<n;i++)val=val*a;
	return val;
}
int main(){

	int test;
	cin>>test;
	for(int kk=1;kk<=test;kk++){
		string in;
		cin>>in;
		int aa[136];	
		memset(aa,-1,sizeof(aa));
		aa[in[0]]=1;int tt=0;
		while(in[tt]==in[0]&&tt!=in.size())tt++;
		aa[in[tt]]=0;
		

		int y=2;
		
		for(int i=tt+1;i<in.size();i++)
			if(aa[in[i]]==-1)aa[in[i]]=y++;
		long long ret =0; 
		for(int i=in.size()-1;i>=0;i--){
			ret+=power(in.size()-1-i,y)*aa[in[i]];
		}		
		cout<<"Case #"<<kk<<": "<<ret<<endl;
	}
	return 0;
}
