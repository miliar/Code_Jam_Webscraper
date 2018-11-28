#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <map>

using namespace std;

//bool flag[1000000];
int bases[502];
map<int,bool> flag;

int basechange(int n, int b){
	
	int ans = 0;
	
	int pow = 1;
	
	while(n!=0){
		ans += pow*(n%b);
		pow = pow*10;
		n = n/b;
	}
	
	return ans;
}

int convert(int n, int b){
	
	int ans = 0;
	
	while(n!=0){
		ans += (n%10)*(n%10);
		n /= 10;
	}
	
	//cout<<"\t"<<ans<<endl;
	
	return basechange(ans,b);
}

bool happy(int n, int b){
	
	//cout<<n<<" "<<b<<endl;
	
	if(n==1)
	return true;
	
	//memset(flag,0,sizeof(flag));
	
	flag.clear();
	
	n = basechange(n,b);
	
	flag[n] = true;
	
	int con = convert(n,b);
	
	//cout<<" "<<con<<endl;
	
	while(con!=1 && flag.find(con)==flag.end()){
		//cout<<" "<<con<<endl;
		flag[con] = true;
		con = convert(con,b);
	}
	
	//cout<<con<<endl;
	
	if(con==1)
	return true;
	
	return false;
	
}
	

int main(){
	
	int t;
	
	int n,c;
	
	int nobase;
	
	cin>>t;
	
	for(int i=0; i<t; i++){
		
		/*
		char temp;
		cin>>bases[nobase];
		nobase++;
		
		while(temp = getchar() && temp!='\n'){
			cin>>bases[nobase];
			cout<<bases[nobase]<<endl;
			nobase++;
		}*/

		if(i==0){
			char temp = getchar();
		}

		string s;
		
		getline(cin,s,'\n');
		
		//cout<<s<<endl;

		stringstream stream;
		stream<<s;
		
		//cout<<stream.str()<<endl;
		
		nobase = 0;
		
		while(stream>>bases[nobase]){
			//cout<<bases[nobase]<<endl;
			nobase++;
		}
		
		//stream.close();
		
		
		bool flag1;
		
		for(int j=2; ; j++){
			
			flag1 = true;
			
			for(int k=0; k<nobase; k++){
				//cout<<"t "<<k<<" "<<bases[k]<<endl;
				//cout<<j<<" "<<bases[k]<<endl;
				if(!happy(j,bases[k])){
					flag1 = false;
					break;
				}
			}
			
			if(flag1==true){
				cout<<"Case #"<<i+1<<": "<<j<<endl;
				break;
			}
		}
		 
		
	}
	
	return 0;
}
				
		
		

