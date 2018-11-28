#include <iostream>
#include <deque>
using namespace std;
deque <int> q;
int main()
{
//	freopen("d:\\gj\\C-small-attempt0.in","r",stdin);
//	freopen("d:\\gj\\bos.txt","w",stdout);
	int ri,rp;
	int k,r,n,i,tp,l,ans;
	cin>>rp;
	for (ri=0;ri<rp;ri++)
	{
		cin>>k>>r>>n; ans=0;
		q.clear();

		for (i=0;i<n;i++)
		{
			cin>>tp;
			q.push_back(tp);
		}
		for (i=0;i<k;i++)
		{
			int c=n;
			l=r;
			while (l>0 && c>0)
			{
				tp=q.front();
				l-=tp;
				c--;
				if (l>=0) 
				{
					ans+=tp;
					q.pop_front();
					q.push_back(tp);
				}
			}
		//	cout<<ans<<endl;
		}
		cout<<"Case #"<<ri+1<<": "<<ans<<endl;
	}
	return 0;
}

