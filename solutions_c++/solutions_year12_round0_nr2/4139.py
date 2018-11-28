#include<iostream>
#include<sstream>
#include<string>
#include<fstream>
using namespace std;
int solve(string s);
int main(){
	char buf[1000];
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int numCases;
	int i=1;
	if(in.getline(buf,1000))
		sscanf(buf,"%d",&numCases);
	while(in.getline(buf,1000)){
		//		cout<<"Enters\n";
		string s(buf);

		cout<<s;
		out<<"Case #"<<i<<": "<<solve(s)<<endl;
		i++;
	}

	in.close();
	out.close();
	return 0;
}

int solve(string s){
	istringstream strm(s);
	int ans=0;
	int N,S,p,val;
	strm>>N;
	strm>>S;
	strm>>p;
	while(N>0){
		strm>>val;
		N--;
		if((val==0)||(val==1)){
			if(val>=p){
				ans++;
				continue;
			}
			else{
				continue;
			}
		}
		int temp=val/3;
		if((val%3)!=0)
			temp++;
		if(temp>=p){
			ans++;
			continue;
		}
		if((val%3)!=1){
			if((temp+1)==p){
				if(S>0){
					S--;
					ans++;
				}
			}
		}
	}
	return ans;
}
