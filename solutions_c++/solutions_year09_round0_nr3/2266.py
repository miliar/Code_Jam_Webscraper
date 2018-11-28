#include<iostream>
#include<string>
#include<sstream>

using namespace std;

string input;
int n;
string first;

int mem[1000][20];

int func(int a,int b){

	
	int &ret=mem[a][b];
	if(ret!=-1)
		return ret;


	if(a<b || a<0 )
		return ret=0;

	int i;
	if(b==0){

		int count=0;
		for( i=0;i<=a;i++){
			if(input[i]==first[b])
				count++;
		}
			return ret=count;
	}
	if(input[a]!=first[b]){
		ret=func(a-1,b)%10000;
		return ret;
	}
	int temp1,temp2;
	temp1=func(a-1,b-1)%10000;
	temp2=func(a-1,b)%10000;
	

	temp1=(temp1+temp2)%10000;
	ret=temp1;

	return ret;
}

int main(void){


	//freopen("a.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	first="welcome to code jam";
	int c,cases;
	cin>>cases;

	string st;
	getline(cin,st);


	for(c=0;c<cases;c++){

		memset(mem,-1,sizeof(mem));
		string str;

		
		input.clear();
		getline(cin,input);
		int i;
		
		n=input.size();
		int ans=func(n-1,18);
		string st;

		if(ans<1000)
			st+="0";
		if(ans<100)
			st+="0";
		if(ans<10)
			st+="0";
		cout<<"Case #"<<c+1<<": ";
		cout<<st<<ans<<endl;


	}

	
	return 0;
}


