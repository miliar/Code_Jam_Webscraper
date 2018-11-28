#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
int main(){
	int M[31];
	int t,t1,n,s,p,marks,i,ans,j;
	char output[] = "output.txt";
	ofstream OutFile;
	OutFile.open(output);
	cin>>t;
	t1=t;
	while(t--){
		for(i=0;i<=31;i++)
		M[i]=0;
		cin>>n>>s>>p;
		ans=0;
		for(i=0;i<n;i++){
			cin>>marks;
			M[marks]++;
		}
		if(p==1)
		i=1;
		else if(p==0)
		i=0;
		else if(s==0)
		i=3*p-2;
		else{
			i=3*p-4;
			if(s>=M[i]){
				ans=ans+M[i];
				s=s-M[i];
			}
			else{
				ans=ans+s;
				s=0;
				}
			if(s==0)
				i=3*p-2;
			else{
				i++;
				if(s>=M[i]){
					ans=ans+M[i];
					s=s-M[i];
				}
				else{
					ans=ans+s;
					s=0;
				}
			i++;
			}
			}
		
		for(j=i;j<=30;j++)
			ans=ans+M[j];
		OutFile<<"Case #"<<t1-t<<": "<<ans<<endl;
	}
}

