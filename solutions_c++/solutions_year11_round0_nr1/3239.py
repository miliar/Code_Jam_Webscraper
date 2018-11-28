#include<vector>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<functional>
#include<cmath>
using namespace std;
void compute(int cases);
int solveSteps(vector<int> v);
int main() {
	int p;
	cin>>p;
	for(int i=1; i<=p; i++) {
		compute(i);
	}
}

void compute(int cases) {
	int n;
	cin>>n;
	vector<int> vo;
	vector<int> vb;
	vector<char> lock;
	for(int i=0;i <n; i++) {
		int step; 
		char c;
		cin>>c>>step;
		if(c=='O') {
			vo.push_back(step);
		} else if(c=='B') {
			vb.push_back(step);
		}
		lock.push_back(c);
	}

	int ocur = 1;
	int ostep =0;//position in vo
	int bcur = 1;
	int bstep =0; //position in vb
	
	int steps = 0;
	
	for(int i= 0;i <n;i++) {
		char c= lock[i];
		if(c=='O') {
			//advance o;
			int maxstep =0;
			int next = vo[ostep];
			while(ocur!=next) {
				if(ocur<next) {
					ocur++;
					maxstep++;
				} else {
					ocur--;
					maxstep++;
				}
			}
            //press button
            maxstep++;
			//advance ob max to nextstep, or the required
			if (bstep<vb.size()) {
                
            
            next = vb[bstep];
			if(abs(next-bcur)>maxstep) {
				//we can move all max step;
				if(bcur<next) {
					bcur+=maxstep;
				} else {
					bcur-=maxstep;
				}
			} else {
				//move to next and wait;
				bcur = next;
			}
            }
			//to next 
			steps+=maxstep;
			ostep++;
		} else {
			//advance b;
            //advance o;
			int maxstep =0;
			int next = vb[bstep];
			while(bcur!=next) {
				if(bcur<next) {
					bcur++;
					maxstep++;
				} else {
					bcur--;
					maxstep++;
				}
			}
            maxstep++;
            if(ostep<vo.size()) {
			//advance ob max to nextstep, or the required
			next = vo[ostep];
			if(abs(next-ocur)>maxstep) {
				//we can move all max step;
				if(ocur<next) {
					ocur+=maxstep;
				} else {
					ocur-=maxstep;
				}
			} else {
				//move to next and wait;
				ocur = next;
			}
            }
			//press buton 
			steps+=maxstep;
			
			bstep++;
            
		}
	}
	cout<<"Case #"<<cases<<": "<<steps<<endl;
}

int solveSteps(vector<int> v) {
	int start =1;
	int steps=0;
	int length = v.size();
	for(int i=0; i<length; i++) {
		int cur = v[i];
		//walk to cur
		while(start!=cur) {
			if(start<cur) {
				start++;
				steps++;
			} else if(start > cur) {
				start--;
				steps++;
			}
		}
		//press cur
		if(start == cur) {
			steps++;
		}
	}
	return steps;
}
