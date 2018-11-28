#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int tb[10000001];
int n;
int cal(vector<int>& vc)
{
	int b = 1;
	int res = 0;
	for(int i=0;i<vc.size();i++)
	{
		res+=b*vc[i];
		b*=10;
	}
	return res;
}
int solve(vector<int> vc)
{
	int i,j,k;
//	bool flag = false;
/*	for( i=0; i<vc.size(); i++)
	{
		for( j=i+1; j<vc.size(); j++)
		{
			if(vc[i]>vc[j])
			{
				int tmp = vc[i];
				for(k=i;k<=j-1;k++)
					vc[k]=vc[k+1];
				vc[j]=tmp;
				return cal(vc);
			}
		}
	}
	return -1; */
	for( i=0;i<vc.size();i++)
	{
		for(j=0;j<i;j++)
		{
			if(vc[i]<vc[j])
			{
				int tmp = vc[j];
				vc[j] = vc[i];
				vc[i] = tmp;
				int res = 0;
				int b = 1;
				for( int a = i-1; a>=0; a--)
				{
					res += b*vc[a];
					b*=10;
				}
				for( int c = i; c<vc.size(); c++)
				{
					res += b*vc[c];
					b*=10;
				}
				return res;
			}
		}
	}
	return -1;
}

/*void perm(vector<int>& vc)
{
	
} */
int main()
{
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("xue3.txt", "w", stdout);
	n = 0;
	vector<int> dg;
	int T;
	int i,j,cur;
	scanf("%d", &T);
	for(i=0; i<T; i++)
	{
		scanf("%d", &cur);
		int tt = cur;
		vector<int> dg;
		while(cur)
		{
			dg.push_back(cur%10);
			cur /= 10;
		}
	//	sort( dg.begin(), dg.end() );

		int res=solve(dg);
		if(res == -1)
		{
			
			vector<int> vcr;
			sort(dg.begin(), dg.end());
			if( dg[0] == 0 )
			{
			//	cout<<"Case #"<<i+1<<": "<<tt*10<<endl;
			//	cout<<"ok 1"<<endl;
				int kk = 1;
				while( dg[kk] == 0)
				{
					kk++;
				}
				int tmp1 = dg[kk];
			//	cout<<"KK:"<<kk<<endl;
			//	vector<int>::iterator it1 = dg.begin();
			//	dg[kk] = 0;
			//	dg.insert( it1, tmp1 );
				dg[0] = dg[kk];
				dg[kk] = 0;
			//	cout<<"ok ins"<<endl;
				dg.insert( dg.begin()+1, 0);
				int b = 1;
				int rs = 0;
				for(int aa = dg.size()-1; aa>=0; aa--)
				{
					rs+=b*dg[aa];
					b*=10;
				}
				cout<<"Case #"<<i+1<<": "<<rs<<endl;
			}
			else{
			vector<int>::iterator it = dg.begin();
			it++;

			dg.insert(it,0);
			
			int rs = 0;
			int b = 1;
			for(int nn = dg.size()-1; nn>=0; nn--)
			{
				rs+=b*dg[nn];
				b*=10;
			}
			cout<<"Case #"<<i+1<<": "<<rs<<endl;
			} //end else
			
		}
		else
			cout<<"Case #"<<i+1<<": "<<res<<endl;

	}

}
