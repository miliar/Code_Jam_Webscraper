#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

#define FORE(i,t) for(typeof(t.begin())i=t.begin();i!=t.end();++i)

int getTime()
{
	char temp[9];
	scanf("%s",temp);
	int h,s;
	sscanf(temp,"%2d:%2d",&h,&s);
	//printf(" (%s)->(%d,%d)\n",temp,h,s);
	return h*60+s;
}

struct Train
{
	int time;
	bool covered;
	Train(int _time):
		time(_time),covered(false)
	{}
	bool operator < (const Train &t)const
	{
		return time<t.time;
	}
};

int main()
{
	int Z;
	scanf("%d",&Z);
	for(int z=1;z<=Z;++z)
	{
		printf("Case #%d: ",z);
		int t,a,b;
		scanf("%d%d%d",&t,&a,&b);
		vector<int> ain,bin;
		vector<Train> aout,bout;
		for(int i=0;i<a;++i)
		{
			int out=getTime(),in=getTime()+t;
			//printf("out=%d in=%d\n",out,in);
			aout.push_back(out);
			bin.push_back(in);
		}
		for(int i=0;i<b;++i)
		{
			int out=getTime(),in=getTime()+t;
			//printf("out=%d in=%d\n",out,in);
			bout.push_back(out);
			ain.push_back(in);
		}
		sort(aout.begin(),aout.end());
		sort(bout.begin(),bout.end());
		int ca=0,cb=0;
		FORE(i,ain)
			FORE(j,aout)
				if(j->time>=*i && !j->covered)
				{
					//printf("cover a %02d:%02d %02d:%02d\n",*i/60,*i%60,j->time/60,j->time%60);
					j->covered=true;
					++ca;
					break;
				}
		FORE(i,bin)
			FORE(j,bout)
				if(j->time>=*i && !j->covered)
				{
					//printf("cover b %02d:%02d %02d:%02d\n",*i/60,*i%60,j->time/60,j->time%60);
					j->covered=true;
					++cb;
					break;
				}
		printf("%d %d\n",a-ca,b-cb);
	}
}
