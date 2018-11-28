#include<iostream>
#include<map>
using namespace std;
main(){
	map<char,long long int> m;
	long long int i,j,k,n,t;
	cin>>t;string str;
	for(k=1;k<=t;k++){
		cin>>str;
		string seq;
		m[str[0]]=1;
		seq+='1';
		for(i=1;i<str.size();i++){
			if(str[i]!=str[0]){
				m[str[i]]=-1;
				seq+='0';
				break;
			}else{
				seq+='1';
			}
		}
		j=i;
		long long int num=2;	
		for(i=j+1;i<str.size();i++){
			if(m[str[i]]==0){
				m[str[i]]=num;
				seq+=char(num+48);
				num++;
			}else{
				if(m[str[i]]==-1)
					seq+='0';
				else seq+=char(m[str[i]]+48);
			}
		}
	//	cout<<num<<endl<<seq<<endl;
		long long int x=1,sum=0;
		for(i=seq.size()-1;i>=0;i--){
			sum+=int(seq[i]-48)*x;
			x=x*num;
		}
		cout<<"Case #"<<k<<":"<<" "<<sum<<endl;
		m.clear();

	}
}
