#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class timetable
{
public:
	vector<int> leavea;
	vector<int> arriveb;
	vector<int> leaveb;
	vector<int> arrivea;
	int turnaround;
	int na;
	int nb;
	timetable();
};

timetable::timetable()
{
	int turnt, nat, nbt, j, i;
	int strl, stra;
	char c;
	cin >> turnt >> nat >> nbt;
	turnaround = turnt;
	na = nat;
	nb = nbt;
	//cout<<na<<nb<<turnt<<endl;
	for (i = 0; i < na; i++)
	{
		//cin.get(strl, 2, ':');
		cin >> strl;
		cin >> c;
		cin >> stra;
		strl *= 60;
		strl += stra;
		leavea.push_back(strl);

		cin >> strl;
		cin >> c;
		cin >> stra;
		strl *= 60;
		strl += stra;
		//cin.get(stra, 2, ':');
		arriveb.push_back(strl);
	}
	for (j = 0; j < nb; j++)
	{
		//cin.get(strl, 2, ':');
		cin >> strl;
		cin >> c;
		cin >> stra;

		strl *= 60;
		strl += stra;

		leaveb.push_back(strl);
		cin >> strl;
		cin >> c;
		cin >> stra;
		strl *= 60;
		strl += stra;
		//cout<<"lll"<<strl;
		//cin.get(stra, 2, ':');
		arrivea.push_back(strl);
	}
	//////////////////////////////////////////////////////////////////////////
	sort(leavea.begin(), leavea.end());
	sort(arrivea.begin(), arrivea.end());
	sort(leaveb.begin(), leaveb.end());
	sort(arriveb.begin(), arriveb.end());
	//vector<int>::iterator pos;

	for (i = 0; i < arriveb.size(); i++)
	{
		for (j = 0; j < leaveb.size(); j++)
		{
			if ((leaveb[j] - arriveb[i]) >= turnaround && nb > 0)
			{
				nb--;
				//cout<<"mmmmm"<<arriveb[i]<<"mmmmm"<<leaveb[j]<<endl;
				leaveb[j] = 0;

				break;
			}
		}
	}
	for (i = 0; i < arrivea.size(); i++)
	{
		for (j = 0; j < leavea.size(); j++)
		{
			if (leavea[j] - arrivea[i] >= turnaround && na > 0)
			{
				na--;
				//cout<<"nnnnn"<<arrivea[i]<<"nnnn"<<leavea[j]<<endl;
				leavea[j] = 0;

				break;
			}
		}
	}
}

int main()
{
	int number;
	cin >> number;
	timetable* t = new timetable[number];
	for (int i = 0; i < number; i++)
	{
		//cout<<"size"<<t[i].leavea.size();
		// 		for (int j = 0; j < t[i].leavea.size(); j++)
		// 		{
		cout <<
			"Case #" <<
			i +
			1 <<
			": " <<
			t[i].na <<
			" " <<
			t[i].nb <<
			endl;
		// 			cout << "aaaaa" << t[i].leavea[j]<<endl;
		// 			cout << "bbbbbb" << t[i].arriveb[j]<<endl;
		/*}*/
	}
	return 1;
}