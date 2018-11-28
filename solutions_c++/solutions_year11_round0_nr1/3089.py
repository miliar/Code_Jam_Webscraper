#include <iostream>
#include <vector>
#define debug 0

using namespace std;

int getNextPos(vector<pair<short, short> >& cmds, int st, int type, int& endpos)
{
	for (int i=max(0,st); i<cmds.size(); i++)
	{
		if (cmds[i].first == type) { endpos=cmds[i].second; return i;}
	}
	return -1;
}
int move (int& pos, int& end, int moves)
{
	int d=(pos<end?1:-1);
	pos = pos + min(abs(end-pos), moves)*d;
	return 0;
}

int process(vector<pair<short, short> >& cmds)
{
	int pos0 = 1, pos1 = 1, idx0=-1, idx1=-1;
	int endpos0 = -1, endpos1=-1;
	int totSec = 0;
	int cnt = 0;
	while (1)
	{
		cnt++;
		if(debug)
			cout << cnt << ". idx0 = " << idx0 << ", idx1 = " << idx1 << endl;
		
		int next0 = getNextPos(cmds, idx0, 0, endpos0);
		int next1 = getNextPos(cmds, idx1, 1, endpos1);
		if(debug)
		{
		cout << cnt << ". next0 = " << next0 << ", next1 = " << next1 << ", endpos0 = " 
			<< endpos0 << ", endpos1 = " << endpos1 << endl;
		}
		
		if(next1 == -1 && next0 == -1) return totSec;
		if (next1 == -1 || (next0 != -1 && next0 < next1))
		{
			int tomove = abs(endpos0 - pos0) + 1;
			totSec += tomove;
			pos0=endpos0;
			move(pos1,endpos1,tomove);
			idx0 = next0+1;
		}
		else if(next0 == -1 || (next1 != -1 && next1 < next0))
		{
			int tomove = abs(endpos1-pos1) + 1;
			totSec += tomove;
			pos1=endpos1;
			move(pos0,endpos0,tomove);
			idx1 = next1+1;
		}
		if(debug)
		cout << cnt << ". totSec = " << totSec << ", pos0 = " << pos0 << ", pos1 = " << pos1 << endl;
	}
}

int main (int argc, char * const argv[]) {
	int T;
	
	cin >> T;
	for(int i=0; i< T; i++)
	{
		vector<pair<short, short> > cmds;
		
		int N;
		cin >> N;
		for (int j=0; j< N; j++)
		{
		char c;
		short pos;
		cin >> c >> pos;
		cmds.push_back(make_pair((c=='O'?0:1), pos));
		}
		int totSec = process(cmds);
		cout << "Case #" << i+1 << ": " << totSec << endl;
	}
	
	
	
    return 0;
}
