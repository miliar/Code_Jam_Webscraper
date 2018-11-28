#include <boost/date_time/posix_time/posix_time.hpp>
#include <boost/date_time/posix_time/posix_time_types.hpp>
#include <iostream>
#include <set>
using namespace std;
using namespace boost::posix_time;
typedef pair<time_duration,time_duration> ParaTime ;
void RozwiazTest(int);

int main()
{
	int N;
	scanf("%d\n",&N);
	for(int i=0;i<N;i++) RozwiazTest(i+1);
	return 0;
}
void RozwiazTest(int k)
{
	int na,nb,T;
	scanf("%d",&T);
	scanf("%d %d\n",&na,&nb);
	ParaTime A[na],B[nb];
	set<ParaTime> s[2];
	for(int i=0;i<na;i++)
	{
		string time1,time2;
		cin>>time1>>time2;
		time1+=string(":00");
		time2+=string(":00");
		s[0].insert(make_pair(duration_from_string(time1),duration_from_string(time2) + minutes(T)));
	}
	for(int i=0;i<nb;i++)
	{
		string time1,time2;
		cin>>time1>>time2;
		time1+=string(":00");
		time2+=string(":00");
		s[1].insert(make_pair(duration_from_string(time1),duration_from_string(time2) + minutes(T)));
	}
/*	if(k==1)
	{
	cout<<"===========Test "<<k<<"==========="<<endl;
	for(set<ParaTime>::iterator i=s[0].begin();i!=s[0].end();i++)
		cout<<i->first<<" "<<i->second<<endl;
	cout<<"----------------------------------"<<endl;
	for(set<ParaTime>::iterator i=s[1].begin();i!=s[1].end();i++)
		cout<<i->first<<" "<<i->second<<endl;
	}*/
	int count[2];
	count[0]=0;
	count[1]=0;
	while(!s[0].empty() || !s[1].empty())
	{
		int i=0;
		if(!s[0].empty() && !s[1].empty()) 
		{
			if( *s[0].begin()>*s[1].begin()) i=1;
		}
		else if(!s[1].empty()) i=1;

		set<ParaTime>::iterator it=s[i].begin();
		count[i]++;
		while(it!=s[i].end())
		{
			ParaTime pt=*it;
//			if(k==1)cout<<"lower_bound["<<i<<"]= "<<pt.first<<"  "<<pt.second<<endl;
			pt.first=pt.second;
			pt.second=time_duration(0,0,0,0);
			s[i].erase(it);
			i+=1;i%=2;
			it=s[i].lower_bound(pt);
//			cout<<"pt="<<pt.first<<"  "<<pt.second<<endl;
		}
	}
	printf("Case #%d: %d %d\n",k,count[0],count[1]);
}
