#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Train
{
	public:
		Train(string start, string end, int Turn)
		{
			begin = 60*atoi(&start[0]) + atoi(&start[3]);
			this->end = 60*atoi(&end[0]) + atoi(&end[3]) + Turn;
		}

		bool operator < (const Train & rhs) const
		{
			return begin < rhs.begin;
		}

		int begin,end;
};

ostream & operator << (ostream & out, const Train & rhs)
{
	out << rhs.begin << " " << rhs.end;
	return out;
}

template <typename T>
void printV(vector<T> & source)
{
	for(unsigned int i=0;i<source.size();i++)
	{
		cout << source[i] << endl;
	}
}

int main()
{
	int num;
	cin >> num;
	for(int i=1;i<=num;i++)
	{
		int turnTime, NA, NB;
		cin >> turnTime >> NA >> NB;

		vector<vector<Train> > Trains(2);
		for(int j=0;j<NA;j++)
		{
			string t1,t2;
			cin >> t1 >> t2;
			Trains[0].push_back(Train(t1,t2,turnTime));
		}

		for(int j=0;j<NB;j++)
		{
			string t1,t2;
			cin >> t1 >> t2;
			Trains[1].push_back(Train(t1,t2,turnTime));
		}

		sort(Trains[0].begin(),Trains[0].end());
		sort(Trains[1].begin(),Trains[1].end());
#ifdef DEBUG
		printV(Trains[0]);
		cout << endl;
		printV(Trains[0]);
		cout << endl;
		printV(Trains[1]);		
		cout << endl;
		printV(Trains[1]);		
		cout << endl;
#endif
		vector<int> answer(2,0);
		while((!Trains[0].empty())||(!Trains[1].empty()))
		{
			int curTime;
			if(Trains[1].empty())
			{
#ifdef DEBUG
				cout << "B is empty, adding: " << Trains[0].size() << " to A" << endl;
#endif
				answer[0] += Trains[0].size();
				break;
			}
			if(Trains[0].empty())
			{
#ifdef DEBUG
				cout << "A is empty, adding: " << Trains[1].size() << " to B" << endl;
#endif
				answer[1] += Trains[1].size();
				break;
			}
			int choice;
			if(Trains[0][0] < Trains[1][0])
			{
				choice = 0;
				curTime = Trains[0][0].end;
#ifdef DEBUG
				cout << "Chose A: " << Trains[0][0] << " with time: " << curTime << endl; 
#endif
				Trains[0].erase(Trains[0].begin());
			}
			else
			{
				choice = 1;
				curTime = Trains[1][0].end;
#ifdef DEBUG
				cout << "Chose B: " << Trains[1][0] << " with time: " << curTime << endl; 
#endif
				Trains[1].erase(Trains[1].begin());
			}
			answer[choice]++;
			int lookingat = !choice;
			
			for(int j=0;j<Trains[lookingat].size();j++)
			{
				if(Trains[lookingat][j].begin >= curTime)
				{
					curTime = Trains[lookingat][j].end;
#ifdef DEBUG
					cout << "Found a new train!" << endl;
					cout << "On route: " << lookingat << ": " << Trains[lookingat][j] << endl;
					cout << "New time: " << curTime << endl;
					printV(Trains[0]);
					cout << endl;
					printV(Trains[1]);
					cout << endl;
#endif
					Trains[lookingat].erase(Trains[lookingat].begin()+j);
					lookingat = !lookingat;
					j=-1;
				}
			}
		}
		cout << "Case #" << i << ": " << answer[0] << " " << answer[1] << endl;
	}
	return 0;
}
