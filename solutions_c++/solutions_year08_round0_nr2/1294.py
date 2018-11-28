#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>

using namespace std;


int N_A=0;
int N_B=0;
int S_A=0;
int S_B=0;

int deltime;
int RUNA;
int RUNB;

class tim{
	public:
	float dat;
	bool start;
	int dir; //1,-1
	};
vector<int> AVON;
vector<int> BVON;

vector<tim> ttime;

void insertt(tim dd)
{
bool ins=true;
vector<tim>::iterator cnt=ttime.begin();
while(ins)
	{
		if(dd.dat<(*cnt).dat)
				{
				ttime.insert(cnt,dd);
				ins=false;
				}
			cnt++;
	if(cnt==ttime.end())
		{
		ttime.push_back(dd);
		ins=false;
		}

	}
}

int main()
{
FILE *myfile;

int cases;

myfile=fopen("data.dat","r");

fscanf(myfile,"%d\n",&cases);

for(int i=0; i<cases; i++)
	{
	fscanf(myfile,"%d\n",&deltime);
	fscanf(myfile,"%d %d\n",&RUNA,&RUNB);

	ttime.resize(0);
	N_A=0; N_B=0;
	S_A=0; S_B=0;
	for(int ii=0; ii<RUNA; ii++)
		{
		int t1,t2,m1,m2;
		char sw;
		fscanf(myfile,"%d:%d %d:%d\n",&t1,&m1,&t2,&m2);// >>":" >> t2;
		
		tim ta, tb;

		tb.dat=60*t1+m1;
		tb.dir=1;
		tb.start=true;
	
		ta.dat=60*t2+m2+deltime-0.01;
		ta.dir=-1;
		ta.start=false;
		
		bool ins=false;

		if(ttime.size()==0)
			{
				ttime.push_back(tb);
				ins=true;
			}
		else insertt(tb);

		insertt(ta)	;
		}

	for(int ii=0; ii<RUNB; ii++)
		{
		int t1,t2,m1,m2;
		char sw;
		fscanf(myfile,"%d:%d %d:%d\n",&t1,&m1,&t2,&m2);// >>":" >> t2;
		tim ta, tb;

		tb.dat=60*t1+m1;
		tb.dir=-1;
		tb.start=true;
	
		ta.dat=60*t2+m2+deltime-0.01;
		ta.dir=1;
		ta.start=false;
		
		bool ins=false;

		if(ttime.size()==0)
			{
				ttime.push_back(tb);
				ins=true;
			}
		else insertt(tb);

		insertt(ta);
		}
	
	for(int i3=0; i3<ttime.size(); i3++)
		{
		//cout << ttime[i3].dat/60 <<":"<< int(ttime[i3].dat)%60 << endl;
		 if(ttime[i3].start)
			{
			if(ttime[i3].dir==1)
					{
					if(N_A>0)
						N_A--;
					else
						S_A++;
					}

			if(ttime[i3].dir==-1)
					{
					if(N_B>0)
						N_B--;
					else
						S_B++;
					}

			}
		else
			{
			if(ttime[i3].dir==1)
					N_A++;

			if(ttime[i3].dir==-1)
					N_B++;

			}

		}
		cout <<"Case #"<<i+1<<": "<< S_A << " " << S_B <<endl;
	}

return 0;
}
