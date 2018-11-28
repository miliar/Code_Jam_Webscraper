#include <iostream>
#include <deque>
#include <string>
using std::cout;
using std::string;
using std::cin;
using std::cerr;
using std::deque;

struct cmd
{
	int dest;
	int seq;
};

typedef deque<int> DS;
typedef deque<cmd> DC;

void trymove(const DC & cmd, int & cur_pos)
{
	if(cmd.size() == 0)
		return;
	int dest = cmd[0].dest;

	if(dest == cur_pos)
		return;
	if(dest < cur_pos)
		cur_pos--;
	else
		cur_pos++;
}

int main()
{
	int tc_count;
	cin >> tc_count;
	string t;
	getline(cin, t);
	for(int tc_index=1; tc_index <= tc_count; tc_index++)
	{
		int n;
		cin >> n;
		
		DC bcmd, ocmd;

		deque<char> rseq;

		for(int i =0 ; i < n ; i++)
		{
			int d;
			char who;
			cin >> who >> d;

			cmd t;
			t.dest = d;
			t.seq = i;

			if(who == 'O')
				ocmd.push_back(t);
			else
				bcmd.push_back(t);

			rseq.push_back(who);
		}

		int res=0;
		int seq_id=0;

		int opos =1, bpos = 1;
		for(; ocmd.size() + bcmd.size(); res++)
		{
			bool opush = false, bpush = false;
			if(rseq[seq_id] == 'O')
			{
				if(opos == ocmd[0].dest)
				{
					ocmd.pop_front();
					seq_id++;
//					cerr << (res+1) << " pushed O\n\n";
					opush =  true;
				}
			}
			else
			{
				if(bpos == bcmd[0].dest)
				{
					bcmd.pop_front();
					seq_id++;
//					cerr << (res+1) << " pushed B\n\n";
					bpush =  true;
				}
			}

			if(!opush)
				trymove(ocmd, opos);
			if(!bpush)
				trymove(bcmd, bpos);

/*
			cerr << (res+1) << ' ' << rseq[seq_id] << " "
			 << opos << ' '
			 << bpos << ' '
			 << '\n';
			 */
		}

		cout << "Case #" << tc_index <<  ": " 
		<<	res
		<< "\n";
	}
	return 0;
}
