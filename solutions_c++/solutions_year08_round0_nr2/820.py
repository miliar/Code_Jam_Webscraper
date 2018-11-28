#include<iostream>
#include<vector>
#include<cstdio>
#include<cstdlib>
using namespace std;

typedef struct schedule{
	int start;
	int finish;
	bool flag;
}schedule;

int cmp(const void *a, const void *b)
{
	schedule *s1=(schedule*)a;
	schedule *s2=(schedule*)b;

	if (s1->start > s2->start)
		return 1;
	else if(s1->start == s2->start)
	{
		return(s1->finish >s2->finish);
	}
		return -1;
}


int main()
{
	int num_cases=0;
	cin>>num_cases;
	for(int i=0;i<num_cases;i++)
	{
		int T,NA,NB,temp;
		schedule *S;
		char c;
		cin>>T;
		cin>>NA>>NB;
		int total=NA+NB;
		S=new schedule[total];
		vector< vector<int> > available;
		vector<int > ja,jb;
			available.push_back(ja);	
			available.push_back(jb);	
		int train[2];
		train[0]=train[1]=0;	
		for(int j=0;j<NA;j++)
		{
			S[j].start=0;
			S[j].finish=0;
			cin>>temp;
			S[j].start+=(60*temp);
			cin>>c;
			cin>>temp;
			S[j].start+=temp;

			cin>>temp;
			S[j].finish+=(60*temp);
			cin>>c;
			cin>>temp;
			S[j].finish+=temp;

			S[j].flag=false;
		}


		for(int j=NA;j<total;j++)
		{
			S[j].start=0;
			S[j].finish=0;
			cin>>temp;
			S[j].start+=(60*temp);
			cin>>c;
			cin>>temp;
			S[j].start+=temp;


			cin>>temp;
			S[j].finish+=(60*temp);
			cin>>c;
			cin>>temp;
			S[j].finish+=temp;

			S[j].flag=true;
		}

		qsort(S,total,sizeof(schedule),cmp);
		for(int j=0;j<total;j++)
		{

			int size=0,deadline;
			bool f=S[j].flag;
			
			if((available[f]).empty())
			{
				train[f]++;
			}
			else
			{
				vector<int > dummy =available[f];
				size=dummy.size();	
				deadline=(S[j]).start;
				if(dummy[0]<=deadline)
				{
					(available[f]).erase((available[f]).begin());
				}
				else
					train[f]++;
			}

			if((available[!f]).empty())
			{
				(available[!f]).push_back(S[j].finish+T);
			}

			else
			{
				deadline=(S[j]).finish+T;
				vector<int > dummy =available[!f];
				size=dummy.size();	
				if(dummy[size-1]<=deadline)
				{
					(available[!f]).push_back(deadline);
				}
				else
				{			
					for(int k=0;k<size;k++)
					{
						if(deadline< dummy[k])
						{
							vector<int>::iterator p=(available[!f]).begin();
							(available[!f]).insert(p+k,deadline);
							break;	
						}

					}
				}
			}

		}

		cout<<"Case #"<<i+1<<": "<<train[0]<<" "<<train[1]<<'\n';
	}
		
return(0);
}

