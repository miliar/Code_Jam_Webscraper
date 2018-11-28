#include <fstream>
using namespace std;
void main()
{
	int n,i,j;
	ifstream in ("input.in");
	ofstream out ("output.out");
	in >> n;
	for(int CASE=0;CASE<n;CASE++)
	{
		int ansa,ansb;
		int na,nb,t,h,m;
		char time[6];
		int dep[2][1440]={0,},arr[2][1440]={0,};
		in >> t >> na >> nb;
		for(i=0;i<na;i++)
		{
			in >> time;
			h=(time[0]-'0')*10+(time[1]-'0');
			m=(time[3]-'0')*10+(time[4]-'0');
			dep[0][h*60+m]++;
			in >> time;
			h=(time[0]-'0')*10+(time[1]-'0');
			m=(time[3]-'0')*10+(time[4]-'0');
			arr[1][h*60+m]++;
		}
		for(i=0;i<nb;i++)
		{
			in >> time;
			h=(time[0]-'0')*10+(time[1]-'0');
			m=(time[3]-'0')*10+(time[4]-'0');
			dep[1][h*60+m]++;
			in >> time;
			h=(time[0]-'0')*10+(time[1]-'0');
			m=(time[3]-'0')*10+(time[4]-'0');
			arr[0][h*60+m]++;
		}
		int a,b; a=b=ansa=ansb=0;
		for(i=0;i<1440;i++)
		{
			if(i>=t && arr[0][i-t])
				a+=arr[0][i-t];
			if(i>=t && arr[1][i-t])
				b+=arr[1][i-t];
			if(dep[0][i])
				a-=dep[0][i];
			if(a<0)
			{ ansa+=-a; a=0; }
			if(dep[1][i])
				b-=dep[1][i];
			if(b<0)
			{ ansb+=-b; b=0; }
		}
		out << "Case #" << CASE+1 << ": " << ansa << " " << ansb << endl;
	}
	out.close();
	in.close();
}