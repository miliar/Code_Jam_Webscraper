#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<vector>
#include<iomanip>
using namespace std;
#define f(i,n) for(int i=0;i<n;i++)
#define vi vector<int>
#define vii vector< vi >
int x=0;
string s1="welcome to code jam";
long long int cal(int i,string &s,int j,vii &v){
	//cout<<i<<"  "<<j<<endl;
	if(i==s.size())
		return 0;
	else if(v[i][j]!=-1)
		return v[i][j];
	else{
		if(j==18 && s[i]==s1[18]){
			x++;
			v[i][j]= 1+cal(i+1,s,j,v)+cal(i+1,s,0,v);
			
		}

		else if(s[i]==s1[j])
			v[i][j]= cal(i+1,s,j+1,v)+ cal(i+1,s,j,v);
		else
			v[i][j]= cal(i+1,s,j,v);
		return v[i][j];
	}
}
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int n;
	fin>>n;
	f(i,n){
		string s;
		if(i==0)
		getline(fin,s);
		getline(fin,s);
		//cout<<s<<endl;
		vii v(s.size(),vi(19,-1));
		//cout<<v[0][0];
		fout<<"Case #"<<i+1<<": "<<setw(4)<<setfill('0')<<cal(0,s,0,v)%10000<<endl;
		
	}

return 0;
}

