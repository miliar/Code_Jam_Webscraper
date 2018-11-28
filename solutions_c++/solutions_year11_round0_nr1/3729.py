#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("//Users//KwonHC//Xcode//Qualification Round 2011 A. Bot Trust//A-large.in", "rt", stdin);
	freopen("//Users//KwonHC//Xcode//Qualification Round 2011 A. Bot Trust//A Bot Trust large.out", "wt", stdout);
	vector <int> robotO;
	vector <int> robotB;
	vector <char> order;
	int T, N;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		robotO.clear();
		robotB.clear();
		order.clear();
		cin >> N;
		while(N--)
		{
			char ctemp;
			int itemp;
			cin >> ctemp >> itemp;
			order.push_back(ctemp);
			if(ctemp=='O') robotO.push_back(itemp);
			else if(ctemp=='B') robotB.push_back(itemp);
		}
		int Opos=1; int Bpos=1;
		int Oindex=0; int Bindex=0;
		int cnt=0;
		for(int i=0; i<order.size(); i++)
		{
			if(order[i]=='O')
			{
				while(true)
				{
					cnt++;
					if(Bpos<robotB[Bindex])
						Bpos++;
					else if(Bpos>robotB[Bindex])
						Bpos--;
					
					if(Opos<robotO[Oindex])
						Opos++;
					else if(Opos>robotO[Oindex])
						Opos--;
					else if(Opos==robotO[Oindex])
						break;
				}
				Oindex++;
			}
			else if(order[i]=='B')
			{
				while(true)
				{
					cnt++;
					if(Opos<robotO[Oindex])
						Opos++;
					else if(Opos>robotO[Oindex])
						Opos--;
					
					if(Bpos<robotB[Bindex])
						Bpos++;
					else if(Bpos>robotB[Bindex])
						Bpos--;
					else if(Bpos==robotB[Bindex])
						break;
				}
				Bindex++;
			}
		}
		cout << "Case #" << t << ": " << cnt << endl;
	}
	return 0;
}