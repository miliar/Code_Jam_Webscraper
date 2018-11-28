#include <iostream>
using namespace std;
int max(int a,int b)
{
	if(a > b)return a;
	return b;
}
int dist(int a,int b)
{	
	if(a > b) return a - b;
	else return b - a;
}
int main()
{
	int pos_1,pos_2;
	char a;
	int Z;
	cin>>Z;
	int time_t,time_b,time_a;
	for(int i = 0; i < Z; i++)
	{
		time_a = time_b = time_t = 0;
		pos_1 = pos_2 = 1;
		int N;
		cin>>N;
		for(int j = 0; j < N; j++)
		{
			int pos;
			cin>>a>>pos;
			if(a == 'O') 
			{
				time_a = max(time_a + dist(pos,pos_1) + 1,time_t + 1);
				time_t = max(time_a,time_b);
				pos_1 = pos;
			}
			else
			{
				time_b = max(time_b + dist(pos,pos_2) + 1,time_t + 1);
				time_t = max(time_a,time_b);
				pos_2 = pos;
			}
		}
		cout<<"Case #"<<i + 1<<": "<<time_t<<endl;
	}
	return 0;
}
				
				
