#include <string>
#include <fstream>
#include <vector>
using std::ofstream;
using std::ifstream;
using std::vector;
using std::string;
using std::iterator;
ofstream out;
ifstream in;
struct SE
{
	string SearchEngine;
	vector<int> OccurrencePosition;
};

void locate(string query, int position,vector<SE> &SearchEngine)
{
	for(vector<SE>::iterator p=SearchEngine.begin();p!=SearchEngine.end();p++)
	{
		if(query==p->SearchEngine)
		{
			p->OccurrencePosition.push_back(position);
			break;
		}
	}

}
int main()
{

	//vector<string> Queries;
	int N=0,S=0,Q=0;
	in.open("input.txt");
	in>>N;
	for(int casenum=1;casenum<=N;++casenum)
	{
		in>>S;
		vector<SE> SearchEngine;
		SE tempS;
		getline(in,tempS.SearchEngine);
		for(int i=0;i<S;++i)
		{
			SE temp;
			getline(in,temp.SearchEngine);
			SearchEngine.push_back(temp);
		}
		in>>Q;
		if(Q==0)
		{
			out.open("output.txt",std::ios::app);
			out<<"Case #"<<casenum<<": "<<0<<std::endl;
			out.close();
			continue;
		}
		string tempQ;
		getline(in,tempQ);
		for(int i=0;i<Q;++i)
		{
			string temp;
			getline(in,temp);
			locate(temp,i,SearchEngine);
		}

		for(vector<SE>::iterator p=SearchEngine.begin();p!=SearchEngine.end();p++)
		{
			p->OccurrencePosition.push_back(-1);
		}
		int max=0,counter=0, flag=0,location=0,newlocation=0;
		for(int i=0;i<S;++i)
		{
			if(SearchEngine.at(i).OccurrencePosition[counter]==-1)
			{
				flag=1;
				break;
			}
			if(max<SearchEngine.at(i).OccurrencePosition[counter])
			{
				max=SearchEngine.at(i).OccurrencePosition[counter];
				location=i;
			}
		}
		while(flag==0)
		{
			int newmax=max;
			++counter;
			for(int i=0;i<S;++i)
			{
				if(i==location)
					continue;
				if(flag==1)
					break;
				for(int j=1;j<SearchEngine.at(i).OccurrencePosition.size();++j)
				{
					if(SearchEngine.at(i).OccurrencePosition[j]==-1)
					{
						flag=1;
						break;
					}
					else if(max<SearchEngine.at(i).OccurrencePosition[j])
					{
						if(newmax<SearchEngine.at(i).OccurrencePosition[j])
						{
							newmax=SearchEngine.at(i).OccurrencePosition[j];
							newlocation=i;
						}
						break;
					}
				}
			}
			location=newlocation;
			max=newmax;
		}
		/*if(max==Q-1)
		{
			++counter;
		}*/
		out.open("output.txt",std::ios::app);
		out<<"Case #"<<casenum<<": "<<counter<<std::endl;
		out.close();
	}
	in.close();
}