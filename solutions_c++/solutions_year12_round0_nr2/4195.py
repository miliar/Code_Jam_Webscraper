#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("B-large.in");
	cout.open("outputBlarge.txt");
	int t,n,s,p,temp1,temp2,temp3,max;
	cin>>t;
	for(int i=0;i<t;i++){
		max=0;
		cin>>n>>s>>p;
		for(int j=0;j<n;j++){
			cin>>temp1;
			temp2=temp1/3;
			temp3=temp1%3;
			if(temp2>=p)max++;
			else if(temp2+1>=p){
				if(temp3>=1)max++;
				else if(s>0 && temp1>0) {s--;max++;}
			}
			else if(temp2+2>=p && s>0 && temp3>=2){ max++;s--;}
		}
		cout<<"Case #"<<i+1<<": "<<max<<endl;
	}
	return 0;
}
			
