#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
using namespace std;
vector<string> slash(vector<string> v)
{
     vector<string> v1;
     string str;
     int c=1;
     int i, j, k;
     for(i=0;i<v.size();i++){
     	for(j=1;j<v[i].size();j++){
     		if( (v[i])[j]=='/' ){
     			for(k=0;k<v1.size();k++){
     				if(v[i].substr(0,j)==v1[k]){
     					c=0;
     					break;
     				}
     			}
     			if(c==1)
     				v1.push_back( v[i].substr(0,j) );
     		}
     		c=1;
        }
        c=1;
        for(k=0;k<v1.size();k++){
  				if(v[i]==v1[k]){
 					c=0;
 					break;
  				}
		}
		if(c==1)
        	v1.push_back(v[i]);
		c=1;
 	}
     return v1;                      
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Output.txt","w",stdout);
	vector<string> ve, vc;
	int N,M,T,z;
	int i,j;
	string str;
	cin>>T;
	for(z=1;z<=T;z++){
		cin>>N>>M;
		for(i=0;i<N;i++){
			cin>>str;
			ve.push_back(str);
		}
		for(i=0;i<M;i++){
			cin>>str;
			vc.push_back(str);
		}
		ve=slash(ve);
		vc=slash(vc);
		for(j=0;j<ve.size();j++){
			for(i=0;i<vc.size();i++){
					if(vc[i]==ve[j]){
						vc.erase(vc.begin()+i,vc.begin()+i+1);
						break;
					}
			}
		}
		cout<<"Case #"<<z<<": "<<vc.size()<<endl;
		ve.clear();
		vc.clear();
	}
	return 0;
}
