#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "algorithm"
#include "map"
using namespace std;
#define UNIVERSE 1
#define TRAIN 0

#if TRAIN

class times
{
public :
		int start,end;
		bool A;
		bool operator < (times val)
		{
			return start < val.start;
		}
		bool operator <= (times val)
		{
			return start <= val.start;
		}
};

int main()
{
	ifstream ip("B-large.in");
	ofstream op("B-large.out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return -1;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return -1;
	}

	int N;
	ip>>N;

	for(int i=1;i<=N;++i)
	{
		int turn,A,B;
		ip>>turn>>A>>B;
		string starttime,endtime;
		int depA = 0,depB = 0;
		vector <times> allTimes,todepA,todepB;
		for(int aitr = 1; aitr <= A; ++aitr)
		{
			times tmp;
			ip>>starttime>>endtime;
			int time = ((starttime[0]-'0')*10+(starttime[1]-'0'))*60 + (starttime[3]-'0')*10+(starttime[4]-'0');
			tmp.start = time;
			time = ((endtime[0]-'0')*10+(endtime[1]-'0'))*60 + (endtime[3]-'0')*10+(endtime[4]-'0');
			tmp.end = time;
			tmp.A = true;
			allTimes.push_back(tmp);
		}
		for(int bitr = 1; bitr <= B; ++bitr)
		{
			times tmp;
			ip>>starttime>>endtime;
			int time = ((starttime[0]-'0')*10+(starttime[1]-'0'))*60 + (starttime[3]-'0')*10+(starttime[4]-'0');
			tmp.start = time;
			time = ((endtime[0]-'0')*10+(endtime[1]-'0'))*60 + (endtime[3]-'0')*10+(endtime[4]-'0');
			tmp.end = time;
			tmp.A = false;
			allTimes.push_back(tmp);
		}
		sort(allTimes.begin(),allTimes.end());

		for(int idx = 0;idx < allTimes.size(); ++idx)
		{
			times tmp = allTimes[idx];
			if(tmp.A)
			{
				int aidx = 0;
				bool found = false;
				for(; aidx < todepA.size(); ++aidx)
					if(todepA[aidx] <= tmp)
					{
						todepA.erase(todepA.begin()+aidx);
						found = true;
						break;
					}
				times tmpb ;
				tmpb.start = tmp.end+turn;
				todepB.push_back(tmpb);
				if(!found)
					++depA;
			}
			else
			{
				int bidx = 0;
				bool found = false;
				for(; bidx < todepB.size(); ++bidx)
					if(todepB[bidx] <= tmp)
					{
						todepB.erase(todepB.begin()+bidx);
						found = true;
						break;
					}
				times tmpa ;
				tmpa.start = tmp.end+turn;
				todepA.push_back(tmpa);				
				if(!found)
					++depB;
			}
		}
		op<<"Case #"<<i<<": "<<depA<<" "<<depB<<endl;
	}
	ip.close();
	op.close();
}
#endif 
#if UNIVERSE
int main()
{
	ifstream ip("A-large.in");
	ofstream op("A-large.out");

	if(!ip)
	{
		cout<<"Cant open input file";
		return -1;
	}
	if(!op)
	{
		cout<<"Cant open output file";
		return -1;
	}

	int N;
	ip>>N;

	for(int i=1;i<=N;++i)
	{
		int Servers;
		int retval = 0;
		string servername;
		vector< string > serverlist;
		vector< string > querylist;
		
		ip>>Servers;
		getline(ip,servername);
		for(int srvidx = 1; srvidx <= Servers; ++srvidx)
		{
			getline(ip,servername);
			serverlist.push_back(servername);
		}

		ip>>Servers;
		getline(ip,servername);
		for(int qridx = 1; qridx <= Servers; ++qridx)
		{
			getline(ip,servername);
			querylist.push_back(servername);
		}

		int queryidx = 0;
		while(1)
		{
			vector <string> tmpserv;
			for(int mainidx = 0; mainidx < serverlist.size(); ++mainidx)
				tmpserv.push_back(serverlist[mainidx]);
			while((tmpserv.size()) && (queryidx < querylist.size()))
			{
				vector <string>::iterator itr = find(tmpserv.begin(),tmpserv.end(),querylist[queryidx]);
				++queryidx;
				if(tmpserv.end() != itr)
					tmpserv.erase(itr);
			}
			if(tmpserv.empty())
			{
				++retval;
				--queryidx;
			}
			if(queryidx == querylist.size())
				break;
		}
		op<<"Case #"<<i<<": "<<retval<<"\n";
	}
	ip.close();
	op.close();
}
#endif
