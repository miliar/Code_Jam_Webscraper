#include<iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int I=1; I<=T; I++)
	{
		int count=0;

		int N;
		cin >> N;
		int S;
		cin >> S;
		int p;
		cin >> p;
		int scores[100];
		for(int i=0; i<N; i++)
		{
			int temp;
			cin >> temp;
			scores[i] =temp;
		}
	
		for(int i=0; i<N; i++)
		{
			
			if((scores[i]) >= 3*p)
			{
				count++;
			}
			else
			{
				//two ps and 1 p-1
				
				if(scores[i] >= (2*p + (p-1)))
				{
					count++;
				}
				else if(scores[i] >= (p + 2*(p-1)))	//one p and 2 p-1
				{
					count++;
				}
				else if((S>=1) &&(p>1) && (scores[i] >= (p + 2*(p-2))))	//one p and 2 p-2 (s-1)
				{
					S--;
					count++;
				}
				else if((S>=1) && (p>1)&& (scores[i] >= (2*p + p-2)))//two p and 1 p-2 (s-1)
				{
					S--;
					count++;
				}
			}

		}

		cout <<"Case #" << I << ": " <<count << endl;
	}

}	
