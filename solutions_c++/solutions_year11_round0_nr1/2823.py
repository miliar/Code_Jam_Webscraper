#include <iostream>
using namespace std;


struct Action
{
	public:
	void setAction(int b, int t)
	{
		but = b;
		time = t;
	}
	int but;
	int time;
};

int main()
{
	int Q;
	cin>>Q;
	for (int q = 0; q < Q; q++){
		Action orange[120];
		Action blue[120];
		int oM = 0;
		int bM = 0;
		int n;

		cin >> n;

		int tim = 0;
		for (int m = 0; m < n; m++) {
			char ch;
			int but;
			cin >> ch >> but;

			if(ch == 'O')
				orange[oM++].setAction(but, tim++);
			else if(ch == 'B')
				blue[bM++].setAction(but, tim++);
		}
		
		int b = 0;
		int o = 0;
		int oP =1;
		int bP =1;
		int time = 0;	
		int count = 0;
		while(time < tim){
			if(o<oM && orange[o].time == time){
				if(orange[o].but == oP){
					time++;
					o++;
				}
				else{
					oP += (orange[o].but > oP)?1:-1;
				}

				if(blue[b].but != bP){
					bP += (blue[b].but > bP)?1:-1;
				}
			}
			else if(b<bM && blue[b].time == time){
				if(blue[b].but == bP){ 
					time++;
					b++;
				}
				else{
					bP += (blue[b].but > bP)?1:-1;
				}

				if(orange[o].but != oP){
					oP += (orange[o].but > oP)?1:-1;
				}
			}
			count++;
		}
		 
		cout<<"Case #"<<q+1<<": "<<count<<endl;
	}
}

