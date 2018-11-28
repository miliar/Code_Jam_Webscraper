#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
#define f(i,n) for(int i=0;i<n;i++)

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int l,d,n;
	
	fin>>l>>d>>n;
	cout<<l<<d<<n<<endl;
	vector<string>v(d);
	string s;
	f(i,d){
		fin>>v[i];
		//cout<<v[i]<<endl;
	}
	sort(v.begin(),v.end());
	f(i,n){
		fin>>s;
		//cout<<s<<endl;
		int a[l][26];
		f(m,l){
			f(n,26)
				a[m][n]=0;
		}
		int k=0,f=0;
		f(j,s.size()){
			if(s[j]=='(')
				f=1;
			else if(s[j]==')'){
				k++;
				f=0;
			}
			else if(f==0){
				a[k][s[j]-'a']=1;
			//	cout<<s[j]<<"  "<<a[k][s[j]-'a']<<endl;

				 k++;
			}
			else{
				a[k][s[j]-'a']=1;
			//	cout<<s[j]<<"  "<<a[k][s[j]-'a']<<endl;

			}
		//	cout<<s[j]<<"  "<<a[k][s[j]-'a']<<endl;
		}
		
		int c=0;
		f(j,v.size()){
			for(k=0;k<l;k++){
				if(a[k][v[j][k]-'a']==1)
					continue;
				else break;
			}
			if(k==l)
				c++;
		}
		fout<<"Case #"<<i+1<<": "<<c<<endl;
	}
	//string s;
	//fin>>s;
	//cout<<s;
	//fout<<s;
	//fout<<"dffdff";
	fin.close();
	fout.close();
	return 0;
}
		




		

