#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream in("B-large.in");
	ofstream out("B-large.out");
	int t,i;
	in >> t;
    for(i=0;i<t;i++)
    {
        int j,n,s,p;
		int t[100]={};
		in >> n >> s >> p;
		for(j=0;j<n;j++)
			in >> t[j];
		int ans=0;
		for(j=0;j<n;j++)
		{
			int ave=t[j]/3,rem=t[j]%3;
			if(rem==0)
			{
				if(ave>=p) ans++;
				else if(ave==p-1 && ave>0 && s>0)
				{
						s--;
						ans++;
				}
			}
			else if(rem==1)
			{
				if(ave>=p-1) ans++;
			}
			else
			{
				if(ave>=p-1) ans++;
				else if(s>0 && ave==p-2)
				{
					s--;
					ans++;
				}
			}
		}
		out << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
