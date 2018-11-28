#include <iostream>
#include <fstream>
#include <queue>
#include <map>

using namespace std;
struct hz{
	long long i,mon;
};
int main()
{
	ifstream fin("input.txt");
	long long nr;
	fin >> nr;
	ofstream fout("output.txt");
	for(long long cases=1;cases<=nr;cases++)
	{
		long long R,k,N;
		fin >> R >> k >> N;
		queue <long long> q;
		map <queue <long long>,hz> m;
		for(long long i=0;i<N;i++)
		{
			long long temp;
			fin >> temp;
			q.push(temp);
		}
		hz v;
		v.i=0;
		v.mon=0;
		m.insert(make_pair(q,v));
		long long total=0;
		long long i=0;
		bool rep=false;
		while(i<R)
		{
			long long now=0;
			long long j=0;
			bool make=true;
			while ((make)&&(j<N))
			{
				long long temp=q.front();
				if (now+temp<=k)
				{
					now+=temp;
					q.pop();
					q.push(temp);
				}
				else make=false;
				j++;
			}
			total+=now;
			if ((m.find(q)==m.end())&&(!rep))
			{
				v.i=i+1;
				v.mon=total;
				m.insert(make_pair(q,v));
			}
			else
			{
				long long div=i+1-m[q].i;
				long long mo=total-m[q].mon;
				int t=R-i-1;
				t/=div;
				i+=t*div;
				total+=mo*t;
			}
			i++;
		}
		fout << "Case #" <<cases <<": " << total << endl;
	}
	return 0;
}