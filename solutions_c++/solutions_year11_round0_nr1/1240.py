#include <iostream>
#include <list>
#include <stdlib.h>


using namespace std;

int main (int argc, char const *argv[])
{
	int T=0;
	cin>>T;
	int N, p; 
	char r;
	for(int i=0; i<T; i++){
	// input	
		list<int> seq;
		list<char> color;
		cin >> N;
		for(int j = 0; j < N; j++){
			cin>>r>>p;
			seq.push_back(p);
			color.push_back(r);
		}
	//
		int time = 0;
		int oPos = 1, bPos = 1;
		int interval=0, oldInt = 0;
		char c = color.front();
		
		while(!seq.empty()){
			p = seq.front();
			seq.pop_front();
			r = color.front();
			color.pop_front();
	//		cout<<p<<" "<<r<<endl;
			if(r == c){
				if(r == 'B'){
					time += abs(p - bPos) + 1;
					oldInt += abs(p - bPos) + 1;
					bPos = p;
				}else{
					time += abs(p - oPos) + 1;
					oldInt += abs(p - oPos) + 1;
					oPos = p;
				}
		//		cout<<time<<" oldInt is "<<oldInt<<endl;
			}else{
				c = r;
				if(r == 'B'){
					interval = abs(p - bPos);
					bPos = p;
				}else{
					interval = abs(p - oPos);
					oPos = p;
				}
		//		cout<<"interval "<<interval<<" oldInt "<<oldInt<<endl;
				if(interval > oldInt){
					time += interval - oldInt + 1;
					oldInt = interval - oldInt + 1;
				}else{
					time += 1;
					oldInt = 1;
				}
		//		cout<<time<<" oldInt is "<<oldInt<<" Interval is "<<interval<<endl;
			}
		}
	
	//output
		cout<< "Case #"<<i+1<<": "<< time<<endl;	
		
	}
	return 0;
}