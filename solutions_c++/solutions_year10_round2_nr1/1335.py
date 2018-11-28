#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
using namespace std;
#define M 100
map<string,int> sou;
string mid1[M+5];
string mid2[M+5];
int net[M*10+5][M*10+5];
int n,m;

int main(){
    freopen("A-small-attempt5.in","rb",stdin);
	freopen("A-small-attempt5.out","wb",stdout);
	int ca,i,j,k,c=0;
	scanf("%d",&ca);
	while(ca--){
		sou.clear();
		c++;
		int res=0;
		scanf("%d%d",&n,&m);
		memset(net,0,sizeof(net));

		for(i=0;i<n;i++){
			cin>>mid1[i];
			mid1[i]+="/";
		}
		for(i=0;i<m;i++){
			cin>>mid2[i];
			mid2[i]+="/";
		}
		sou[" "]=1;
		int total=1;

		for(i=0;i<n;i++){
			int fa=1;
			int child=0;
			string temp;
			for(j=1;j<mid1[i].length();j++){
				temp.append(1,mid1[i][j]);
				if(mid1[i][j]=='/'){
					//cout<<temp<<endl;
					if(sou[temp]==0){
						total++;
						sou[temp]=total;
					}
					child=sou[temp];
					net[fa][child]=1;

					fa=child;
				}
			}
		}


		for(i=0;i<m;i++){
			int fa=1;
			int child=0;
			string temp;
			for(j=1;j<mid2[i].length();j++){
				temp.append(1,mid2[i][j]);
				if(mid2[i][j]=='/'){
					if(sou[temp]==0){
						total++;
						sou[temp]=total;
					}
					child=sou[temp];
					
					//cout<<temp<<endl;
					if(net[fa][child]==0){
						net[fa][child]=1;
						res++;
					}

					fa=child;
				}
			}
		}
		//cout<<total<<endl;
		printf("Case #%d: %d\n",c,res);
		
	}
	//system("pause");
	return 0;
}