#include<iostream>
#include<algorithm>
using namespace std;


char pattern[5000+10][20];


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int L,D,N;
	while(scanf("%d %d %d",&L,&D,&N)!=EOF){
		for(int i=0;i<D;i++)
			scanf("%s",pattern[i]);
		char str[1000];
		int Case=1;
		bool flag[20][30];
		for(int i=0;i<N;i++){
			scanf("%s",str);
			memset(flag,false,sizeof(flag));
			int k=0;
			for(int j=0;str[j]!='\0';j++){
				if( str[j]=='(' ){
					j++;
					while(str[j]!=')' ){
						flag[k][ str[j]-'a' ]=true;
						j++;
					}
				}
				else flag[k][ str[j]-'a']=true;
				k++;
			}
			int cnt=0;
			for(int j=0;j<D;j++){
				int k=0;
				for( ; k<L && flag[k][ pattern[j][k]-'a' ] ;k++);
				if( k==L )cnt++;
			}
			printf("Case #%d: %d\n",Case,cnt);
			Case++;
		}
	}
	return 0;
}


				

		