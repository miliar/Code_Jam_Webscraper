#include <stdio.h>
#include <vector>

using namespace std;

#define FORab(i,a,b) for(int i = (a); i < (b); i++)
#define FORn(i,n) FORab(i,0,n)
#define DBG(args...) /*fprintf(stderr, args)*/

typedef float ff;
typedef unsigned long long ii;

#define DNP 0
#define WON 1
#define LOST 2

ii gcd (int a, int b) {
  ii temp;
  while (b != 0) {
    temp = a % b;
    a = b;
    b = temp;
  }
  return(a);
}

class Frac{
	public:

	ii p, q;

	Frac(ii _p = 0, ii _q = 1):p(_p), q(_q) {
		reduce();
	}

	void reduce() {
		if(q) {
			ii g = gcd(p,q);
			p /= g;
			q /= g;
		}
	}

	void print() {
		DBG("(%llu / %llu) ", p, q);
	}

	void printValue(int digits=12) {
		if(p == 0) {
			printf("0");
			return;
		}
		if(p < q)
			printf("0.");
		else {
			printf("%llu.", p/q);
			p = p % q;
		}
		FORn(i,digits) {
			p = p*10;
			printf("%llu", p/q);
			p = p % q;
		}
	}

	ff value() {
		if(p == (ii)0) return (ff)0;
		DBG("%llu %llu %f\n", p, q, p / (ff)q);
		return p / (ff) q;
	}

	Frac operator + (Frac f) {
		return Frac(p*f.q + q*f.p, q*f.q);
	}

	Frac operator += (Frac f) {
		p = (p*f.q + q*f.p);
		q = q*f.q;
		reduce();
		return *this;
	}

	Frac operator * (Frac f) {
		return Frac(p*f.p, q*f.q);
	}
};

class Team{
	public:

	vector<int> status;
	vector<Frac> WP2;
	Frac WP, OWP, OOWP, RPI;
	int wins, losses;

	Team() {
		wins = losses = 0;
	}
};

void main2() {
	char str[101];
	int N; scanf("%d", &N);

	vector<Team> teams;
	FORn(i,N) {
		scanf("%s", str);
		DBG("str = %s\n", str);

		Team t;
		FORn(j,N) {
			if(str[j] == '1') {
				t.wins++;
				t.status.push_back(WON);
			} else if(str[j] == '0') {
				t.losses++;
				t.status.push_back(LOST);
			} else {
				t.status.push_back(DNP);
			}
		}
		t.WP = Frac(t.wins, t.wins + t.losses);
		FORn(j,N) {
			if(t.status[j] == WON) {
				t.WP2.push_back(Frac(t.wins-1,t.wins+t.losses-1));
			} else if(t.status[j] == LOST) {
				t.WP2.push_back(Frac(t.wins,t.wins+t.losses-1));
			} else {
				t.WP2.push_back(Frac());
			}
		}
		teams.push_back(t);
	}

	DBG("1");

	FORn(i,N) {
		Team& t = teams[i];
		int count = 0;
		FORn(j,N) {
			if(t.status[j]) {
				t.OWP += teams[j].WP2[i];
				count ++;
			}
		}
		t.OWP = t.OWP * Frac(1,count);
	}

	Frac a(1,4), b(1,2);

	FORn(i,N) {
		Team& t = teams[i];
		int count = 0;
		FORn(j,N) {
			if(t.status[j]) {
				t.OOWP += teams[j].OWP;
				count ++;
			}
		}
		t.OOWP = t.OOWP * Frac(1,count);
		t.RPI = (t.WP + t.OOWP) * a + t.OWP * b;
		//float f = t.RPI.value();
		//printf("%.10f\n", f);
		DBG("WP = "); t.WP.print();
		DBG("OWP = "); t.OWP.print();
		DBG("OOWP = "); t.OOWP.print();
		DBG("RPI = "); t.RPI.print();
		DBG("\n");
		t.RPI.printValue(); printf("\n");
	}
}

int main() {
	int T; scanf("%d", &T);

	for(int caseno = 1; caseno <= T; caseno++) {
		printf("Case #%d:\n", caseno);
		main2();
	}

	return 0;
}
