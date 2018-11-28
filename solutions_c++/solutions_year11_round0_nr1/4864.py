#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<map>
#include<deque>

using namespace std;

deque<int>blue;
deque<int>oran;
deque<char>iden;

void move(int &pos_b,int &pos_fb,int &pos_o,int &pos_fo)
{
	if(pos_b>pos_fb)
		--pos_b;
	else if(pos_b<pos_fb)	
		++pos_b;
		
		
	if(pos_o>pos_fo)
		--pos_o;
	else if(pos_o<pos_fo)
		++pos_o;						
}

int main()
{
	int t;	
	int which=1;	
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d\n",&n);
		for(int i=1;i<=n;++i){
			char col;
			int num;
			scanf("%c %d ",&col,&num);
			if(col=='B'){
				blue.push_back(num);	
			}	
			else
				oran.push_back(num);
			iden.push_back(col);
												
		}
	
	
		/*for(int i=0;i<blue.size();++i)
			cerr<<blue[i]<<" ";
		cerr<<" BLUE\n";
		for(int i=0;i<oran.size();++i)
			cerr<<oran[i]<<" ";
		cerr<<" ORAN\n";
		for(int i=0;i<iden.size();++i)
			cerr<<iden[i]<<" ";
		cerr<<" IDEN\n";
		cerr<<"\n";*/
								
		int count=0;
		int pos_b=1,pos_o=1,pos_fb=1,pos_fo=1;
		char col;			
		while(!iden.empty()){
			col=iden.front();	
		//cerr<<col<<"-col\n";	
			iden.pop_front();	
			if(col=='B'){
		//cerr<<pos_b<<"-pos_b\n";		
		//cerr<<pos_fb<<"-from pos_fb\n";	
				pos_fb=blue.front();
		//cerr<<pos_fb<<"-to pos_fb\n";
			
				blue.pop_front();
				pos_fo=oran.empty()? pos_o : 
oran.front();	
		//cerr<<pos_b<<"  "<<pos_fb<<"  fds sfsffsd\n";			
				while(pos_b!=pos_fb){
					move(pos_b,pos_fb,pos_o,pos_fo);	
					++count;
		/*cerr<<"/------------"<<count<<"--------------/\n";	
		cerr<<pos_o<<"-pos_o\n";
		cerr<<pos_b<<"-pos_b\n";
		cerr<<"/------------------------------------/\n";*/				
				}
				move(pos_b,pos_fb,pos_o,pos_fo);	
				++count;	
		/*cerr<<"/------------"<<count<<"--------------/\n";	
		cerr<<pos_o<<"-pos_o\n";
		cerr<<pos_b<<"-pos_b\n";
		cerr<<"/------------------------------------/\n";*/		
			}
			else{
		//cerr<<pos_o<<"-pos_o\n";		
		//cerr<<pos_fo<<"-from pos_fo\n";	
				pos_fo=oran.front();
		//cerr<<pos_fo<<"-to pos_fo\n";	
			
				oran.pop_front();
				pos_fb=blue.empty()? pos_b : 
blue.front();			
				while(pos_o!=pos_fo){
					move(pos_b,pos_fb,pos_o,pos_fo);	
					++count;
		/*cerr<<"/------------"<<count<<"--------------/\n";	
		cerr<<pos_o<<"-pos_o\n";
		cerr<<pos_b<<"-pos_b\n";
		cerr<<"/------------------------------------/\n";*/	
				}
				move(pos_b,pos_fb,pos_o,pos_fo);	
				++count;
		/*cerr<<"/------------"<<count<<"--------------/\n";	
		cerr<<pos_o<<"-pos_o\n";
		cerr<<pos_b<<"-pos_b\n";
		cerr<<"/------------------------------------/\n";*/				
			}
		//cerr<<"\n";						
										
		}
		printf("Case #%d: %d\n",which,count);
		++which;		
	//break;						
	}			
	return 0;
}	

