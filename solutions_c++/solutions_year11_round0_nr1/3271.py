#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

int main(){
	int caseCount = 0;
	cin >> caseCount;
	cin.ignore();
	for(int i=0;i<caseCount;i++){
		int time=0;
		int pos_orange=1;
		int pos_blue=1;
		//get input
		queue< pair<char,int> > jobs;
		queue<int> jobs_orange;
		queue<int> jobs_blue;
		string inText;
		string tempText;
		getline(cin,inText);
		stringstream streamInText(inText);
		bool end=false;
		int buttonCount=0;
		streamInText>>buttonCount;
		for(int j=0;j<buttonCount;j++){
			char r;
			int d;
			streamInText >> r;
			streamInText >> d;
			pair<char,int> p;
			p.first = r;
			p.second = d;
			jobs.push(p);
			if(r=='O'){
				jobs_orange.push(d);
			}
			if(r=='B'){jobs_blue.push(d);
			}
		}
		//move robots
		while(jobs.size()>0){
			int push=0;

			if(jobs_orange.size()>0){
				if(pos_orange<jobs_orange.front())pos_orange++;
				else if(pos_orange>jobs_orange.front())pos_orange--;
				else{
					if(
							(jobs.front().first=='O')&&
							(jobs.front().second==pos_orange)
					  )push=1;
				}
			}

			if(jobs_blue.size()>0){
				if(pos_blue<jobs_blue.front())pos_blue++;
				else if(pos_blue>jobs_blue.front())pos_blue--;
				else{
					if(
							(jobs.front().first=='B')&&
							(jobs.front().second==pos_blue)
					  )push=2;
				}
			}

			if(push==1){
				jobs.pop();
				jobs_orange.pop();
			}
			else if(push==2){
				jobs.pop();
				jobs_blue.pop();
			}
			time++;
		}
		//return output
		cout << "Case #"<<i+1<<": "<<time<<endl;
	}
}
