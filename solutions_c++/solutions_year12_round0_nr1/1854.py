#include<iostream>
#include<fstream>
using namespace std;
int main(){
 char a[]={'y','h' ,'e','s', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z',  't', 'n', 'w', 'j', 'p', 'f', 'm', 'a','q'};
 int n,i,j,temp;
 
 string str;
 ifstream inf;
 inf.open("A-small-attempt1.in");
 ofstream outf;
 outf.open("out.txt");
 getline(inf,str);
 n=30;
 
for(i=0;i<n;i++)
 {
 	getline(inf,str);
 	
 	outf<<"Case #"<<i+1<<":"<<" ";
 	for(j=0;j<str.size();j++)
 		if(str[j]!=' ')
			str[j]=a[str[j]-'a'];
	outf<<str<<endl;
	

	}

inf.close();
outf.close();	

 return 0;
}