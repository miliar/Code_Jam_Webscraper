#include <iostream>
#include <queue>
#include <map>

using namespace std;

void calc(int T, queue<int> O, queue<int> B, queue<char> Q)
{	
	int Bpos = 1;
	int Opos = 1;

	int timer = 0;
	while (!Q.empty())
	{
		timer++;
		bool act = false;
		if (O.size())
		{
			if (O.front() != Opos)
			{
				if (O.front() > Opos){
					Opos++;	// move right
				}
				else{
					Opos--;	// move left
				}
			}
			else if (Q.front() == 'O')
			{
				O.pop();
				Q.pop();
				act = true;
			}
		}
		
		if (B.size())
		{
			if (B.front() != Bpos)
			{
				if (B.front() > Bpos){
					Bpos++;	// move right
				}
				else{
					Bpos--;	// move left
				}
			}
			else if (Q.front() == 'B' && !act)
			{
				B.pop();
				Q.pop();
			}
		}
	}
	cout<<"Case #"<<T<<": "<<timer<<endl;
}

int main(int argc, char * argv[])
{
	int T, Tc = 1;
	cin>>T;

	while (T--)
	{
		int N;
		cin>>N;

		queue<int>B;
		queue<int>O;
		queue<char>Q;
		
		char R;
		int P;
		int orange = 0, blue = 0;

		for (int i = 0; i < N; i++)
		{
			cin>>R>>P;
			if (R == 'O'){
				O.push(P);
			}else{
				B.push(P);
			}
			Q.push(R);
		}
	
		calc(Tc++, O, B, Q);
	}
	return 0;
}