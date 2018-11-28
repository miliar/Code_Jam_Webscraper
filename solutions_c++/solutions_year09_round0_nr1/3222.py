#include<iostream>
#include<vector>
using namespace std;
int main()
{
	long long int i,j,k,n,d,l,j1,cnt,cnt1,j2,fin;
	cin>>l>>d>>n;
	vector<string> vd,vin;
	string s;
	for(i=0;i<d;i++){
		cin>>s;
		vd.push_back(s);
	}
	for(i=0;i<n;i++){
		cin>>s;
		vin.push_back(s);
	}
	for(i=0;i<vin.size();i++){
		fin=0;
		for(j=0;j<vd.size();j++){
			j1=0;cnt1=0;
			for(k=0;k<vd[j].size();k++){
				cnt=0;
				if(vin[i][j1]=='('){
					for(j2=j1;vin[i][j2]!=')' && j2<vin[i].size();j2++){
						if(vd[j][k]==vin[i][j2])
							cnt++;
					}
					j1=j2+1;
				}else if(vin[i][j1]==vd[j][k]){
					j1++;
					cnt++;
				}
				if(cnt>0)
					cnt1++;
			}
			if(cnt1==k)
				fin++;	
		}
		cout<<"Case #"<<i+1<<": "<<fin<<endl;
	}	
	return 0;
}

