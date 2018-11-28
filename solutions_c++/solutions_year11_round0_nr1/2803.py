#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define BLUE 0
#define ORANGE 1
#define COLOR 1
#define POS 0

int target[2][100];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int k;
	cin>>k;

	for(int i=0;i<k;i++){
		int n;
		cin>>n;

		for(int j=0;j<n;j++){
			int b;
			char c;
			cin>>c>>b;
			target[POS][j]=b;
			target[COLOR][j]=(c=='O'?ORANGE:BLUE);
		}

		int time=0;
		int currstep=0;

		int oaimpos;
		int baimpos;
		int ocurrpos=1;
		int bcurrpos=1;
		while(currstep<n){
			if(target[COLOR][currstep]==BLUE){
				baimpos=target[POS][currstep];

				int det=abs(bcurrpos-baimpos)+1;
				bcurrpos=baimpos;
				time+=det;

				int k=currstep;
				while(target[COLOR][k]!=ORANGE&&k<n)k++;
				oaimpos=target[POS][k];

				if(det>=abs(ocurrpos-oaimpos))
					ocurrpos=oaimpos;
				else{
					if(ocurrpos>oaimpos)ocurrpos-=det;
					else ocurrpos+=det;
				}
			}else{
				oaimpos=target[POS][currstep];

				int det=abs(ocurrpos-oaimpos)+1;
				ocurrpos=oaimpos;
				time+=det;

				int k=currstep;
				while(target[COLOR][k]!=BLUE&&k<n)k++;
				baimpos=target[POS][k];

				if(det>=abs(bcurrpos-baimpos))
					bcurrpos=baimpos;
				else{
					if(bcurrpos>baimpos)bcurrpos-=det;
					else bcurrpos+=det;
				}
			}
			currstep++;
		}

		cout<<"Case #"<<i+1<<": "<<time<<endl;
	}

	return 0;
}