#include<iostream>
#include<fstream>

using namespace std;

char pp(char a,char b,char c,char d){
	if(a!='.'&&b!='.'&&c!='.'&&d!='.'){
		if(a==b&&b==c&&c==d){
			return a;
		}else if(a=='T'&&b==c&&c==d){
			return b;
		}else if(b=='T'&&a==c&&c==d){
			return a;
		}else if(c=='T'&&a==b&&b==d){
			return a;
		}else if(d=='T'&&a==b&&b==c){
			return a;
		}else{
			return 'F';
		}
	}else
		return 'F';
}

void main(){
	ifstream f1("D:\\codeJam\\A\\A-large.in");
	ofstream f2("D:\\codeJam\\A\\A-large.out");
	int T;
	f1>>T;
	for(int t=0;t<T;t++){
		char s[16],r;
		bool win;
		win=false;
		for(int i=0;i<16;i++)
			f1>>s[i];
		for(int i=0;i<13;i=i+4){
			r=pp(s[i],s[i+1],s[i+2],s[i+3]);
			if(r!='F'){
				win=true;
				break;
			}
		}
		if(win){
			f2<<"Case #"<<t+1<<": "<<r<<" won"<<endl;
		}else{
			for(int i=0;i<4;i++){
				r=pp(s[i],s[i+4],s[i+8],s[i+12]);
				if(r!='F'){
					win=true;
					break;
				}
			}
			if(win){
				f2<<"Case #"<<t+1<<": "<<r<<" won"<<endl;
			}else{
				r=pp(s[0],s[5],s[10],s[15]);
				if(r!='F')
					f2<<"Case #"<<t+1<<": "<<r<<" won"<<endl;
				else{
					r=pp(s[3],s[6],s[9],s[12]);
					if(r!='F')
						f2<<"Case #"<<t+1<<": "<<r<<" won"<<endl;
					else{
						bool comp=true;
						for(int co=0;co<16;co++){
							if(s[co]=='.'){
								comp=false;
								break;
							}
						}
						if(comp){
							f2<<"Case #"<<t+1<<": "<<"Draw"<<endl;
						}else{
							f2<<"Case #"<<t+1<<": "<<"Game has not completed"<<endl;
						}
					}
				}
			}
		}

	}
	f1.close();
	f2.close();
}
