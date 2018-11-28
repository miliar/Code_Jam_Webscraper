#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

#define LL long long
#define MaxN (1111)

LL n,m,d,a[MaxN][MaxN];
char ch[MaxN][MaxN];
LL sc[MaxN][MaxN],sr[MaxN][MaxN];
LL scr[MaxN][MaxN],scl[MaxN][MaxN];
LL srr[MaxN][MaxN],srl[MaxN][MaxN];

LL _sr(LL a,LL b,LL c){return sr[a][c]-(b?sr[a][b-1]:0);}
LL _sc(LL a,LL b,LL c){return sc[a][c]-(b?sc[a][b-1]:0);}

LL _srl(LL a,LL b,LL c){return srl[a][c]-(b?srl[a][b-1]:0)-_sr(a,b,c)*b;}
LL _scl(LL a,LL b,LL c){return scl[a][c]-(b?scl[a][b-1]:0)-_sc(a,b,c)*b;}

LL _srr(LL a,LL b,LL c){return srr[a][c]-((b+1<m)?srr[a][b+1]:0)-_sr(a,c,b)*(m-b-1);}
LL _scr(LL a,LL b,LL c){return scr[a][c]-((b+1<n)?scr[a][b+1]:0)-_sc(a,c,b)*(n-b-1);}


void work(){
	cin >> n >> m >> d;
	for (int i=0;i<n;i++)
		scanf("%s",ch[i]);
	memset(a,0,sizeof(a));
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			a[i*2][j*2]=(LL)(ch[i][j]-'0')+d;
	n*=2;m*=2;
	for (int i=0;i<n;i++){
		LL cur=0;
		for (int j=0;j<m;j++){
			cur+=a[i][j];
			sr[i][j]=cur;
			//cout << sr[i][j] <<" ";
		}
	//	puts("");
	}
	for (int i=0;i<m;i++){
		LL cur=0;
		for (int j=0;j<n;j++){
			cur+=a[j][i];
			sc[i][j]=cur;
		}
	}
	for (int i=0;i<n;i++){
		LL cur=0;
		for (int j=0;j<m;j++){
			cur+=a[i][j]*(LL)(j+1);
			srl[i][j]=cur;
		}
	}
	for (int i=0;i<m;i++){
		LL cur=0;
		for (int j=0;j<n;j++){
			cur+=a[j][i]*(LL)(j+1);
			scl[i][j]=cur;
		}
	}

	for (int i=0;i<n;i++){
		LL cur=0;
		for (int j=m-1;j>=0;j--){
			cur+=a[i][j]*(LL)(m-j);
			srr[i][j]=cur;
		}
	}
	for (int i=0;i<m;i++){
		LL cur=0;
		for (int j=n-1;j>=0;j--){
			cur+=a[j][i]*(LL)(n-j);
			scr[i][j]=cur;
		}
	}
	//cout << _srr(1,3,1) <<endl;
	//
	//puts("");
	//for (int i=0;i<n;i++){
//		for (int j=0;j<m;j++) cout << a[i][j] <<" ";
//		puts("");
//	}
	
	
	int ret=0;
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++){
			if ((i+j)%2!=0) continue;
			for (int len=1;i+len<n&&j+len<m&&i-len>=0&&j-len>=0;len++){
				
				LL cur1=0,cur2=0;
				for (int p=i-len;p<=i+len;p++)
					for (int q=j-len;q<=j+len;q++){
						if ((p==i-len||p==i+len)&&(q==j-len||q==j+len)) continue;
						cur1+=(p-i)*a[p][q];
						cur2+=(q-j)*a[p][q];
					}
				if (cur1==0&&cur2==0) {
					if (i%2==0) {if (len%2==0) ret=max(ret,len+1);}
						else {if (len%2==1) ret=max(ret,len+1);}
				}
			}
		}
	/*for (int i=0;i<n;i++)
		for (int j=0;j<m;j++){
			if ((i+j)%2!=0) continue;
			LL cur1=0,cur2=0;
			for (int len=1;i+len<n&&j+len<m&&i-len>=0&&j-len>=0;len++){
				//if (len%2==1&&len>1)cout << len <<" " << cur1 <<" " << cur2 <<endl;
				if (cur1+_sr(i-len,j-len+1,j+len-1)-_sr(i+len,j-len+1,j+len-1)
						+_scl(j-len,i-len+1,i)-_scr(j-len,i+len-1,i)
						+_scl(j+len,i-len+1,i)-_scr(j+len,i+len-1,i)!=0) continue;
				
				if (cur2+_sc(j-len,i-len+1,i+len-1)-_sc(j+len,i-len+1,i+len-1)
						+_srl(i-len,j-len+1,j)-_srr(i-len,j+len-1,j)
						+_srl(i+len,j-len+1,j)-_srr(i+len,j+len-1,j)!=0) continue;
				if (i%2==0) {if (len%2==0) ret=max(ret,len+1);}
				else {if (len%2==1) ret=max(ret,len+1);}
				cur1=cur1+_sr(i-len,j-len,j+len)-_sr(i+len,j-len,j+len)
						+_scl(j-len,i-len+1,i)-_scr(j-len,i+len-1,i)
						+_scl(j+len,i-len+1,i)-_scr(j+len,i+len-1,i);
				cur2=cur2+_sc(j-len,i-len,i+len)-_sc(j+len,i-len,i+len)
						+_srl(i-len,j-len+1,j)-_srr(i-len,j+len-1,j)
						+_srl(i+len,j-len+1,j)-_srr(i+len,j+len-1,j);
			}
		}*/
	//cout << ret <<endl;
	if (ret>=3)cout << ret <<endl;
	else puts("IMPOSSIBLE");
}



int main(){
	freopen("B2.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ":" <<" ";
		work();
	}
	//system("pause");
	return 0;
}
