#include<iostream>
#include<fstream>
using namespace std;

struct Label{
	char color;
	int pos;
};


int main()
{

	int Num,n,m;
	ofstream output("output.txt", ios::out|ios::trunc);
	ifstream cin("input.txt",ios::in);


	cin>>Num;
	for(int i = 1; i <= Num; i ++){
		cin>>n;
		struct Label* list= new Label[n];
		struct Label* olist= new Label[n];
		struct Label* blist= new Label[n];
		int ocount = 0,bcount = 0,sumcount = 0;


		for(int j = 0; j < n; j ++){
			char inputColor;
			int inputPos;
			cin>>inputColor>>inputPos;
			list[sumcount].color = inputColor;
			list[sumcount].pos = inputPos;
			sumcount ++;

			if(inputColor == 'O'){
				olist[ocount].color = inputColor;
				olist[ocount].pos = inputPos;
				ocount ++;
			}
			else{
				blist[bcount].color = inputColor;
				blist[bcount].pos = inputPos;
				bcount ++;
			}
		}

		int k= 0,ans = 0,ok = 0,bk = 0;

		//initialize
		int oPos = 1;
		int bPos = 1;
		int stopFlag = 0;

		char nextColor = list[k].color;
		int nextPos = list[k].pos;

		int nextOPos,nextBPos;

		if(nextColor == 'O'){
			nextOPos = nextPos;
			if(bk < bcount){
				nextBPos = blist[bk].pos;
			}
			else{
				nextBPos = -1;
			}
		}
		else{
			nextBPos = nextPos;
			if(ok < ocount){
				nextOPos = olist[ok].pos;
			}
			else{
				nextOPos = -1;
			}
		}
	
		//ans ++;

		while(true){
			//cout <<  nextColor << nextPos << " " << oPos << " " << bPos <<" "<<ans<<"start" <<endl;
			stopFlag = 0;

			if(nextOPos > oPos &&oPos < 100){
				oPos ++;
			}
			else if(nextOPos < oPos && oPos > 0){
				oPos --;
			}
			else if(nextOPos == oPos){

				if(nextColor == 'O' && nextOPos == nextPos){

					stopFlag = 1;
					ok ++;
					nextOPos = olist[ok].pos;					
				}
			}

			if(nextBPos > bPos &&bPos < 100){
				bPos ++;
			}
			else if(nextBPos < bPos && bPos > 0){
				bPos --;
			}
			else if(nextBPos == bPos){

				if(nextColor == 'B' && nextBPos == nextPos){
					stopFlag = 1;
					bk ++;
					nextBPos = blist[bk].pos;
				}
			}

			
			if(stopFlag == 1){
					k ++;
					
					if(k == sumcount){
						cout<<"Case #"<<i<< ": "<<ans+1<<endl;
						output<<"Case #"<<i<< ": "<<ans+1<<endl;
						//fprintf("output.txt","Case #%d: %d\n",i,ans+1);

						break;
					}	
					
					nextColor = list[k].color;
					nextPos = list[k].pos;
			}

			ans ++;
			//cout << nextColor << nextPos << " " << oPos << " " << bPos <<" "<<ans<<" "<<k<<endl;
		}

		}


		output.close();
		cin.close();

		return 0;

}



			
			





