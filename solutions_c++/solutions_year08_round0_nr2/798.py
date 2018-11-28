#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
struct Trip {
	int start;
	int end;
	int dir;
};
Trip A[101], B[101], AB[201];
int time[1600][2];
int change(string s)
{
	int ret = ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + ((s[3] - '0') * 10 + (s[4] - '0'));
	return ret;
}
int cmp(const Trip& a, const Trip& b)
{
	if(a.start == b.start)
		return a.end < b.end;
	return a.start < b.start;
}
int main()
{
	ifstream cin("input.txt");
	ofstream cout("out.txt");
	int n;
	cin>>n;
	for(int CASE = 1; CASE <= n; CASE++)
	{
		int T, NA, NB;
		cin>>T>>NA>>NB;
		string start, end;
		int p = 0;
		for(int i = 1; i <= NA; i++)
		{
			cin>>start>>end;
			A[i].start = change(start);
			A[i].end = change(end);
			A[i].dir = 0;
			AB[p++] = A[i];
		}
		for(int i = 1; i <= NB; i++)
		{
			cin>>start>>end;
			B[i].start = change(start);
			B[i].end = change(end);
			B[i].dir = 1;
			AB[p++] = B[i];
		}

		sort(AB, AB + p, cmp);

		//for(int i = 0; i < p; i++)
		//{
		//	cout<<AB[i].dir << " " <<AB[i].start<<" "<<AB[i].end<<endl;
		//}
		int ansa = 0, ansb = 0;
		for(int i = 0; i < 1600; i++)
			time[i][0] = time[i][1] = 0;
		for(int i = 0; i < p; i++)
		{
			if(AB[i].dir == 0) //A->B
			{
				if(time[AB[i].start][0] == 0)
				{
					for(int j = AB[i].end + T; j < 1600; j++)
						time[j][1]++;
					ansa++;

				}
				else
				{
					for(int j = AB[i].start; j < 1600; j++)
						time[j][0]--;
					for(int j = AB[i].end + T; j < 1600; j++)
						time[j][1]++;
				}
			}
			else  //B->A
			{
				if(time[AB[i].start][1] == 0)
				{
					for(int j = AB[i].end + T; j < 1600; j++)
						time[j][0]++;
					ansb++;
				}
				else
				{
					for(int j = AB[i].start; j < 1600; j++)
						time[j][1]--;
					for(int j = AB[i].end + T; j < 1600; j++)
						time[j][0]++;
				}
			}
		}
		cout<<"Case #"<<CASE<<": "<<ansa<<" "<<ansb<<endl;
	}
}
