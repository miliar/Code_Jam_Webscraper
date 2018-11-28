#include<iostream>
#include<fstream>
#include<queue>
#include<cmath>
#include<time.h>
using namespace std;

int A[3000],G[1000],shift[1000];

void init()
{
	for (int i = 0; i <= 1000 ; i++)
	{
		A[i] = 0;
		A[i+1000] = 0;
		G[i] = 0;
		shift[i] = 0;
	}
	
}

void make_table(int n , int highest)
{
	__int64 j,sum,t;
	deque<__int64> q,q1;
	for ( __int64 m = 0; m < n ; m++)
	{
		q.push_back(A[m]);
		
	}


	for ( __int64 i = 0 ; i < n ; i++)
	{
	//	que_disp(q);
		sum = q.front();
		q1.push_back(q.front());
		q.pop_front();
		
		j=1;
		while((! q.empty() )&&(sum+q.front())<=highest)
		{
			
			sum=sum+q.front();
			q1.push_front(q.front());
			q.pop_front();
			j++;
		}
		q.push_back(q1.back());
		q1.pop_back();
		G[i] = sum ;
		shift[i] = j;
		while(! q1.empty())
		{
			q.push_front(q1.front());
			q1.pop_front();
		}
	
		//cout << "A[i] : " << A[i] << " G[i] : "<< G[i] << " Shift[i] " << shift[i] << endl;
	}
	
}
__int64 func(long long unsigned int r,long long unsigned int k,long long unsigned int n)
{
	make_table(n,k);
	__int64 s=0,i=0;
	while(r!=0)
	{
		//cout << "I : " << i << "G[i] : " << G[i] << endl;
		s = s + G[i];
		i = i+ shift[i];
		i = i % n;
		r--;
	}
		

	return s;

}
int main()
{  
	
	__int64 no;
	//cout << "Answer : " << func(5,5,10);

	//cin.get();
	fstream f("a.txt",ios::in);
	fstream f2("outpu.txt",ios::out);
	
	f >> no;
	
	long long unsigned int r,k,n,i,j;
	for ( i = 1 ; i <= no ; i ++)
	{
		init();
		f >> r >> k >> n;
//		cout << "Runs : " << r << " K Persons : " << k << " N : " << n << endl;
		for ( j = 0 ; j< n; j++)
			f >> A[j];
	//	cout << "Case #"<<i<<": "<< func(r,k,n)<<endl;
		f2 << "Case #"<<i<<": "<< func(r,k,n)<<endl;
	//
		//cin.get();
	}
	f.close();
	f2.close();

	return 0;
}

