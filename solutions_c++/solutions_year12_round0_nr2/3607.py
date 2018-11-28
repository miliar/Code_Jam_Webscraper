#include<iostream>

using namespace std;

bool nonSurprising(int a,int p)
{
	if((3*p-2)==a)
	{
		return true;
	}
	if((3*p-1)==a)
	{

		return true;
	}
	return false;
}


bool surprising(int a, int p)
{
	if((3*p-4)==a)
	{
	return true;
	}
	if((3*p-3)==a)
	{
	 return true;
	}
	return false;
}


int main()
{
int cases,N,S,P,caseno=1;
cin>>cases;
while(cases--)
{
	cin>>N;
	cin>>S;
	cin>>P;
	int t[N],count=0;
	for(int i=0; i<N ; i++)
	{
		cin>>t[i];
	}
	
	for(int i=0; i< N ; i++)
	{
		int x=t[i]/3;
		if(t[i]==0 && P==0) 
		{
			count++;
			continue;
		}
		else if( t[i]==0 && P!=0)
		{
			continue;
		}

		if(x>=P)
		{
			count++;
		}
		else 
		{
			if(nonSurprising(t[i],P))
			{
				count++;
			}
			else if(S>0)
			{
				if(surprising(t[i],P))
				{
					count++;
					S--;
				}
			}
		}


	}
	cout<<"Case #"<<caseno<<": "<<count<<endl;
	caseno++;
}

return 0;
}

