#include <iostream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

typedef long long int64;


vector<int64> mm;
vector<int64> nn;
vector<int64> gg;
int main()
{
	int casenum=0;
	cin>>casenum;
	for (int i=0; i<casenum; i++){
		int64 n,m,X,Y,Z;
		cin>>n>>m>>X>>Y>>Z;
		int64 temp;
		mm.clear();
		nn.clear();
		gg.clear();
		for (int j=0; j<m; j++){
			cin>>temp;
			mm.push_back(temp);
		}	
		for (int j=0; j<n; j++){
			nn.push_back(mm[j%m]);
			mm[j%m]=(X*mm[j%m]+Y*(j+1))%Z;
		}

		gg=nn;
		sort(gg.begin(),gg.end());
		vector<int64> hh(gg);
		int tt=hh[0];
		hh[0]=0;
		for (int j=1,uu=0; j<n; j++){
			if (hh[j]>tt){
				uu++;
				tt=hh[j];
				hh[j]=uu;				
			}
			else
				hh[j]=uu;
		}
		
		map<int64, int> table;
		for (int j=0; j<n; j++){
			table[gg[j]]=hh[j];
		}


		vector<int64> rest;
		for (int j=0; j<n; j++){
			rest.push_back(0);
		}

		for (int j=0; j<n; j++){
			int64 zzz=nn[j];
			int ww=table[zzz];
			rest[ww]++;
			for (int k=0; k<ww; k++){
				rest[ww]+=rest[k]%1000000007;
			}
		}

		int64 sum=0;
		for (int j=0; j<n; j++){
			sum+=rest[j]%1000000007;
		}

		cout<<"Case #"<<(i+1)<<": "<<(sum%1000000007)<<endl;
	}

	//system("pause");
	return 0;
}
