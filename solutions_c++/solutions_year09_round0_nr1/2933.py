#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main(){
	int i,j,k,l,d,n,f,b,c;
	vector<string> v,u;
	string s,w,z;
	cin>>l>>d>>n;
	int r[n];
	for(i=0;i<d;i++){
		cin>>s;
		v.push_back(s);
	}
	for(i=0;i<n;i++){
		r[i]=0;
		cin>>s;
		u.push_back(s);
	}
	for(i=0;i<d;i++){
		w=v[i];
		for(j=0;j<n;j++){
			z=u[j];
			f=0;b=0;
			for(k=0;k<l;k++){
				c=b;
				if(w[k]==z[f]){
					b++;
				}
				else if(z[f]=='('){
					while(z[f]!=')'){
						if(z[f]==w[k])
							b++;
						f++;
					}
				}
				if(c==b)
					break;
				f++;
			}	
			if(b==l)
				r[j]++;		
		}
	}
	for(i=0;i<n;i++)
		cout<<"Case #"<<i+1<<": "<<r[i]<<endl;
	return 0;
}	
