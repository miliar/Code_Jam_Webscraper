#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
	int T;
	cin>>T;

	for (int i=0;i<T;i++){
		int N;
		cin>>N;

		int tsum=0;

		int pospre[2]={1,1};

		int ob;
		int obpre;
		char OB=0;

		int t=0;

		for (int j=0;j<N;j++){
			int pos;
			cin>>OB;
			cin>>pos;

			if (OB=='O') ob=1;
			else ob=0;

			if (j==0) obpre=ob;

			if (ob!=obpre){
				tsum+=t;
				int tmp=abs(pos-pospre[ob]);
				if (tmp<=t) pospre[ob]=pos;
				else{
					if (pos>pospre[ob]) pospre[ob]+=t;
					else pospre[ob]-=t;
				};
				t=0;
			}
			
			t+=abs(pos-pospre[ob])+1;
			pospre[ob]=pos;

			obpre=ob;
		}
		tsum+=t;

		cout<<"Case #"<<i+1<<": "<<tsum<<endl;
	}

	return 0;
}
