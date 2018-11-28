#include <iostream> 
using namespace std;

char str[5010][20];
bool flg[20][30], yes;
int main(){
	int i, j, k, res, L, D, N;
	char ch;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for( i= 0; i< D; i++ )
		scanf("%s",str[i]);
	for( i= 0; i< N; i++ ){
		memset(flg,false,sizeof(flg));
		for( j= 0; j< L; j++ ){
			ch= getchar();
		    while( ch== ' ' || ch== '\n') 
				ch= getchar();
			if( ch!= '(' )	flg[j][ch-'a']= true;
			else
				while((ch= getchar()) != ')')
					flg[j][ch-'a']= true;
		}   
		for( res= j= 0; j< D; j++ ){
			for( k= 0, yes= true; k< L; k++ ){
				if( !flg[k][str[j][k]-'a'] ){
					yes= false;
					break;
				}
			}
			if( yes )
				res++;
		}
		printf("Case #%d: %d\n",i+1,res);
	}	
}
