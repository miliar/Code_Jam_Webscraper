#include "iostream"
#include "fstream"
using namespace std;
int main()
{
	ifstream is;
	ofstream os;
	
	is.open("A-large.in");
	os.open("output");
	
	int cnt, c, num;
	char chr;
	
	is>>cnt;
	for(int rc=1; rc<=cnt; rc++)
	{
		is>>c;
		
		int b[100], o[100], a[100];
		int bi=0, oi=0, ai=0;
		for(int i=0; i<c; i++)
		{
			is>>chr; is>>num;
			
			if(chr == 'O') { o[oi++] = num; a[ai++] = num *-1; }
			else { b[bi++] = num; a[ai++] = num; }
		}
		
		int time = 1, bc=1, oc=1, ac=0, op =0, bp=0;
		while(1)
		{		
			int of=0, bf=0;
			if(a[ac] < 0)
			{
				if(oc == o[op]) {op++; ac++; of=1;}
			}
			else
			{
				if(bc == b[bp]) {bp++; ac++; bf=1;}
			}
			
			if(oi>0 && of==0)
			{
				if(o[op] > oc) oc++;
				if(o[op] < oc) oc--;
			}
			if(bi>0 && bf==0)
			{
				if(b[bp] > bc) bc++;
				if(b[bp] < bc) bc--;
			}
			
			if(ac >= c) break;

			time++;
			
		}
		
		//cout<<"Case #"<<rc<<": "<<time<<endl;
		os<<"Case #"<<rc<<": "<<time<<endl;
	}
	
	os.flush();

	is.close();
	os.close();
	
	return 0;
}