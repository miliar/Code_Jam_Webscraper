#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath> 
using namespace std;
long max(long a,long b)
{
	return a>b?a:b;
}
void main(){
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
	long n,i,j,k,l;
	cin>>n;
	for(l=0;l<n;l++)
	{
		vector<long> o,b;
		cin>>k;
		vector<bool> p(k);
		for(i=0;i<k;i++)
		{
			char c;
			cin>>c>>j;
			if(c=='O'){
				o.push_back(j);
				p[i]=true;
			}
			else{
				b.push_back(j);
				p[i]=false;
			}
		}
		o.push_back(0); b.push_back(0);
		long poso=1,posb=1,lasts=0,nexto=0,nextb=0;
		bool lastr=p[0];
		long long time=0;
		for(i=0;i<k;i++)
		{
			if(lastr==p[i]){
				if(p[i])
				{
					time+=abs(poso-o[nexto])+1;
					lasts+=abs(poso-o[nexto])+1;
					nexto++;
					poso=o[nexto-1];
				}
				else{
					time+=abs(posb-b[nextb])+1;
					lasts+=abs(posb-b[nextb])+1;
					nextb++;
					posb=b[nextb-1];
				}
			}
			else{
				if(p[i]){
					time+=max(-lasts+abs(poso-o[nexto]),0)+1;
					lasts=max(-lasts+abs(poso-o[nexto]),0)+1;
					nexto++;
					poso=o[nexto-1];
					lastr=true;
				}
				else{
					time+=max(-lasts+abs(posb-b[nextb]),0)+1;
					lasts=max(-lasts+abs(posb-b[nextb]),0)+1;
					nextb++;
					posb=b[nextb-1];
					lastr=false;
				}
			}
		}
		cout<<"Case #"<<l+1<<": "<<time<<endl;
	}
}