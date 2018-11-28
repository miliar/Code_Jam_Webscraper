#include<iostream>
#include<string>
#include<sstream>
#include<list>
#include"math.h"
using namespace std;

int recycle(int a, int A, int B){
	int i=0,count=0;
	int b=a;
	while(b!=0){
		b/=10;
		count++;
	}
	list<int> ll;
	int current=a;
	int temp;
	int power=(pow(10, count-1));
	for(i=0;i<count-1;i++){
		int flag=0;
		temp=(10*(current%power)) + (current/power);
		list<int>::iterator itr;
		itr = ll.begin();
		while(itr != ll.end()){
			if (temp==(*itr)) flag=1;
			itr++;
		}
		
		if(temp>=A && temp<=B && temp != a && flag == 0){
			ll.push_back(temp);
			}
		current=temp;
		flag=0;
	}
	
	return ll.size();
}
	

int myfunc(int a, int b){
	int sum=0;
	for(int i=a; i<b+1; i++){
		sum+=recycle(i,a,b);
	}
	return (sum/2);
}
	

int main(){
	int n,i=0,j;
	cin>>n;
	string str[n];
	getline (cin, str[i]);
	string sub;
	int values[n][2];
	
	
	for(i=0;i<n;i++){
		cin>>values[i][0]>>values[i][1];		
	}

	
	

	for(i=0;i<n;i++){
		cout<<"Case #"<<(i+1)<<": "<<myfunc(values[i][0], values[i][1])<<endl;
	}
	
	return 0;
}
