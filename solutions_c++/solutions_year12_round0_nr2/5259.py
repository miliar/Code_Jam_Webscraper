#include<iostream>
#include<cmath>
#include<math.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int nog,s,p,count=0,c2=0;
		cin>>nog>>s>>p;
		//cout<<"Sanket";
		for(int k=0;k<nog;k++){
			int score;
			cin>>score;
			int res=score-3*p;
			if(res>=0){
				count++;
				//cout<<score<<"0"<<endl;
			}
			else if(res == -1 && score>0){
				count++;
				//cout<<score<<"1 "<<endl;
			}
			else if(res == -2 && score>0){
				count++;
				//cout<<score<<"2 "<<endl;
			}
			else if(res == -3 && score>0 && c2<s){
				count++;
				c2++;
				//cout<<score<<"3 "<<endl;
			}
			else if(res == -4 && score>1 && c2<s){
				count++;
				c2++;
				//cout<<score<<"4 "<<endl;
			}
			/*int top=score/3;
			if(top == p-1 && top>0 && c2<=s){
				count++;
				c2++;
			}
			else if(top >= p){
				count++;
			}
			else if(top == p-2 && top>0 && c2<=s){
				count++;
				c2++;
			}*/
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
		count=0;
	}
	return 0;
}
