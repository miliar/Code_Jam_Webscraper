#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int j,g,out,m,l,d,n,i,k,t,h;
	cin>>l>>d>>n;
	string a[d];
	string s;
	for(i=0;i<d;i++)
		cin>>a[i];
	for(t=0;t<n;t++){
		cin>>s;
		if(s.find_first_of("(")==-1){
			k=0;
			for(i=0;i<d;i++){	
				if(a[i]==s)
					k++;
			}
			cout<<"Case #"<<t+1<<": "<<k<<endl;
		}
		else{
			h=s.size();
			out=0;
			for(i=0;i<d;i++){
				j=0;m=0;k=0;
				while(j<h){
					g=0;
					if(s[j]=='('){
						j++;
						while(s[j]!=')'){
							if(a[i][k]==s[j]){
								g=1;
								k++;
								while(s[j]!=')')
									j++;
								break;	
							}
							j++;
						}
						j++;
						if(g==0){
							m=1;
							break;
						}
					}
					else{
						if(s[j]==a[i][k]){
							k++;
							j++;
						}
						else{
							m=1;
							break;
						}
					}
				}
				if(m==0)
					out++;
			}
			cout<<"Case #"<<t+1<<": "<<out<<endl;
		}			
	}
	return 0;
}		
