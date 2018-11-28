#include<iostream>
#include<stdlib.h>

using namespace std;

void task(){
	int N;

	int t,wt;
	int b_pos,o_pos;

	int x;
	char c1,c2;

	t=wt=0;
	b_pos=o_pos=1;
	c1=c2='\0';
	cin>>N;
	for(int i=0;i<N;i++){
		cin>>c1>>x;
		if(c1==c2){
			if(c1=='B'){
				t+=abs(b_pos-x)+1;
				wt+=abs(b_pos-x)+1;
				b_pos=x;
			}else if(c1=='O'){
				t+=abs(o_pos-x)+1;
				wt+=abs(o_pos-x)+1;
				o_pos=x;
			}
		}else{
			if(c1=='B'){
				if(abs(b_pos-x)+1-wt>0){
					t+=abs(b_pos-x)+1-wt;
					wt=abs(b_pos-x)+1-wt;
				}
				else{
					t+=1;
					wt=1;
				}
				b_pos=x;
			}else if(c1=='O'){
				if(abs(o_pos-x)+1-wt>0){
					t+=abs(o_pos-x)+1-wt;
					wt=abs(o_pos-x)+1-wt;
				}
				else{
					t+=1;
					wt=1;
				}
				o_pos=x;
			}

		}
		c2=c1;
	}
	cout<<t;
}

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		task();
		cout<<endl;
	}
	return 0;
}


