#include<iostream>
#include<conio.h>
#include<vector>
#include<map>
#include<algorithm>
#include<string>
#include<math.h>
#define max 1000

using namespace std;

int n;

int mult[max];
string in;
int first[max];
string already;

int find_index(char ch){
	int i,ret;
	int n=already.size();
	for(i=0;i<already.size();i++)
		if(already[i]==ch)
			break;
	if(i==already.size()){
		already+=ch;
		ret=mult[n];
		//first[ch]=n;
	}
	else
		ret=mult[i];
	return ret;
}



int main(void){

	
	freopen("b.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int cases,c;
	int i;
	mult[0]=1;
	mult[1]=0;
	for(i=2;i<max;i++)
		mult[i]=i;

	cin>>cases;

	for(c=0;c<cases;c++){
		int i,j;
		already.clear();

		cin>>in;
		for(i=0;i<in.size();i++){
			first[i]=find_index(in[i]);
			//cout<<first[i]<<endl;
		}

		int ans=0;
		int n=in.size();

		if(already.size()==1){
			ans=pow((double)2,n)-1;
		}else{

		for(i=0;i<in.size();i++)
			ans+=first[i]*pow((double)already.size(),n-i-1);
		}
		cout<<"Case #"<<c+1<<": ";
		cout<<ans<<endl;
	}
	getch();
	return 0;
}