#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;
#define limit 4
int main(){
	int t,ctr=0,k,l,x,o,flag=0,tie=0;
	string in[limit];
	cin>>t;
	while(ctr++<t){
		flag=0;
		tie=0;
		for(k=0;k<limit;k++){cin>>in[k];}
		for(k=0;k<limit;k++){
			x=0;o=0;
			for(l=0;l<limit;l++){
				if(in[k][l]=='X')x++;
				else if(in[k][l]=='O')o++;
				else if(in[k][l]=='.'){tie=1;break;}
				else if(in[k][l]=='T'){o++;x++;}
			}
			if(x>3){flag=-1;break;}
			if(o>3){flag=1;break;}
		}
		if(flag==0){
			for(k=0;k<limit;k++){
				x=0;o=0;
				for(l=0;l<limit;l++){
					if(in[l][k]=='X')x++;
					else if(in[l][k]=='O')o++;
					else if(in[l][k]=='.'){tie=1;break;}
					else if(in[l][k]=='T'){o++;x++;}
				}
				if(x>3){flag=-1;break;}
				if(o>3){flag=1;break;}
			}
			if(flag==0){
				x=0;o=0;
				for(l=limit-1,k=0;l>=0;l--,k++){
					if(in[l][k]=='X')x++;
					else if(in[l][k]=='O')o++;
					else if(in[l][k]=='.'){tie=1;break;}
					else if(in[l][k]=='T'){o++;x++;}
				}
				if(x>3){flag=-1;}
				if(o>3){flag=1;}	
				if(flag==0){
					x=0;o=0;
					for(l=0,k=0;l<limit;l++,k++){
						if(in[l][k]=='X')x++;
						else if(in[l][k]=='O')o++;
						else if(in[l][k]=='.'){tie=1;break;}
						else if(in[l][k]=='T'){o++;x++;}
					}
					if(x>3){flag=-1;}
					if(o>3){flag=1;}
					
				}
			}
		}
		cout<<"Case #"<<ctr<<": ";
		if(flag==-1)cout<<"X won\n";
		else if(flag==1)cout<<"O won\n";
		else if(tie==1)cout<<"Game has not completed\n";
		else cout<<"Draw\n";	
	}
	return 0;
}
