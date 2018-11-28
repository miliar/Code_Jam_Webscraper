#include <iostream>

using namespace std;
typedef long long llong;

int n;
int e;
int hl[100][2];
int w[100][2];
int hlp[2];

int main(){
	int NN;cin>>NN;
	for(int MM=1;MM<=NN;MM++){
		cin>>n;
		hlp[0]=hlp[1]=0;
		for(int i=0;i<n;i++){
			char c;int t;
			cin>>c>>t;
			hl[hlp[c=='O']][c=='O']=t;
			w[hlp[c=='O']++][c=='O']=i;
		}
		e=0;
		int p[2]={1,1};
		int hp[2]={0,0};
		int l=0;
		while(l<n){
			int nn[2] = {1001,1001};
			for (int k=0;k<2;k++)
				if (hp[k]<hlp[k])
					if(l==w[hp[k]][k]&&hl[hp[k]][k]==p[k])
						nn[k]=1000;
					else
						nn[k]=hl[hp[k]][k]==p[k]?1001:hl[hp[k]][k]-p[k];
			int ee=min(abs(nn[0]),abs(nn[1]));
			if(nn[0]==1000||nn[1]==1000)
				ee=1;
			for (int k=0;k<2;k++)
				if(nn[k]==1000) {
					l++;
					hp[k]++;
				} else if (nn[k]<1000) {
					p[k]+=ee*(nn[k]>0?1:-1);
				}
			e+=ee;
		}

		cout<<"Case #"<<MM<<": "<<e<<endl;
	}
	return 0;
}