#include <iostream>
#include <queue>
#include <sstream>
#include <functional>

using namespace std;

int read_time()
{
	string time;
	int t;

	cin >> time;
		
	istringstream reader(time);
	reader >> t;
	t *= 100;
	
	char c;
	reader >> c; //throw away colon
	
	int tmp;
	reader >> tmp;
	t += tmp;
	
	return t;
}

int main()
{
	int numCases;
	cin >> numCases;
	
	for (int caseNum = 1; caseNum <= numCases; caseNum++)
	{
		int turn;
		cin >> turn;

		int na, nb;
		cin >> na >> nb;
		
		priority_queue<int, vector<int>, greater<int> > a_arrive;
		priority_queue<int, vector<int>, greater<int> > a_depart;
		priority_queue<int, vector<int>, greater<int> > b_arrive;
		priority_queue<int, vector<int>, greater<int> > b_depart;
		
		a_arrive.push(9999);
		b_arrive.push(9999);
		a_depart.push(9999);
		b_depart.push(9999);
		
		for (int i = 0; i < na; i++)
		{
			int tda, tab;
			tda = read_time();
			tab = read_time();
			
			a_depart.push(tda);
			
			tab += turn;
			int diff = tab % 100;
			if (diff >= 60)
			{
				tab += 100;
				tab -= 60;
			}
			b_arrive.push(tab);
		}
		
		for (int i = 0; i < nb; i++)
		{
			int tdb, taa;
			tdb = read_time();
			taa = read_time();
			
			b_depart.push(tdb);
			
			taa += turn;
			int diff = taa % 100;
			if (diff >= 60)
			{
				taa += 100;
				taa -= 60;
			}
			a_arrive.push(taa);
		}
		
		int a = 0;
		int b = 0;
		
		int needa = 0;
		int needb = 0;
		
		while (!a_arrive.empty() || !b_arrive.empty() || !a_depart.empty() || !b_depart.empty())
		{
			int tda, tab, tdb, taa;
			tda = a_depart.top();
			tab = b_arrive.top();
			tdb = b_depart.top();
			taa = a_arrive.top();
			
			int next = min(tda, min(tab, min(tdb, taa)));
			
			//cout << next << ": (" << tda << ", " << tab << ", " << tdb << ", " << taa << ")" << endl;
			if (next == 9999) break; //End of all of the lists
			
			if (taa == next)
			{
				//cout << "   train ready at a" << endl;
				a_arrive.pop();
				a++;
			}
			
			if (tab == next)
			{
				//cout << "   train ready at b" << endl;
				b_arrive.pop();
				b++;
			}
			
			if (tda == next)
			{
				//cout << "   train leaving a" << endl;
				a_depart.pop();
				
				if (a == 0)
				{
					needa++;
				}
				else
				{
					a--;
				}
			}
			
			if (tdb == next)
			{
				//cout << "   train leaving b" << endl;
				b_depart.pop();
				
				if (b == 0)
				{
					needb++;
				}
				else
				{
					b--;
				}
			}
		}

		cout << "Case #" << caseNum << ": " << needa << " " << needb << endl;
	}
	
	return 0;
}