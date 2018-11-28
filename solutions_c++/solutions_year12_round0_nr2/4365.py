#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
using namespace std;


int main(int argc, char ** argv)
{
	int T;
	cin>>T;
	int* answers = new int[T];
	for(int i=0;i<T;i++)
	{
		int N;
		cin>>N;
		int* totals = new int[N];
		int s;
		cin>>s;
		int p;
		cin>>p;
		for(int j=0;j<N;j++)
		{
			cin>>totals[j];
		}
		int answer = 0;
		int temp = s;
		for(int j=0;j<N;j++)
		{
			if(totals[j]>30)
			{
				return 0;
			}
			int quo = totals[j]/3;
			int rem = totals[j] - quo*3;
			if(p > 10)
			{
				break;
			}
			if(p == (quo+2))
			{
				if(temp>0 and rem == 2)
				{
					answer++;
					temp--;
				}
			}
			else if(p == (quo+1))
			{
				if(rem >0)
				{
					answer++;
				}
				if(rem == 0 and quo>0 and temp>0)
				{
					answer++;
					temp--;
				}
			}
			else if(p < (quo+1))
			{
				answer++;
			}
		}
		answers[i] = answer;
	}
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": "<<answers[i]<<endl;
	}		
	return 0;
}
