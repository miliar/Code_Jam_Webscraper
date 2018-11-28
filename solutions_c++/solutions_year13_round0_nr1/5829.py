#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<vector>
#include<map>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
int main()
{
	int t,n,a,b,i,j,cse,x,y;
	char p[4][5];
    freopen("D:\\input.txt","r",stdin);
    freopen("D:\\output.txt","w",stdout);
    cin>>cse;
    for(t=1;t<=cse;t++)
    {
    	int cnt1=0,cnt2=0,cnt3=0,cnt4=0;
    	for(i=0;i<4;i++) cin >> p[i];
    	for(i=0;i<4;i++) for(j=0;j<4;j++) if(p[i][j]=='T') cnt4++;
    	for(i=0;i<4;i++) for(j=0;j<4;j++) if(p[i][j]=='.') cnt3++;;
    	//Case 1 T=X
    	for(i=0;i<4;i++) for(j=0;j<4;j++) if(p[i][j]=='T') {p[i][j]='X'; x=i;y=j;}
    	for(j=0;j<4;j++)
    	if(p[0][j]=='X' &&p[1][j]=='X' &&p[2][j]=='X' &&p[3][j]=='X')
    	cnt1++;
    	for(i=0;i<4;i++)
    	if(p[i][0]=='X' &&p[i][1]=='X' &&p[i][2]=='X' &&p[i][3]=='X')
    	cnt1++;
    	if(p[0][0]=='X' &&p[1][1]=='X' &&p[2][2]=='X' &&p[3][3]=='X')
    	cnt1++;
    	if(p[0][3]=='X' &&p[1][2]=='X' &&p[2][1]=='X' &&p[3][0]=='X')
    	cnt1++;
    	
    	//Case 2 T=O
    	if(cnt1==0 ){ if(cnt4==1) p[x][y]='T';
    	for(i=0;i<4;i++) for(j=0;j<4;j++) if(p[i][j]=='T') p[i][j]='O';
    	for(j=0;j<4;j++)
    	if(p[0][j]=='O' &&p[1][j]=='O' &&p[2][j]=='O' &&p[3][j]=='O')
    	cnt2++;
    	for(i=0;i<4;i++)
    	if(p[i][0]=='O' &&p[i][1]=='O' &&p[i][2]=='O' &&p[i][3]=='O')
    	cnt2++;
    	if(p[0][0]=='O' &&p[1][1]=='O' &&p[2][2]=='O' &&p[3][3]=='O')
    	cnt2++;
    	if(p[0][3]=='O' &&p[1][2]=='O' &&p[2][1]=='O' &&p[3][0]=='O')
    	cnt2++; }
    	//for(i=0;i<4;i++){cout<<p[i]<<endl;    	}
		if(cnt1>0) printf("Case #%d: X won\n",t);	
		else if(cnt2>0) printf("Case #%d: O won\n",t);	
		else if(cnt3==0) printf("Case #%d: Draw\n",t);	
		else  printf("Case #%d: Game has not completed\n",t);	
	}
	return 0;
}

