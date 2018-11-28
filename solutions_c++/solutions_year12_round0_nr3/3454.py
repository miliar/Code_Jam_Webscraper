#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
using namespace std;

int i,j,k;

int main()
{
	int t,a,b,l,x,y,ans;
	char input[] = "C-small-attempt0.in";
	char output[] = "out.txt";
	ifstream InFile; 
	ofstream OutFile;
	InFile.open(input);
	OutFile.open(output);
	int *s;
	s = new int[1001];

	for(i=1;i<10;i++) s[i]=i;
	l=2;k=10;
	for(i=10;i<1000;i++){
		if(s[i]==0){
			s[i]=k;
			if(i==100) l=3;
			if(i%10==0){
				if(l==2);
				else if(l==3){
					if(i%100!=0) s[10*(i%100) + i/100]=k;
				} 
			}
			else{
				x=i%10;
				if(l==2){ s[10*x + i/10] = k;}
				else if(l==3){ 
					y = 100*x + i/10;
					s[y]=k;
					if(y%10!=0) s[100*(y%10) + y/10]=k; 
				}
			}
			k=k+1;
		}
	}
	int *c;
	c = new int[1001];
		
	InFile>>t;
	for(j=0;j<t;j++){
		ans=0;
		InFile>>a>>b;
		for(i=a;i<=b;i++) c[s[i]]=c[s[i]]+1;
		for(i=1;i<1000;i++){
			if(c[i]!=0){
				ans = ans+ (c[i]*(c[i]-1))/2;
			}
		}
		OutFile<<"Case #"<<j+1<<": "<<ans<<endl;
		for(i=1;i<1000;i++) c[i]=0;
	}
	
	InFile.close();
	OutFile.close();
	return 0;
}
