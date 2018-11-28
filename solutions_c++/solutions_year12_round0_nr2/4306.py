#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cmath>

using namespace std;

int flag;

class googler
	{
	public:
	int total;
	int scores[2];
	void update()
		{
		if (total%3==0)
			{
			scores[0]=total/3;
			scores[1]=scores[0]+1;
			}
		else if (total%3==1)
			scores[0]=scores[1]=floor(total/3)+1;
		else
			{
			scores[0]=1+(total/3);
			scores[1]=1+scores[0];
			}
		if (total>28||total<2)
			scores[1]=-1;	
		}
	};

		

int main()
	{
	googler a[100];
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.in");
	int T,n;
	fin>>T;
	for (int t=0;t<T;++t)
		{
		int N, S, p, B=0, u=0;
		int max=0;
		fin>>N;
		fin>>S;
		fin>>p;
		for (n=0; n<N; ++n)
			{
			fin>>a[n].total;
			a[n].update();
			if (a[n].scores[0]>=p)
				B++;
			else if (a[n].scores[1]>=p)
				u++;
			}
		int tot1=((u+B)>S)?S:(u+B);
		max+=tot1;
		if (tot1>u)
			{
			u=0;
			tot1-=u;
			}
		else
			{
			tot1=0;
			}
		int downs=B-tot1;
		int tot2=(downs>(N-S))?(N-S):downs;
		max+=tot2;		
		fout<<"Case #"<<t+1<<": "<<max<<"\n";
	}
	fin.close();
	fout.close();
	return 0;
	}	
