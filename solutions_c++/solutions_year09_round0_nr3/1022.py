#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
using namespace std;

int arr1[510];
int arr2[510];
int N;
int size;
string welcome = "welcome to code jam";
string input;



void solve(){
	
	size = input.length();
	
	char c = welcome[0];
	
	for(int i=0; i<size; i++){
		if(input[i]==c)
			arr1[i] = 1;
		else
			arr1[i] = 0;
	}
	
	for(int i=1; i<size; i++){
		arr1[i] += arr1[i-1];
	}
	
	for(int i=1; i<19; i++){
		c = welcome[i];
		
		arr2[0] = 0;
		
		for(int j=1; j<size; j++){
			if(input[j]==c){
				arr2[j] = arr1[j-1];
			}
			else{
				arr2[j] = 0;
			}
		}
		
		arr1[0] = 0;
		
		for(int j=1; j<size; j++){
			arr1[j] = (arr2[j]+arr1[j-1])%10000;
		}
	}
	
	arr1[size-1] = arr1[size-1]%10000;
	
	printf("%04d\n",arr1[size-1]);
		
	return;
}

int main(){
	
	cin>>N;
	//cout<<N<<endl;
	char c = getchar();
	for(int i=0; i<N; i++){
		
		getline(cin,input,'\n');
		//cout<<input<<endl;
		cout<<"Case #"<<i+1<<": "; 
		solve();
	}
	
	return 0;
}
