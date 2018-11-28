#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream f;
	f.open("B-large.in.in");
	int tcn;
	f >> tcn;
	for(int i=0; i<tcn; i++)
	{
		int clistn, rlistn;
		vector<string> clist, rlist;
		string tmp;
		string vacantstr = "";
		f >> clistn;
		for(int j=0;j<clistn; j++)
		{
			f >> tmp;
			clist.push_back(tmp);
			clist.push_back(vacantstr+tmp[1]+tmp[0]+tmp[2]);
		}

		f >> rlistn;
		for(int j=0; j<rlistn; j++)
		{
			f>>tmp;
			rlist.push_back(tmp);
			rlist.push_back(vacantstr+tmp[1]+tmp[0]);
		}

		int seqn;
		string seq;
		f >> seqn >> seq;

		string rslt="";
		for(int j=0; j<seqn; j++)
		{
			char nowc = seq[j];
			char beforec = (rslt.size()==0)? '\0': rslt[rslt.size()-1];
		combine:
			for(int ii=0; ii<clist.size(); ii++)
			{
				if(clist[ii][0] == beforec && clist[ii][1] == nowc)
				{
					rslt = rslt.substr(0,rslt.size()-1);
					rslt += clist[ii][2];
					goto loop_end;
				}
			}
		remove:
			for(int ii=0; ii<rlist.size(); ii++)
			{
				if(rlist[ii][0] == nowc)
				{
					if(rslt.find(rlist[ii][1]) != string::npos)
					{
						rslt = "";
						goto loop_end;
					}
				}
			}
		default_action:
			rslt += nowc;
		loop_end:;
		}

		cout << "Case #" << i+1 << ": [";
		for(int k=0; k<rslt.size(); k++)
		{
			cout << rslt[k];
			if(k < rslt.size()-1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
