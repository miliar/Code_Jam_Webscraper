//#include<stdio>
#include<iostream>
using namespace std;


class bot{
public:
	int pos;
	int time;
	int movement;
public:	
	bot(){
		pos=1;
		time=0;
	}
	void move(int);
};

void bot::move(int position){
	movement=(position>pos)?(position-pos):(pos-position);
}

int botmove();

int main(){
	int T;		//Total number of test cases
//	cout<<"Enter total number of test cases\t";
	cin>>T;
	for (int i=1;i<=T;i++){
		cout<<"\nCase #"<<i<<": "<<botmove();
	}
	return 0;
}

int botmove(){
	bot o,b;	
	int N;		//Number of buttons to be pressed
//	cout<<"Enter number of buttons to be pressed\t";
	cin>>N;
	int pos[N];	//Button number to be pressed
	char bot[N];	//Bot to press the button
	int i,final_time=0;
	for(i=0;i<N;i++){
//		cout<<"\nenter ith bot and button to be pressed";
		cin>>bot[i];
		if(bot[i]!='O'&&bot[i]!='B'){
			cout<<"Wrong INput";
			 
		}
		cin>>pos[i];
		if(pos[i]<1||pos[i]>100){
			cout<<"Wrong INput";
			 
		}
	}
/*	
	for(i=1; i<=N;i++){
		cout<<"\n"<<bot[i]<<" "<<pos[i];
	}
*/
	for(i=0;i<N;i++){
		if(bot[i]=='O'){
			o.move(pos[i]);
			if(final_time>o.time){
				o.movement-=(final_time-o.time);
				if(o.movement<0)
					o.movement=0;			
			}			
			final_time+=o.movement;
			final_time++;	
			o.time=final_time;
			o.pos=pos[i];
			o.movement=0;
		}
		if(bot[i]=='B'){
			b.move(pos[i]);
			if(final_time>b.time){
				b.movement-=(final_time-b.time);
				if(b.movement<0)
					b.movement=0;			
			}			
			final_time+=b.movement;
			final_time++;	
			b.time=final_time;
			b.pos=pos[i];
			b.movement=0;
		}
//		cout<<"\nfinal_time"<< i<<": "<<final_time;
	}
		
	return final_time;

}
