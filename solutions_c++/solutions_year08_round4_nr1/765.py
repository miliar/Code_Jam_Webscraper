#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;


int bv[10001],isc[10001],gt[10001];
int N,M,V;


int rek (int nod, int co)
{
	int wyn=0,sw1,sw2;
	if(co==bv[nod])return 0;
	if(nod>(M-1)/2)return -1;
	if(co==1){
		if(gt[nod]==1){
			if(isc[nod]){
				wyn+=1;
				sw1=rek(nod*2,1);
				sw2=rek(nod*2+1,1);
				if(sw1==-1)
					if(sw2==-1) wyn=-1;
					else wyn+=sw2;
				else
					if(sw2==-1) wyn+=sw1;
					else wyn+=min(sw1,sw2);
			}else{
				sw1=rek(nod*2,1);
				sw2=rek(nod*2+1,1);
				if(sw1==-1 || sw2==-1)wyn=-1;
				else wyn+=sw1+sw2;
			}
		}else{
			sw1=rek(nod*2,1);
			sw2=rek(nod*2+1,1);
				if(sw1==-1)
					if(sw2==-1) wyn=-1;
					else wyn+=sw2;
				else
					if(sw2==-1) wyn+=sw1;
					else wyn+=min(sw1,sw2);
		}
	}else{
		if(gt[nod]==0){
			if(isc[nod]){
				wyn+=1;
				sw1=rek(nod*2,0);
				sw2=rek(nod*2+1,0);
				if(sw1==-1)
					if(sw2==-1) wyn=-1;
					else wyn+=sw2;
				else
					if(sw2==-1) wyn+=sw1;
					else wyn+=min(sw1,sw2);
			}else{
				sw1=rek(nod*2,0);
				sw2=rek(nod*2+1,0);
				if(sw1==-1 || sw2==-1)wyn=-1;
				else wyn+=sw1+sw2;
			}
		}else{
			sw1=rek(nod*2,0);
			sw2=rek(nod*2+1,0);
				if(sw1==-1)
					if(sw2==-1) wyn=-1;
					else wyn+=sw2;
				else
					if(sw2==-1) wyn+=sw1;
					else wyn+=min(sw1,sw2);
		}
	}
	return wyn;
}

int main()
{
  int i,j,k,l,m,wyn;
  cin>>N;
  for(i=1;i<=N;i++)
  {
	wyn=0;
	cin>>M;cin>>V;
	for(j=1;j<=(M-1)/2;j++)
		{cin>>gt[j];cin>>isc[j];}
	for(j=(M-1)/2+1;j<=M;j++) cin>>bv[j];
	for(j=(M-1)/2;j>0;j--)if(gt[j])if(bv[2*j] && bv[2*j+1])bv[j]=1;else bv[j]=0; else if(bv[2*j] || bv[2*j+1]) bv[j]=1; else bv[j]=0;

	wyn=rek(1,V);

	if(wyn!=-1) cout<<"Case #"<<i<<": "<<wyn<<endl;
	else cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
  }

  return 0;
}
