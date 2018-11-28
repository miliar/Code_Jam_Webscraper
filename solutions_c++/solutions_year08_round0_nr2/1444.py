#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>

using namespace std;

struct AtoB
{
	int D;
	int A;
	int Dir;
};

vector<AtoB> AB;

bool mycmp(AtoB m,AtoB n)
{
	if(m.D < n.D) return 1;
	if(m.D > n.D) return 0;
	if(m.A < n.A) return 1;
	if(m.A > n.A) return 0;
	return m.Dir>n.Dir? 1:0;
}

int main()
{
	int N;
	cin >> N;
	int t = 0;
	while(N--)
	{
		AB.clear();
		int T;
		cin >> T;
		int NA,NB;
		cin >> NA >> NB;
		char p[20];
		getchar();
		AtoB atob;
		for(int i = 0; i< NA; ++i) 
		{
			gets(p);
			//cout << p << endl;
			int hour,min;
			hour = (p[0]-'0')*10 + (p[1]-'0');
			min = (p[3]-'0')*10 + (p[4]-'0');
			atob.D = hour*60+min;

			hour = (p[6]-'0')*10 + (p[7]-'0');
			min = (p[9]-'0')*10 + (p[10]-'0');
			atob.A = hour*60+min+T;
			atob.Dir = 1;
			AB.push_back(atob);
		}
		for(int i = 0; i< NB; ++i)
		{
			gets(p);
			//cout << p << endl;
			int hour,min;
			hour = (p[0]-'0')*10 + (p[1]-'0');
			min = (p[3]-'0')*10 + (p[4]-'0');
			atob.D = hour*60+min;

			hour = (p[6]-'0')*10 + (p[7]-'0');
			min = (p[9]-'0')*10 + (p[10]-'0');
			atob.A = hour*60+min+T;
			atob.Dir = 0;
			AB.push_back(atob);
		}
		sort(AB.begin(),AB.end(),mycmp);
		//for(int i = 0; i< AB.size(); ++i) cout << AB[i].D << "   " << AB[i].A << "      " << AB[i].Dir << endl;
		int A_num = 0;
		int B_num = 0;
		int len = AB.size();
		int *tag = new int[len+1];
		memset(tag,0,sizeof(tag));
		for(int i = 0; i< AB.size(); ++i)
		{
			if(tag[i] == 1) continue;
			tag[i] = 1;
			int start;
			if(AB[i].Dir == 1) start = 1;
			else start = 0;
			int end = 0;
			if(start == 0) end = 1;
			while(true)
			{
				bool ok = false;
				for(int k = 0; k< len; ++k)
				{
					if(tag[k] == 1) continue;
					if(AB[k].Dir == end)
					{
						if(AB[k].D>=AB[i].A)
						{
							AB[i].A = AB[k].A;
							if(end == 1) end = 0;
							else end = 1;
							ok = true;
							tag[k] = 1;
							break;
						}
						else
						{
						}
					}
				}
				if(ok == false) break;
			}
			if(start == 1) A_num++;
			else B_num ++;
		}
		cout << "Case #" << ++t << ": " << A_num << " " << B_num << endl;

	}
	return 0;
}

