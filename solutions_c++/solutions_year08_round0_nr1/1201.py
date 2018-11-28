#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>
using namespace std;
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("small");
	fout.open("result");
	int n;
	string stringTemp;
	getline(fin,stringTemp);
	istringstream is(stringTemp);
	is>>n;
	for(int i=1;i<=n;i++){
		vector<string> engine,query;
		int e,q;
		getline(fin,stringTemp);
		istringstream is1(stringTemp);
		is1>>e;
		cout<<e<<endl;
		for(int j=0;j<e;j++){
			string s;
			getline(fin,s);
			engine.push_back(s);
			cout<<s<<endl;
		}
		getline(fin,stringTemp);
		istringstream is2(stringTemp);
		is2>>q;
		cout<<q<<endl;
		for(int j=0;j<q;j++){
			string s;
			getline(fin,s);
			query.push_back(s);
			cout<<s<<endl;
		}
		int count=0,result=0,num=-1;
		int flag[100]={0};
		for(int j=0;j<q;j++){
			for(int k=0;k<e;k++){
				if(query[j]==engine[k]){
					if(flag[k]==0){
						flag[k]=1;
						count++;
						num=k;
					}
					break;
				}
			}
			if(count==e){
				result++;
				memset(flag,0,sizeof(flag));
				flag[num]=1;
				count=1;
			}
		}
		for(int i=0;i<e;i++)
			cout<<flag[i]<<' ';
		fout<<"Case #"<<i<<": "<<result<<endl;
	}
	system("pause");
}
