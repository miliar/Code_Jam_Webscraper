#include <iostream>
#include <vector>
#include <algorithm>
using std::vector;
using std::cin;
using std::cout;
using std::endl;
using std::sort;

unsigned Get_Max_Num(unsigned N,unsigned S,unsigned p,const vector<unsigned> &t_Vec);

int main()
{
	vector<unsigned> t_Vec,Max_Num_Vec;
	unsigned N,S,p,T,Val;

	cin>>T;
	cin.ignore(1000,'\n');
	for(unsigned i=0;i!=T;i++)
	{
		cin>>N>>S>>p;
		for (unsigned j=0;j!=N;j++)
		{
			cin>>Val;
			t_Vec.push_back(Val);
		}
		Max_Num_Vec.push_back(Get_Max_Num(N,S,p,t_Vec));
		t_Vec.clear();
	}
	for (unsigned i=0;i!=T;i++)
	{
		cout<<"Case #"<<i+1<<": "<<Max_Num_Vec[i]<<endl;
	}
	return 0;
}

unsigned Get_Max_Num(unsigned N,unsigned S,unsigned p,const vector<unsigned> &t_Vec)
{
	vector<unsigned> Arr02p;
	unsigned N1p,N02p,N02Ex,Max_Num,q,t,Best;
	N1p=0;
	N02Ex=0;
	for(unsigned i=0;i!=N;i++)
	{
		t=t_Vec[i];
		q=t%3;
		if(q==1)
		{
			Best=(t-1)/3+1;
			if(Best>=p)
				N1p++;
		}
		else
		{
			if(q==0)
			{
				if(t>=3&&t<=27)
				{
					Best=t/3+1;
					if(Best>=p)
					Arr02p.push_back(Best);
				}
				else
				{
					Best=t/3;
					if(Best>=p)
						N02Ex++;
				}
			}
			else
			{
				if (t>=2&&t<=26)
				{
					Best=(t-2)/3+2;
					if(Best>=p)
					Arr02p.push_back(Best);
				}
				else
				{
					Best=(t-2)/3+1;
					if(Best>=p)
						N02Ex++;
				}
				
			}
				
		}
	}

	N02p=Arr02p.size();
	sort(Arr02p.begin(),Arr02p.end());

	if(S>N02p)
		Max_Num=N1p+N02p+N02Ex;
	else
	{
		unsigned S1;
		S1=0;
		for (unsigned i=S;i!=N02p;i++)
		{
			if(Arr02p[i]-1>=p)
				S1++;
		}
		Max_Num=S+S1+N1p+N02Ex;
	}
	return Max_Num;
}