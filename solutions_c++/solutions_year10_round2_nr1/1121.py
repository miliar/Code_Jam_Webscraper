#include<iostream>
#include<vector>
#include<queue>
#include<cmath>
#include<numeric>
#include<functional>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;

class file
{	
	vector<string> s1,s2,record;
	string s;
	int M,N;
	int a;
	public:
	file(){

	}
	void getdata(){
		cin>>N>>M;
		for(int i=0;i<N;i++){
			cin>>s;
			s1.push_back(s);
		}
		for(int i=0;i<M;i++){
			cin>>s;
			s2.push_back(s);
		}
    }
    bool mkdirno(string temp){
		int result=0;
		for(int j=0;j<record.size();j++){
			if(temp==record[j])
				return true;
		}
    return false;
	}
			
    int solve(){
a=0;
	string temp;
	int count=0;
	for(int i=0;i<s1.size();i++){
			s1[i]+='/';
			for(int j=1;j<s1[i].size();j++){		
				if(s1[i][j]=='/'){
					temp.assign(s1[i].begin(),s1[i].begin()+j);
					record.push_back(temp);
				}
			}
	}
	for(int i=0;i<s2.size();i++){
			s2[i]+='/';
			for(int j=1;j<s2[i].size();j++){
				if(s2[i][j]=='/'){
					temp.assign(s2[i].begin(),s2[i].begin()+j);
					if(!mkdirno(temp))
						a++;
					record.push_back(temp);
				}
			}
			
	}			
	//cout<<a;
	return a;
}
};
int main()
{
	int Testcases,i;
	cin>>Testcases;
	file *ob;
	ob=new file[Testcases+1];
	for(i=1;i<Testcases+1;i++)
	{
		ob[i].getdata();
	}
	for(i=1;i<=Testcases;i++)
	{
		cout<<"Case #"<<i<<": "<<ob[i].solve()<<endl;
	}
	return 0;
}
