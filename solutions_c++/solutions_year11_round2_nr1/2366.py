#include <cstdio>
#include <cstdlib>
#include <cstring>

class zlomek {
	public:
	int cit, jmen;
	zlomek(int a, int b) {cit=a; jmen=b; zkrat();}
	zlomek() {cit=0; jmen=1;}
	void zkrat() {int acit=cit, ajmen=jmen; while(acit>0 && ajmen>0) {if(acit>ajmen) acit%=ajmen; else ajmen%=acit;} cit/=(acit+ajmen); jmen/=(acit+ajmen);}
	zlomek operator+(const zlomek &z) const {zlomek r; r.cit=cit*z.jmen+jmen*z.cit; r.jmen=jmen*z.jmen; r.zkrat(); return r;}
	zlomek operator*(const zlomek &z) const {zlomek r; r.cit=cit*z.cit; r.jmen=jmen*z.jmen; r.zkrat(); return r;}
	zlomek operator/(const zlomek &z) const {zlomek r; r.cit=cit*z.jmen; r.jmen=jmen*z.cit; r.zkrat(); return r;}
	void operator=(const zlomek &z) {cit=z.cit; jmen=z.jmen;}
	long double vydel() const {return (long double)(((long double) cit)/((long double) jmen));}
};

int main()
{
	int T; scanf("%d", &T);
	for(int test=1; test<=T; test++) {
		int N; scanf("%d\n", &N);
		char Tab[100][100];
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				scanf("%c", &Tab[i][j]);
			}
			scanf("\n");
		}
		int Vyhrane[100], Celkem[100];
		for(int i=0; i<N; i++) Vyhrane[i]=Celkem[i]=0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) if(Tab[i][j]=='1') {Vyhrane[i]++; Celkem[i]++;} else if(Tab[i][j]=='0') {Celkem[i]++;}
		}
		zlomek WP[100];
		for(int i=0; i<N; i++) WP[i]=zlomek(Vyhrane[i], Celkem[i]);
		zlomek OWP[100];
		for(int i=0; i<N; i++) {
			zlomek prumer;
			for(int j=0; j<N; j++) {
				if(Tab[i][j]=='.') continue;
				prumer=prumer+zlomek(Vyhrane[j]-(Tab[j][i]=='0' ? 0 : 1), Celkem[j]-1);
			}
			prumer=prumer/zlomek(Celkem[i], 1);
			OWP[i]=prumer;
		}
		zlomek OOWP[100];
		for(int i=0; i<N; i++) {
			zlomek prumer;
			for(int j=0; j<N; j++) {
				if(Tab[i][j]=='.') continue;
				prumer=prumer+OWP[j];
			}
			prumer=prumer/zlomek(Celkem[i], 1);
			OOWP[i]=prumer;
		}
		zlomek RPI[100];
		zlomek ctvrt(1, 4), pul(1, 2);
		for(int i=0; i<N; i++) {
			RPI[i]=RPI[i]+ctvrt*WP[i];
			RPI[i]=RPI[i]+pul*OWP[i];
			RPI[i]=RPI[i]+ctvrt*OOWP[i];
		}
		printf("Case #%d:\n", test);
		for(int j=0; j<N; j++) printf("%.8Lf\n", RPI[j].vydel());
	}

	return 0;
}
