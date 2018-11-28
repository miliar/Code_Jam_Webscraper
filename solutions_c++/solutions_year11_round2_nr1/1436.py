#include<iostream>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

int main()
{
    int T,totalcase;
    cin>>T;
    totalcase=T;
    
    while(T)
    {
		int n;
		cin>>n;
		
		vector<vector<char> > mat;
		vector<pair<int,int> > wl;
		vector<double> owp;
		vector<double> wp;
		vector<double> oowp;
		
		for(int i =0;i<n;i++)
		{
			vector<char> row;
			int w=0,l=0;
			for(int j=0;j<n;j++)
			{
				char k;
				cin>>k;
				row.push_back(k);
				if(k=='1')
					w++;
				else if(k=='0')
					l++;
			}
			wl.push_back(make_pair(w,l));
			wp.push_back((double)((double)(w)/(double)(w+l)));
			mat.push_back(row);
		}
		
		for(int i=0;i<n;i++)
		{
			//vector<double> owpb;
			double owpbsum=0;
			int owpbcount=0;
			for(int j=0;j<n;j++)
			{
				if(mat[i][j]=='1')
				{
					owpbsum += ((double)((double)wl[j].first)/(double)(wl[j].second-1+wl[j].first));
					owpbcount++;
				}
				else if(mat[i][j]=='0')
				{
					owpbsum += ((double)((double)(wl[j].first-1))/(double)(wl[j].second+wl[j].first-1));
					owpbcount++;
				}
			}
			owp.push_back(owpbsum/owpbcount);
		}
		
		for(int i=0;i<n;i++)
		{
			double oowpsum=0;
			int oowpcount=0;
			for(int j=0;j<n;j++)
			{
				if(mat[i][j]!='.')
				{
					oowpsum+= owp[j];
					oowpcount++;
				}
			}
			oowp.push_back(oowpsum/oowpcount);
		}
		
		cout<<"Case #"<<totalcase-T+1<<":"<<endl;
		for(int i=0;i<n;i++)
		{
			double res = ((0.25 * (wp[i])) + (0.50 * (owp[i])) + (0.25 * (oowp[i])));
			cout<<res<<endl;
		}
            
            T--;
    }
    
    return 0;
    
}
