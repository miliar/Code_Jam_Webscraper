#include <iostream>
#include <queue>

using namespace std;

class Train
{
	public:
	int time;
	int dir;//0 from,1 to
	int city;//0 -A ,1-B
};

bool operator<(Train a,Train b){
	if(a.time==b.time)
	return a.dir<b.dir;
	return (a.time>b.time);}

priority_queue<Train> pQ;

int t,na,nb,T;


int main()
{
	int u,i,num1,num2,num;
	int stock[2],sol[2];
	char c;
	cin >> t;
	Train a;
	for(u=0;u<t;u++)
	{
		cin >> T;
		cin >> na >> nb;
		a.city=0;
		for(i=0;i<na;i++)
		{
			cin >> num1 >> c >> num2; 
			num=num1*100+num2;
			a.city=0;
			a.dir=0;
			a.time=num;
			pQ.push(a);
			
			cin >> num1 >> c >> num2; 
			num=num1*100+num2+T;
			a.city=1;
			a.dir=1;
			a.time=num;
			pQ.push(a);
		}
		
		for(i=0;i<nb;i++)
		{
			cin >> num1 >> c >> num2; 
			num=num1*100+num2;
			a.city=1;
			a.dir=0;
			a.time=num;
			pQ.push(a);
			
			cin >> num1 >> c >> num2; 
			num=num1*100+num2+T;
			a.city=0;
			a.dir=1;
			a.time=num;
			pQ.push(a);
		}
		
		stock[0]=stock[1]=sol[0]=sol[1]=0;
		while(!pQ.empty())
		{
			a=pQ.top();
			pQ.pop();
			
			if(a.dir==0)
			{
				if(stock[a.city]>0)
				stock[a.city]--;
				else
				sol[a.city]++;			
			}
			else if(a.dir==1)
			{
				stock[a.city]++;			
			}
			
			//cout << a.time << " " << a.city << " " << a.dir << "\n";
		}
		cout << "Case #" << (u+1) << ": " << sol[0] << " " << sol[1] << "\n";	
	}
	return 0;
}
