#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

vector<int> orange,blue;
int N,T;

int main()
{
	string s,seq;
	int i,j,k,pos_o,pos_b,result,id_o,id_b,step;
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin >> T;
	for (i=0;i<T;i++)
	{
		cin >> N;
		pos_o=1;
		pos_b=1;
		id_o=0;
		id_b=0;
		result=0;
		orange.clear();
		blue.clear();
		seq.clear();
		for (j=0;j<N;j++)
		{
			cin >> s >> k;
			seq=seq+s;
			if (s=="O")
				orange.push_back(k);
			else
				blue.push_back(k);
			//orange.push_back(101);
			//blue.push_back(101);
		}
		for (j=0;j<N;j++)
		{
			if (seq[j]=='O')
			{
				step=abs(orange[id_o]-pos_o)+1;
				result=result+step;
				pos_o=orange[id_o];
				id_o++;
				if (id_b<blue.size())
				{if (blue[id_b]>=pos_b)
				{
					pos_b=min(pos_b+step,blue[id_b]);
				}
				else
				{
					pos_b=max(pos_b-step,blue[id_b]);
				}}
			}
			else
			{
				step=abs(blue[id_b]-pos_b)+1;
				result=result+step;
				pos_b=blue[id_b];
				id_b++;
				if (id_o<orange.size())
				{
				if (orange[id_o]>=pos_o)
				{
					pos_o=min(pos_o+step,orange[id_o]);
				}
				else
				{
					pos_o=max(pos_o-step,orange[id_o]);
				}
				}
			}
		}
		cout << "Case #" << i+1 << ": " << result << endl;
	}
	return 0;
}