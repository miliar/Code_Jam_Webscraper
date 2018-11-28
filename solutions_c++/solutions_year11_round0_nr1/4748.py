#include<iostream>
#include<queue>
#include<cmath>

using namespace std;

struct cmd{
	int to;
	char who;
};

queue<cmd> command;
queue<cmd> clear;
int po=1,pb=1;						//positon of orange&blue

void setpositon(cmd p){
	if(p.who=='O')
		po=p.to;
	else
		pb=p.to;
}

int gettime(cmd c){
	if(c.who=='O')
		return abs(c.to-po)+1;
	else
		return abs(c.to-pb)+1;
}


int run(){
	int time=0,pretime=0,total=0;
	cmd pre=command.front();
	command.pop();
	pretime=pre.to;
	total+=pretime;
	setpositon(pre);
	while(!command.empty()){
		if(pre.who==command.front().who){
			time=gettime(command.front());
			total+=time;
			pretime+=time;
			setpositon(command.front());
		}
		else{
			time=gettime(command.front());
			setpositon(command.front());
			if(time>pretime){
				total+=time-pretime;
				pretime=time-pretime;
			}
			else{
				total+=1;
				pretime=1;
			}
		}
		pre=command.front();
		command.pop();
	}
	return total;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cases=0;
	cin>>cases;
	for(int casecount=1;casecount<=cases;casecount++){
		command=clear;
		po=1,pb=1;
		int cmds=0;
		cmd input;
		cin>>cmds;
		for(int cmdcount=0;cmdcount<cmds;cmdcount++){
			cin>>input.who>>input.to;
			command.push(input);
		}
		int time=run();
		cout<<"Case #"<<casecount<<": "<<time<<endl;
	}
	return 0;
}

