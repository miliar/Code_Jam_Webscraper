#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
//#include<sstream>
#define f(i,n) for(int i=0;i<n;i++)

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	//stringstream ss (stringstream::in | stringstream::out);
	int t,c=1;
	fin>>t;
	string s2="1342";
	next_permutation(s2.begin(),s2.end());
	//cout<<s2<<endl;
	while(t--){
		string s;
		fin>>s;
	//	cout<<s<<endl;
		int f=0,i=0;
		for( i=0;i<s.size()-1;i++)
			if(s[i+1]>s[i])
			break;
		if(i!=s.size()-1){
			next_permutation(s.begin(),s.end());
			fout<<"Case #"<<c<<": "<<s<<endl;
		}
		else{
			sort(s.begin(),s.end());
			string s1="";
			i=0;
			while(s[i]=='0' && i<s.size())
				i++;
			s1+=s[i];
			int j=i;
			s1+='0';
			i++;
			f(k,j)
				s1+='0';
			while(i<s.size()){
				s1+=s[i];
				i++;
			}
			
			fout<<"Case #"<<c<<": "<<s1<<endl;
		}
		c++;
	}



	fin.close();
	fout.close();
	return 0;
}
		




		

