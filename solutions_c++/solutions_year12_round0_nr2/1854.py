#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int n, s, p;
int scores[105];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int t;
	cin>>t;
	for(int Ci = 1; Ci<=t; Ci++)
	{
		cin>>n>>s>>p;
		for(int i=0; i<n; i++)
			cin>>scores[i];
		sort(scores, scores+n);
		int res = 0;
		for(int i=0; i<n; i++)
		{
			if((scores[i]+4)/3 < p)
				continue;
			if(scores[i]%3==0 && scores[i]/3>=p)
				res ++;
			else if(scores[i]>=2 && (scores[i]+1)%3==0 && (scores[i]+1)/3 >= p)
				res++;
			else if(scores[i]>=1 && (scores[i]+2)%3 ==0 && (scores[i]+2)/3 >= p)
				res++;
			else if(scores[i]>=3 && (scores[i]+3)%3==0 && (scores[i]+3)/3 >= p && s>0){
				res ++;
				s --;
			}
			else if(scores[i]>=2 && (scores[i]+4)%3==0 && (scores[i]+4)/3 >= p && s>0 ){
				res ++;
				s --;
			}
		}
		cout<<"Case #"<<Ci<<": "<<res<<endl;
	}
	return 0;
}