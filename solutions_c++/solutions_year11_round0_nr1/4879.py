#include <iostream>
#include <vector>
#include <utility>
using namespace std;

class ROBOT
{
public:
	ROBOT()
	{
		pos=1,current=0;
	}
	int pos;
	int current;
	vector< pair<int,int> > button;
}r[2];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	int c=0;
	while(t--)
	{
		c++;
		ROBOT r[2];
		int n;
		cin >> n;
		char color;
		int id;
		for(int i=0;i<n;++i)
		{
			cin >> color >> id;
			if(color=='O')
				r[0].button.push_back(make_pair(i,id));
			else
				r[1].button.push_back(make_pair(i,id));
		}
		int index;
		int other;
		int total=0;
		while(true)
		{
			if(r[0].current==r[0].button.size())
			{
				for(int i=r[1].current;i<r[1].button.size();++i)
				{
					total += abs(r[1].button[i].second-r[1].pos)+1;
					r[1].pos=r[1].button[i].second;
				}
				break;
			}
			if(r[1].current==r[1].button.size())
			{
				for(int i=r[0].current;i<r[0].button.size();++i)
				{
					total += abs(r[0].button[i].second-r[0].pos)+1;
					r[0].pos=r[0].button[i].second;
				}
				break;
			}
			if(r[0].button[r[0].current].first<r[1].button[r[1].current].first)
				index=0;
			else
				index=1;
			other = (index+1)%2;
			if((abs(r[index].pos-r[index].button[r[index].current].second)+1)>=abs(r[other].pos-r[other].button[r[other].current].second))
			{
				total += abs(r[index].pos-r[index].button[r[index].current].second) +2;
				r[index].pos = r[index].button[r[index].current].second;
				r[other].pos = r[other].button[r[other].current].second;
				r[index].current++;
				r[other].current++;
				if(r[index].current!=r[index].button.size())
				{
					if(r[index].pos<r[index].button[r[index].current].second)
						r[index].pos+=1;
					else if(r[index].pos>r[index].button[r[index].current].second)
						r[index].pos-=1;
				}
			}
			else
			{
				if(r[other].pos<r[other].button[r[other].current].second)
					r[other].pos = r[other].pos+abs(r[index].pos-r[index].button[r[index].current].second)+1;
				else
					r[other].pos = r[other].pos-abs(r[index].pos-r[index].button[r[index].current].second)-1;
				total += abs(r[index].pos-r[index].button[r[index].current].second)+1;
				r[index].pos = r[index].button[r[index].current].second;
				r[index].current++;
			}
		}
		cout << "Case #" << c << ": " << total << endl;
	}

	return 0;
}