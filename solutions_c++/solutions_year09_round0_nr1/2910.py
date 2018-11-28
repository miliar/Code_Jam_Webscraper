#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
    
	int l,d,n;
	cin>>l>>d>>n;
	string s;
	vector<string>v(d),v1(n),v2;

	for(int i=0;i<d;i++){
		cin>>v[i];
	}

	for(int i=0;i<n;i++){
		cin>>v1[i];
	}

	int k,j,flag,p;
	int count;	
	string s1;
	for(int i=0;i<n;i++){
		j=0;
		while(j<v1[i].length()){
			if(v1[i][j]!='('){
				s1+=v1[i][j];
				v2.push_back(s1);
				//cout<<s1<<endl;
				s1="";
				j++;
			}else{
				j++;
				k=j;
				p=0;	
				while(v1[i][j+p]!=')'){
					p++;
				}
				v2.push_back(v1[i].substr(k,p));
				//cout<<v1[i].substr(k,p)<<endl;
				j+=p+1;
			}
			//cout<<j<<endl;
		}
		//cout<<v2.size()<<endl;
		count=0;
		for(j=0;j<d;j++){
			flag=0;
			for(k=0;k<l;k++){
				if(v2[k].find(v[j][k])==-1){
					flag=1;
					break;
				}
			}
			if(flag==0){
				count++;
			}
		}		
		cout<<"Case #"<<i+1<<": "<<count<<endl;
		v2.clear();		
	}
	
	return 0;
}
