#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<map>
#include<fstream>
#include<algorithm>
//#include<sstream>
#define f(i,n) for(int i=0;i<n;i++)
struct node{
	string s;
	float f;
	node *left,*root;
};

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	//stringstream ss (stringstream::in | stringstream::out);
	int t;
	int c=1;
	fin>>t;
	while(t--){
		map<char,int>m;
		string s;
		int a=2,f=0;
		fin>>s;
		cout<<s;
		m[s[0]]=1;
		for(int i=1;i<s.size();i++){
			if(m.find(s[i])==m.end()){
				if(f==0){
					m[s[i]]=0;
					f=1;
				}
				else{
				m[s[i]]=a;
				a++;
				}
			}
		}
		unsigned long long int x=0,b;
		if(m.size()==1)
			b=2;
		else
			b=m.size();
		unsigned long long int d=1;
		for(int i=s.size()-1;i>=0;i--){
			x+=(d*m[s[i]]);
			d*=b;
		}
		fout<<"Case #"<<c<<": "<<x<<endl;
		cout<<x<<endl;
		c++;
	}


	fin.close();
	fout.close();
	return 0;
}
		




		

