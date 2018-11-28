#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
bool now[1000];
int main(){
	freopen("1.in","r",stdin);
	freopen("11.out","w",stdout);
	
	int T,n,i,TC=0;
	scanf("%d",&T);
	while(T--){TC++;
		scanf("%d",&n);
		vector<int > o,b;
		for(i=0;i<n;i++){
			char tem[10];
			int temp;
			scanf("%s%d",tem,&temp);
			if(tem[0] == 'O')o.push_back(temp);
			else b.push_back(temp);
			now[i]=(tem[0] == 'O');
		}
		int no,nb,neo,neb,so,sb;
		no=nb=1;
		neo=neb=i=0;
		so= o.size();sb=b.size();
		int ans=0;
		while(i<n){
			ans++;
			bool flag=0;
			if(neo<so){
				if(now[i] && o[neo] == no)neo++,flag=1;//,printf("p\t");
				else if(o[neo] < no) no--;//,printf("d\t");
				else if(o[neo] > no) no++;//,printf("u\t");
			}
			if(neb<sb){
				if(!now[i] &&b[neb] == nb)neb++,flag=1;//,printf("p\n");
				else if(b[neb] < nb) nb--;//,printf("d\n");
				else if(b[neb] > nb) nb++;//,printf("u\n");
			}
			if(flag)i++;
			//printf("\n");
		}
		printf("Case #%d: %d\n",TC,ans);
	}
}
