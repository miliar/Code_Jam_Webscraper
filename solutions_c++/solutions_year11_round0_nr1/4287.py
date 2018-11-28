#include<iostream>
using namespace std;

int main(){
	int t,kase=1;
	cin>>t;
	while(t--){
		int n,seq=0,count=0;
		cin>>n;
		char sequence[n];
		int position[n];
		int i=0,j=0,k=n;
		while(k--){
			cin>>sequence[i]>>position[i];
			i++;
		}
		
		int current_o=1,current_b=1,o_counter=0,b_counter=0,inc;
		char prev='\0';
		for(i=0;i<n;i++){
			if(sequence[i]=='O')
			{
				inc=(position[i]-current_o)>0?(position[i]-current_o):(current_o-position[i]);
				//cout<<"INC:"<<inc<<endl;
				if(prev=='O'){
					o_counter+=inc;
					o_counter+=1;
				}else if(prev=='B'){
					inc=inc-b_counter;
					if(inc<0)
						inc=0;
					b_counter=0;
					o_counter=inc+1;
					prev='O';
				}else if(prev=='\0'){
					o_counter=inc+1;
					prev='O';
				}
				count+=inc;
				count++;
				current_o=position[i];
			}else if(sequence[i]=='B')
			{
				inc=(position[i]-current_b)>0?(position[i]-current_b):(current_b-position[i]);
			//	cout<<"INC:"<<inc<<endl;
				if(prev=='B'){
					b_counter+=inc;
					b_counter+=1;
				}else if(prev=='O'){
					inc=inc-o_counter;
					if(inc<0)
						inc=0;
					o_counter=0;
					b_counter=inc+1;
					prev='B';
				}else if(prev=='\0'){
					b_counter=inc+1;
					prev='B';
				}
				count+=inc;
				count++;
				current_b=position[i];
			}
			//cout<<sequence[i]<<" "<<position[i]<<" "<<count<<endl;
		}
		cout<<"Case #"<<kase++<<": "<<count<<endl;
		
	}
	return 0;
}
