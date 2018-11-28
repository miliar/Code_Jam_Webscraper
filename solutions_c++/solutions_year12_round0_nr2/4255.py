#include <iostream>

using namespace std;

int main(void)
{
	int t,n,s,p,exp_score,sur_score;
	cin>>t;
	for (int i=0;i<t;i++)
	{
		int ans=0;
		cin>>n>>s>>p;
		int score[n];
		for(int j=0;j<n;j++)
			cin>>score[j];
		if(p>=2)	
		{
			exp_score=p+2*(p-1);
			sur_score=p+2*(p-2);
		}
		else if (p==1)
		{
			exp_score=1;
			sur_score=1;		
		}
		else
		{
			exp_score=0;
			sur_score=0;
		}
		
		for(int j=0;j<n;j++)
		{
			if(score[j]>=exp_score)
				ans++;
			else if(score[j]>=sur_score && s>0)
			{
				ans++;
				s--;
			}	
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
