#include <iostream>
#include <string>
#include <>
int L;

int _check(string a,string b){
	int goa=0,gob=0;
	int flag=1;
	int ig=0;
	int b_length=b.length();

	while(gob<b_length){
		if(goa==L)
			break;
					
		if(b[gob]=='('){
			flag=-1;
			gob++;
			ig=0;
			continue;
		}
		if(b[gob]==')'){
			if(ig==0)
				return 0;
			flag=1;
			ig=0;
			gob++;
			continue;
		}
		
		if(ig==1){
			gob++;
			continue;
		}
		
		if(b[gob]==a[goa]){
			goa++;
			if(goa==L)
				return 1;
			if(flag==-1)
				ig=1;
		}
		else {
			if(flag==1)
				return 0;
		}
		gob++;
	}
	return 1;	
}

int main(){
	
	int D,N,i;
	cin >> L >> D >> N;
	
	string words[D],to_words[N];
	for(i=0;i<D;i++)
		cin>>words[i];
		
	for(i=0;i<N;i++)
		cin >> to_words[i];
	for(i=0;i<N;i++){
		int count=0;
		for(int j=0;j<D;j++)
			if(_check(words[j],to_words[i])==1)
				count++;
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}