#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<string>
#include<list>

using namespace std;
ifstream infile;
ofstream outfile;

bool same(int len, long int v, long int val){
	int valc=val;int len2=-1;
	while(valc>0){
		len2++;
		valc/=10;
	}	
	return (len2==len);
}

int check(long int v, long int a, long int b){
	//get the digits
	//cout<<"\n**v**"<<v<<' ';
	int digits[10],len=-1,count=0;
	int vc=v;
	while(vc>0){
		digits[++len]=vc%10L;
		vc/=10L;
	}
	//all the digits in reverse
	for(int st=0; st<len; st++){
		long int val=0L; 
		for(int i=st; i>=0; i--){val*=10L; val+=digits[i];}
		for(int i=len; i>st; i--){val*=10L; val+=digits[i];}
		if(!same(len,v,val))continue;
		//cout<<val<<' ';
		if((val>v)&&(val>=a)&&(val<=b)){count++;}
	}
	return count;
}

int main(){

infile.open("C-small-attempt0.in");
outfile.open("out.out");
int tc;
infile>>tc;

for(int tcc=1; tcc<=tc; tcc++){

long int a,b; int count=0;
infile>>a>>b;
for(int i=a; i<b; i++)count+=(check(i,a,b));

outfile<<"Case #"<<tcc<<": "<<count<<endl;
}

return 0;
}
