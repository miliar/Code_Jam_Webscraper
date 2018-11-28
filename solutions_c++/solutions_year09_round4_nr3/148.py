#include<iostream>
#include<algorithm>
#include<numeric>
#include<stdlib.h>
#include<stdio.h>
#include<queue>
#include<list>
#include<stack>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<math.h>
#include<limits>
#include<cmath>
#include<string>
#include<fstream>
#include<sstream>
#include<stdio.h>
#include<time.h>
#include<string.h>
#include<complex>
#include<iterator>
using namespace std;

struct Link{
	int v, next;
	void set( int V=-1, int Next=-1){ v=V; next=Next; }
};
class List{
public:
	int end; Link *V;
	List( int size = 1024 ){ V = new Link[size]; }
	~List(){ delete []V; }	
	void init( int n ){ end = n; for(int i=0; i<n; i++) V[i].next = -1; }
	void insert( int u, int v ){
		V[end].set( v, V[u].next );
		V[u].next = end++;
	}
};

class Match{
public:
    static bool find( int u, Link *V, bool *vis, int *y ){
        for(int i=V[u].next; i!=-1; i=V[i].next){
            int v = V[i].v;
            if( vis[v] ) continue;
            vis[v] = true;
            if( y[v] == -1 || find( y[v], V, vis, y ) ){
                y[v] = u;    return true;
            }
        }
        return false;
    }
    static int MaxMatch( int n, int m, Link *V, int *y ){
        int i, res = 0;
        for(i=0; i<m; i++) y[i] = -1;
        bool *vis = new bool[m];
        for(i=0; i<n; i++){
            memset( vis, 0, sizeof(bool)*m );
            if( find( i, V, vis, y ) ) res ++;
        }
        delete []vis;
        return res;
    }
};

int main(){
	freopen("C:\\Documents and Settings\\zgmcn\\桌面\\in.txt","r",stdin);
	freopen("C:\\Documents and Settings\\zgmcn\\桌面\\out.txt","w",stdout);
	int t, n, k, a[101][30], y[301];
	scanf("%d",&t);
	List s( 100000 );
	for(int r=1; r<=t; r++){
		scanf("%d%d",&n,&k);
		for(int i=0; i<n; i++){
			for(int j=0; j<k; j++) scanf("%d",&a[i][j]);
		}
		s.init( 2*n );
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if( i==j ) continue;
				int x = 0;
				for(; x<k; x++) if(a[i][x]<=a[j][x]) break;
				if( x<k ) continue;
				else s.insert( i, j );
			}
		}
		printf("Case #%d: %d\n",r,n-Match::MaxMatch( n, n, s.V, y ) );
	}
	return 0;
}

//int main(){
//	freopen("C:\\Documents and Settings\\zgmcn\\桌面\\in.txt","r",stdin);
//	freopen("C:\\Documents and Settings\\zgmcn\\桌面\\out.txt","w",stdout);
//	int t, n, a[41];
//	double x[41], y[41], d[41];
//	scanf("%d",&t);
//	//char s[41];
//	for(int r=1; r<=t; r++){
//		scanf("%d",&n);
//	/*	for(int i=0,j; i<n; i++){
//			scanf("%s",s);
//			for(j=n-1; j>=0; j--) if( s[j]=='1') break;
//			a[i] = j;
//		}
//		int num = 0;
//		for(int i=0,j; i<n; i++){
//			for(j=i; j<n; j++) if( a[j]<=i ) break;
//			for(int k=j-1; k>=i; k--){ swap( a[k], a[k+1] ); num++; }
//		}*/
//		for(int i=0; i<n; i++) scanf("%lf%lf%lf",&x[i],&y[i],&d[i]);
//		printf("Case #%d: ",r);
//		if( n==1 ) printf("%.5f\n",d[0]);
//		else if(n==2 ) printf("%.5f\n",max(d[0],d[1]));
//		else{
//			double s1 = d[2], d1 = sqrt((x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1]));
//			s1 = max( s1, (d1+d[0]+d[1])/2 );
//
//			double s2 = d[1], d2 = sqrt((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]));
//			s2 = max( s2, (d2+d[0]+d[2])/2 );
//
//			double s3 = d[0], d3 = sqrt((x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1]));
//			s3 = max( s3, (d3+d[2]+d[1])/2 );
//			s1 = min( s1, s2 ); s1 = min( s1, s3 );
//			printf("%.5f\n",s1);
//		}
//		//printf("Case #%d: %d\n",r,num);
//	}
//	return 0;
//}