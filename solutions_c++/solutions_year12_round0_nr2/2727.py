#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int T,N,S,p,i,j,k,flag=0,lendata;
	int *score,count;
	ifstream ip("B-small-attempt4.in");
	ofstream op("write.txt");
	ip>>T;
	for(i=0;i<T;i++)
	{
		ip>>N;
		ip>>S;
		ip>>p;
		count=0;
		score=new int[N];
		for(j=0;j<N;j++)
			ip>>score[j];
		if(p==0)
			count=N;
		else{
		for(j=0;j<N;j++)
		{
			if(score[j]>(p*3-3) && score[j]>0)
			{
				count++;
			}
			else if(S>0 && score[j]>=(p*3-4) && score[j]>0)
			{
				count++;
				S--;
			}
		}
		}
		delete score;
		op<<"Case #"<<i+1<<": "<<count<<endl;
	}
	ip.close();
	op.close();
	return 0;
}
