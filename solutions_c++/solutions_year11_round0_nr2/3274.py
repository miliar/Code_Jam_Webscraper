#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <queue>
#include <cstring>
#include <ctime>
using namespace std;

#define pii pair<int,int>
#define MPII make_pair<int,int>
#define PLL pair<lng,lng>
#define MPLL make_pair<lng,lng>
#define PI 3.1415926535897932384626433832795
#define DEG2RAD (PI/180.0)
#define RAD2DEG (1.0/DEG2RAD)
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define forn(i,n) for(int i=0;i<n;++i)
#define fornr(i,n) for(int i=n-1;i>=0;--i)
#define forn1(i,n) for(int i=0;i<n+1;++i)
#define forv(i,v) for(int i=0;i<v.size();++i)
#define forvr(i,v) for(int i=v.size()-1;i>=0;--i)
#define fors(i,s) for(int i=0;i<s.length();++i)
#define EPS 1e-12
#define eps EPS
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)
#define maxll ((1LL<<62)-1+(1LL<<62))
#define SQ(a) ((a)*(a))
#define SWAP(t,a,b) {t ____tmpasdasdasd=(a);(a)=(b);(b)=____tmpasdasdasd;}
#define abs(a) ((a)<0?-(a):(a))
#define ALL(a) (a).begin(),(a).end()

char subst1[100], subst2[100], subst3[100];
char clea1[100], clea2[100];
char seq[100];
char newseq[100];
int newlen;

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tc;
	cin>>tc;
	
	forn(q,tc){
		int subst;
		memset(newseq,0,100);
		newlen=0;

		scanf("%d", &subst);
		forn(i,subst) {
			scanf(" %c%c%c", &subst1[i], &subst2[i],&subst3[i]);
		}

		int clea;
		scanf("%d", &clea);
		forn(i,clea) {
			scanf(" %c%c", &clea1[i], &clea2[i]);
		}

		int len;
		scanf(" %d%s", &len, &seq);

		forn(i,len) {
			int isnext=0;
			if (newlen == 0) {newseq[newlen++] = seq[i];continue;}
			forn(j,subst) {
				if ((seq[i]==subst1[j] && newseq[newlen-1]==subst2[j]) || 
					(seq[i]==subst2[j] && newseq[newlen-1]==subst1[j])) {
					newseq[newlen-1]=subst3[j];
					isnext=1;
					break;
				}
			}
            if (isnext) continue;

			forn(j,clea) {
				forn(m, newlen) {
					if ((seq[i]==clea1[j] && newseq[m]==clea2[j]) || 
						(seq[i]==clea2[j] && newseq[m]==clea1[j])) {
						newlen=0;
						isnext=1;
						break;
					}
				}
				if (isnext) break;
			}
			if (isnext) continue;

			newseq[newlen++] = seq[i];
		}

		cout<<"Case #"<<q+1<<": [";
		forn(i, newlen) {
			cout<<newseq[i];
			if (i<newlen-1) {
				cout<<", ";
			}
		}
		cout<<"]"<<endl;	
	}

	return 0;
}
