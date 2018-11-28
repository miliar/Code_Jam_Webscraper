#include<iostream>
#include<vector>

#define forin(i,n) for(i=1;i<=n;i++)
#define foriik(i,n) for(i=0;i<n;i++)
using namespace std;

class Googlers
{
	public :
	int q1,q2,q3,sum;
	Googlers(int a1,int a2,int a3,int num)
	{
		q1=a1;
		q2=a2;
		q3=a3;
		sum = num;
	}
};

int process(int N,int S,int P, int *t)
{
	int i,j;
	int tempS=S;
	int counter=0;
	vector<Googlers> passed;
	vector<Googlers> notyet;
	foriik(i,N)
	{
		int q1,q2,q3;
		int sum=t[i];
		q1=sum/3;
			q3=q2=q1;
			int rem = sum%3;
			if(rem==1)
			{
				q3++;
			}
			else if(rem==2)
			{
			q2++;
			q3++;
			}
		Googlers p(q1,q2,q3,sum);
		
		if(q3<P)
		{
			//cout<<q1<<","<<q2<<","<<q3<<" "<<sum<<" notyet"<<endl;
			notyet.push_back(p);
			
		}
		else
		{
			//cout<<q1<<","<<q2<<","<<q3<<" "<<sum<<" passed"<<endl;
			passed.push_back(p);
		}
	}
	
	counter = passed.size();
	foriik(i,tempS)
	{
		if(notyet.size()>i)
		{
		Googlers *temp = &notyet.at(notyet.size()-1-i);
		int sum = temp->sum;
		//cout<<sum<<endl;
		int q1,q2,q3;
		q1=(sum-2)/3;
		q3= q1+2;
		q2=sum-(q1+q3);
		//cout<<q1<<","<<q2<<","<<q3<<" "<<sum<<" notyet"<<endl;
		if(q3>=P&&sum>0)
		{
			counter++;
		}
		}
		
	}
	/*
	if(tempS>0)
	{
	
	foriik(i,tempS)
	{
		
		if(i<passed.size())
		{
		int sum = passed.at(i).sum;
		int q1,q2,q3;
		q1=(sum-2)/3;
		q3= q1+2;
		q2=sum-(q1+q3);
		
		}
		
	}
	}*/

	
	 
	return counter;
}

int compare( const void *a, const void *b)
    {
       int intOne = *((int*)a);
       int intTwo = *((int*)b);
       if (intOne < intTwo)
          return -1;
       if (intOne == intTwo)
          return 0;
       return 1;
 }

int main(int* argc, char ** argv)
{
	int test;
	cin>>test;
	int i,j,result;
	
	forin(i,test)
	{
		int N,S,P;
		cin >>N;
		cin>>S;
		cin>>P;
		int t[N];
		j=0;

		foriik(j,N)
		{
			cin>>t[j];
		}
		
		//cout<<N<<" "<<S<<" "<<P<<endl;
		
		qsort((void *)t,N,sizeof(int),compare);
		result=process(N,S,P,t);
		cout<<"Case #"<<i<<": "<<result<<endl;
	}
	
	
	
	
	return 0;
}