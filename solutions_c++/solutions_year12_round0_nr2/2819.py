#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
	//freopen("test.in", "rt", stdin);
	freopen("bs.in", "rt", stdin);
	freopen("bs.out","wt", stdout);

	int nCases;
	cin>>nCases;
	for (int nCase=1;nCase<=nCases;nCase++) {
		cout<<"Case #"<<nCase<<": ";

		int nGooglers,nSurp,minBest;
		int totals[100];
		cin>>nGooglers>>nSurp>>minBest;		
		for (int i=0;i<nGooglers;i++)
			cin>>totals[i];

		int res=0;
		
		for (int iGoogler=0;iGoogler<nGooglers;iGoogler++)
			if (totals[iGoogler]%3==0) {
				if ((int)(totals[iGoogler]/3)>=minBest)
					res++;
				else if (nSurp>0 && (int)(totals[iGoogler]/3)+1==minBest 
					&& (int)(totals[iGoogler]/3)+1<=10 && (int)(totals[iGoogler]/3)-1>=0) {
					res++;
					nSurp--;
				}
			} else if (totals[iGoogler]%3==1) {
				if ((int)(totals[iGoogler]/3)+1>=minBest)
					res++;
			} else if (totals[iGoogler]%3==2) {
				if ((int)(totals[iGoogler]/3)+1>=minBest)
					res++;
				else if (nSurp>0 && (int)(totals[iGoogler]/3)+2==minBest
					&& (int)(totals[iGoogler]/3)+2<=10) {
					res++;
					nSurp--;
				}
			}

		cout<<res<<endl;
	}

	return 0;
}
