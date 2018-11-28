#include<iostream>
#include <bitset>
#include<fstream>
#include<string>
#include <stdlib.h> 
 using namespace std;
  class binary{
 public:
	 string tobinary(int num){
		 int total=0;string y;
	 while(num > 0)
		{  
			total = num % 2;  
			num /= 2;  		 
			if(total==1)y="1"+y;
			else y="0"+y;
		}	
			return y; 
	 }
	 int todec(string bin){
	 int a=bitset<32>(bin).to_ulong();
	 return a;
	 }
int addtwobin(int n1,int n2){//addtwobin as small boy
string s1=tobinary(n1);
string s2=tobinary(n2);
//cout<<n1<<"S1"<<s1<<endl;
//cout<<n2<<"S2"<<s2<<endl;
		 if(s1.length()<s2.length()){
			 while(s1.length()<s2.length()){s1="0"+s1;}}//if
		 else {while(s1.length()>s2.length()){s2="0"+s2;}}//else
		 //cout<<s1<<endl;
		 //cout<<s2<<endl;
		 string re="";
		 for(int i=0;i<s1.length();i++){
			 if(s1[i]=='1'){
			 if(s2[i]=='1')re+="0";
				 else re+="1";
			 }
			 else if(s1[i]=='0'){
				 if(s2[i]=='1')re+="1";
				 else re+="0";}

		 }// end for
//for(int j=0;j<re.length();j++)cout<<re[j];
int n=todec(re);
return n;//cout<<"N"<<n<<endl;
	 
}
 
 };

 int main(){
	 binary bin;
ifstream in("x.in");
ofstream out("y.out");
while(!in.eof()){
int n;
in>>n;//cout<<"N"<<n<<endl;
 for(int i=0;i<n;i++){//loop testcases>>>>>>>>>>>>>>>>>>>>>>
int arraynum;
in>>arraynum;//cout<<"ARnum"<<arraynum<<endl;
bool equal=false;int value=0;
int* A=new int[arraynum];
for(int j=0;j<arraynum;j++){
in>>A[j];//cout<<"AR"<<A[j];
}//endfor
//cout<<endl;
int max=0;//bool equal=false;int value=0;
for(j=0;j<arraynum-1;j++){
	for(int k=0;k<arraynum-j;k++){// take num
		int first=0,second=0;int actualf=0,actuals=0;
		for(int l=k;l<=k+j ;l++){
			first=bin.addtwobin(first,A[l]);
			actualf+=A[l];
	//	cout<<"LLLLL>>>>"<<A[l];
		}// end for l
		//cout<<endl;cout<<k<<"  "<<l<<endl;
		for(int m=0;m<arraynum;m++){
			if(m<k||m>=l){
				second=bin.addtwobin(second,A[m]);
				actuals+=A[m];
			//cout<<"MMM>>>"<<A[m];
			}//if m,k
		}//end for m
		//cout<<endl;
if(first==second&&first!=0){//cout<<first<<endl;cout<<second<<endl;
	equal=true;
	if(actualf>actuals)value=actualf;
	else value=actuals;
	}//end fi first
if(value>max)max=value;
	}//end for k
	
}//end for j
if(equal){out<<"Case #"<<(i+1)<<": "<<max<<endl;
}
else {out<<"Case #"<<(i+1)<<": "<<"NO"<<endl;}
	 //cout<<i<<endl;
 }//end for i

}// end while
in.close();
out.close();


 /*binary bin;
int a=bin.addtwobin("1","101");
cout<<endl<<a<<endl;
//string h="";
//h+="1";
//cout<<h<<endl;

/*
 string s=b.tobinary(999);
 for(int i=0;i<s.length();i++){
 cout<<s[i];
 }*/




return 0;
 }
