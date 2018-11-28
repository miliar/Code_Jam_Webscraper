#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define REP(i,n) for(int i=0; i < (int)n; i++)
#define REPD(i,n) for(int i=n-1; i >= 0; i--)
#define FOR(i,a,b) for(int i= (int)a; i <= (int)b; i++)
#define FORD(i,a,b) for(int i= (int)a; i >= (int)b; i--)
#define SIZE(x) ((int)(x.size()))
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vii;
typedef vector<char> vc;
typedef vector< vc > vcc;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;

int main() {
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("A-small-attempt1.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	//freopen("inputA.txt","r",stdin);
	//freopen("outputA.txt","w",stdout);
	int cases;
	scanf("%d",&cases);
	
	REP(i,cases) {
		int n,k; scanf("%d %d",&n,&k);
		char board[n][n];
		char nl; scanf("%c",&nl);
		REP(j,n) {
			REP(k,n) {
				char t; scanf("%c",&t);
				board[j][k]=t;
				//printf("%c",t);
			}
			scanf("%c",&nl);
			//printf("\n");
		}
	
		char nboard[n][n];
		REP(a,n) {
			REP(b,n) {
				nboard[a][b] = board[n-b-1][a]; 
			}
		}

		//gravity
		REP(c,n) {
			FORD(k,n-1,1) {
				int b=0;
				REP(q,k) if(nboard[q][c]!='.') b=1;
				while((nboard[k][c]=='.') && (b==1)) {
					int count=0;
					FORD(d,k,1) {
						nboard[d][c]=nboard[d-1][c];
					}
					nboard[count][c]='.';
					count++;
				}
			}
		}
		int r=0,blue=0;
		int maxr=0,maxb=0;
		int redmax=0,bluemax=0;
		//count
		REP(a,n) {
			int rcount=0,bcount=0;
			REP(b,n) {
				//printf("%c",nboard[a][b]);
				char z='a';
				if(nboard[a][b]!='.') {
					z=nboard[a][b];
					rcount=1;
					int c=b+1;
					while(c <= n-1) {
						if(nboard[a][c]==z) rcount++;
						else break;
						c++;
					}
					c=b-1;
					while(c >= 0) {
						if(nboard[a][c]==z) rcount++;
						else break;
						c--;
					}
					maxr=max(maxr,rcount);
					rcount=1;
					c=a+1;
					while(c<=n-1) {
						if(nboard[c][b]==z) rcount++;
						else break;
						c++;
					}
					c=a-1;
					while(c>=0) {
						if(nboard[c][b]==z) rcount++;
						else break;
						c--;
					}
					maxr=max(maxr,rcount);
					//diagonal
					int d1=a+1; int d2=b+1;
					rcount=1;
					while((d1<=n-1) && (d2<=n-1)) {
						if(nboard[d1][d2]==z) rcount++;
						else break;
						d1++; d2++;
					}
					d1=a-1;d2=b-1;
					while((d1>=0) && (d2>=0)) {
						if(nboard[d1][d2]==z) rcount++;
						else break;
						d1--; d2--;
					}
					maxr=max(maxr,rcount);

					//other diag
					d1=a+1; d2=b-1;
					rcount=1;
					while((d1<=n-1) && (d2>=0)) {
						if(nboard[d1][d2]==z) rcount++;
						else break;
						d1++; d2--;
					}
					d1=a-1; d2=b+1;
					while((d1>=0) && (d2<=n-1)) {
						if(nboard[d1][d2]==z) rcount++;
						else break;
						d1--; d2++;
					}
					maxr=max(maxr,rcount);
				}
				if(z!='.')
					//printf("%c %d\n",z,maxr);
				if(z=='R') { redmax=max(redmax,maxr); r=max(r,redmax); }
				else if(z=='B') { bluemax=max(bluemax,maxr); blue=max(blue,bluemax); }
				maxr=0;
			}
			//printf("\n");
		}
		//printf("%d %d %d\n",r,blue,k);
		printf("Case #%d: ",i+1);
		if((r>=k) &&(blue>=k)) printf("Both\n");
		else if(r>=k) printf("Red\n");
		else if(blue>=k) printf("Blue\n");
		else printf("Neither\n");
	}

}
