#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
#include <sstream>
#include<map>
using namespace std;
 
string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}
 
int convertString(string S)
{
        stringstream ss;
        ss << S;
        int m;
        ss>>m;
        return m;
}
 
map < string,vector<string>  > Set;
int main()
{
        //ifstream fin ("in.txt");
        //ofstream fout ("out.txt");
        int n;
        cin>>n;
	for(int i=0;i<n;i++){
		cout<<"Case #"<<i+1<<": ";
		long a,b,c;
		long d[100000],e[100000]={0},f[100000];
		cin>>a;
		for(long j=0;j<a;j++){
		cin>>d[j]>>f[j];
		}
		cin>>d[a];
		f[a]=99999999L;
		e[0]=2*d[0]; 	
		for(long j=1;j<=a;j++){
			for(long k=0;k<j;k++){
			if(d[j]<=e[k]) {long x=d[j]-d[k]<f[j]?d[j]-d[k]:f[j];e[j]=d[j]+x;break;}
		}}
	if(e[a]!=0) cout<<"YES\n";
	else cout<<"NO\n";
	}
}  
