#include<iostream>
#include<algorithm>
#include<fstream>
#include<sstream>
using namespace std;
main(){
	long long int i,j,t,k,n,m,cnt,flag;
	cin>>t;
	//stringstream ss;
	string str,str1;
	for(i=1;i<=t;i++){
		//cin>>n;
		//ss.clear();
		//ss<<n;
		cin>>str;
		flag=0;
		//str1=str;
		//sort(str.begin(),str.end());
		while(next_permutation(str.begin(),str.end())){
			cout<<"Case #"<<i<<":"<<" "<<str<<endl;
			flag=1;
			break;
		}
		if(flag!=1){
			sort(str.begin(),str.end());
			int ind=str.find_first_not_of('0');
			//cout<<ind<<endl;
			str1=str[0+ind];
			str1+='0';
			for(j=1;j<=ind;j++){
				str1+='0';
			}
			str1+=str.substr(1+ind);
			cout<<"Case #"<<i<<":"<<" "<<str1<<endl;
		}
	}
}
