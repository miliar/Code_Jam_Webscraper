#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void main()
{
	int n, na, nb, turnaround;
	int hour, min;
	//istream &in = cin;
	//ostream &out = cout;
	ifstream in("in.txt");
	ofstream out("out.txt");
	in>>n;
	for(int i = 0; i < n; ++ i)
	{
		in>>turnaround;
		in>>na>>nb;
		vector<int> eat(na, 0);
		vector<int> aat(na, 0);
		char ch;
		for(int j = 0; j < na; ++ j)
		{
			in>>hour>>ch>>min;
			eat[j] = hour * 60 + min;
			in>>hour>>ch>>min;
			aat[j] = hour * 60 + min + turnaround;
		}
		for(int j = 0; j < na; ++ j)
		{
			for(int k = j + 1; k < na; ++ k)
			{
				if(eat[j] > eat[k])
				{
					int temp = eat[j];
					eat[j] = eat[k];
					eat[k] = temp;

					temp = aat[j];
					aat[j] = aat[k];
					aat[k] = temp;
				}
			}
		}

		vector<int> ebt(nb, 0);
		vector<int> abt(nb, 0);
		for(int j = 0; j < nb; ++ j)
		{
			in>>hour>>ch>>min;
			ebt[j] = hour * 60 + min;
			in>>hour>>ch>>min;
			abt[j] = hour * 60 + min + turnaround;
		}
		for(int j = 0; j < nb; ++ j)
		{
			for(int k = j + 1; k < nb; ++ k)
			{
				if(ebt[j] > ebt[k])
				{
					int temp = ebt[j];
					ebt[j] = ebt[k];
					ebt[k] = temp;

					temp = abt[j];
					abt[j] = abt[k];
					abt[k] = temp;
				}
			}
		}
		int as = 0, bs = 0;
		bool isA = false;
		bool end = true;
		int p = 0, q = 0;
		int at = 0;
		while(true)
		{
			if(end)
			{
				for(; p < na; ++ p)
				{
					if(eat[p] < 25 * 60) break;
				}
				for(; q < nb; ++ q)
				{
					if(ebt[q] < 25 * 60) break;
				}
				if(na == p) 
				{
					//bs += nb - q;
					for(; q < nb; ++ q) bs += ebt[q] < 25 * 60;
					break;
				}
				if(nb == q)
				{
					//as += na - p;
					for(; p < na; ++ p) as += eat[p] < 25 * 60;
					break;
				}
				if(eat[p] < ebt[q])
				{
					++ as;
					isA = false;
					at = aat[p];
					eat[p] = 26 * 60;
				}
				else 
				{
					++ bs;
					isA = true;
					at = abt[q] ;
					ebt[q] = 26 * 60;
				}
				end = false;
			}
			if(isA)
			{
				int m;
				for(m = 0; m < na; ++ m)
				{
					if(eat[m] < 25*60 && at <= eat[m])
					{
						at = aat[m];
						eat[m] = 26 * 60;
						isA = false;
						break;
					}
				}
				if(m == na)	end = true;
			}
			else 
			{
				int m;
				for(m = 0; m < nb; ++ m)
				{
					if(ebt[m] < 25*60 && at <= ebt[m])
					{
						at = abt[m];
						ebt[m] = 26 * 60;
						isA = true;
						break;
					}
				}
				if(m == nb)	end = true;
			}
		}
		out<<"Case #"<<(i+1)<<": "<<as<<" "<<bs<<endl;
	}
	out.close();
	in.clear();
	system("out.txt");
}
