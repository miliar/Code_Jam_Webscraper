#include<string>
#include<iostream>
#include<stdio.h>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		int result[20];
		for(int j=0;j<20;j++){
			result[j]=0;
		}
		string input; 
		bool complete=false;
		for(int j=0;j<4;j++){
			cin>>input;//cout<<endl;
			for(int k=0;k<4;k++){
				//cout<<input[k];
				switch((char)input[k]){
					case 'X':
						result[k]++;
						result[4+j]++;
						if(j==k)
							result[8]++;
						if(j+k==3)
							result[9]++;
						break;
					case 'O':
						result[10+k]++;
						result[14+j]++;
						if(j==k)
							result[18]++;
						if(j+k==3)
							result[19]++;
						break;
					case 'T':
						result[k]++;
						result[10+k]++;
						result[4+j]++;
						result[14+j]++;
						if(j==k){
							result[18]++;
							result[8]++;
						}
						if(j+k==3){
							result[19]++;
							result[9]++;
						}
						break;
					case '.':
						complete=true;//cout<<"Oui"<<endl;	
						break;
					default: {}
				}
			}
		}
		cout<<"Case #"<<i+1<<":";
		bool won=false;
		for(int j=0;j<20;j++){
			//cout<< "Result "<<j<< " " << result[j]<<endl;
			if(result[j]==4){
				won=true;
				if (j>9)
					cout<<" O won";
				else 
					cout<<" X won";
				break;
			}
		}
		if(won==false){
			if(complete==false)
				cout<<" Draw";
			else
				cout<<" Game has not completed";
		}
		cout<<endl;
		getchar();
	}
	return 0;
}
