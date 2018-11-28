#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
using namespace std;

int i,j;

int main()
{
	int t,n,s,p,a,x,ans;
	char input[] = "B-large.in";
	char output[] = "out.txt";
	ifstream InFile; 
	ofstream OutFile;
	InFile.open(input);
	OutFile.open(output);
	InFile>>t;
	for(j=0;j<t;j++){
		ans=0;
		InFile>>n>>s>>p;
		for(i=0;i<n;i++){
			InFile>>x;
			a=x/3;
			if(x==0){ if(p==0) ans=ans+1; } 
			else if(x%3==0){ 
				if(a==p-1){ if(s!=0){ s = s-1; ans=ans+1;}}
				else if(a>=p) ans= ans+1;
			}
			else if(x%3==1){ 
				if(a>=p-1) ans=ans+1; 
			}
			else if(x%3==2){
				if(a==p-2){ if(s!=0){ s = s-1; ans=ans+1;}}
				else if(a>=p-1) ans=ans+1;
			}
		}
		OutFile<<"Case #"<<j+1<<": "<<ans<<endl;
	}

	InFile.close();
	OutFile.close();

	return 0;
}
