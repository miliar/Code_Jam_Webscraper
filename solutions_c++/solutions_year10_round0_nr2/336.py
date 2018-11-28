#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = ((int)n)-1; i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

/*vector<int> numbers[1000];

bool menor(vector<int> vec1, vector<int> vec2)
{
    dforn(i,60)
    {
        if(vec1[i]<vec2[i])
        {
            return true;
        }
        if(vec1[i]>vec2[i])
        {
            return false;
        }
    }
    return true;
}

vector<int> resta(vector<int> vec1, vector<int> vec2)
{
    dforn(i,60)
    {
        if(vec1[i]<vec2[i])
        {
            swap(vec1,vec2);
            break;
        }
        if(vec1[i]>vec2[i])
        {
            break;
        }
    }
    vector<int> res(60);
    forn(i,60)
        res[i] = vec1[i]-vec2[i];
    for(int i=59;i>0;i++)
    {
        if(res[i]>9)
        {
            res[i-1]+=res[i]/10;
            res[i]%=10;
        }
    }
    return res;
}

vector<int> suma(vector<int> vec1, vector<int> vec2)

vector<int> mult(vector<int> vec1, vector<int> vec2)
{
    vector<int> res(60);
    forn(i,60)
    forn(j,60-i)
        res[i+j] = vec1[i]*vec2[j];
    for(int i=59;i>0;i++)
    {
        if(res[i]>9)
        {
            res[i-1]+=res[i]/10;
            res[i]%=10;
        }
    }
    return res;
}

vector<int> div(vector<int> vec1, vector<int> vec2)
{
    vector<int> vec(60,0);
    vec[0] = 1;
    int pos = 0;
    while(menor(mult(vec,
}

vector<int> modulo(vector<int> vec1, vector<int> vec2)
{
    return resta(vec1,mult(div(vec1,vec2),vec2));
}

vector<int> mcd(vector<int> vec1, vector<int> vec2)
{
    return (count(all(vec1),0)==60)?vec2:mcd(modulo(vec2,vec1),vec1);
}
*/

typedef long long tipo;
#define BASEXP 6
#define BASE 1000000
#define LMAX 1000

struct Long {
	int l;
	tipo n[LMAX];
	Long(tipo x) { 	l = 0; forn(i, LMAX) { n[i]=x%BASE; l+=!!x||!i; x/=BASE;} }
	Long(){*this = Long(0);}
	Long(string x) {
		l=(x.size()-1)/BASEXP+1;
		fill(n, n+LMAX, 0);
		tipo r=1;
		forn(i,x.size()){
			n[i / BASEXP] += r * (x[x.size()-1-i]-'0');
			r*=10; if(r==BASE)r=1;
		}
	}
};

void out(Long& a) {
	char msg[BASEXP+1];
	cout << a.n[a.l-1];
	dforn(i,a.l-1) {
		sprintf(msg, "%6.6llu", a.n[i]); cout << msg; // 6 = BASEXP !
	}
	cout << endl;
}
void invar(Long &a) {
	fill(a.n+a.l, a.n+LMAX, 0);
	while(a.l>1 && !a.n[a.l-1]) a.l--;
}

void lsuma(const Long&a, const Long&b, Long&c) { // c = a + b
	c.l = max(a.l, b.l);
	tipo q = 0;
	forn(i, c.l) q += a.n[i]+b.n[i], c.n[i]=q%BASE, q/=BASE;
	if(q) c.n[c.l++] = q;
	invar(c);
}
Long& operator+= (Long&a, const Long&b) { lsuma(a, b, a); return a; }
Long operator+ (const Long&a, const Long&b) { Long c; lsuma(a, b, c); return c; }

bool lresta(const Long&a, const Long&b, Long&c) { // c = a - b
	c.l = max(a.l, b.l);
	tipo q = 0;
	forn(i, c.l) q += a.n[i]-b.n[i], c.n[i]=(q+BASE)%BASE, q=(q+BASE)/BASE-1;
	invar(c);
	return !q;
}
Long& operator-= (Long&a, const Long&b) { lresta(a, b, a); return a; }
Long operator- (const Long&a, const Long&b) {Long c; lresta(a, b, c); return c;}

bool operator< (const Long&a, const Long&b) { Long c; return !lresta(a, b, c); }
bool operator<= (const Long&a, const Long&b) { Long c; return lresta(b, a, c); }
bool operator== (const Long&a, const Long&b) { return a <= b && b <= a; }

void lmul(const Long&a, const Long&b, Long&c) { // c = a * b
	c.l = a.l+b.l;
	fill(c.n, c.n+b.l, 0);
	forn(i, a.l) {
		tipo q = 0;
		forn(j, b.l) q += a.n[i]*b.n[j]+c.n[i+j], c.n[i+j] = q%BASE, q/=BASE;
		c.n[i+b.l] = q;
	}
	invar(c);
}

Long& operator*= (Long&a, const Long&b) { Long c; lmul(a, b, c); return a=c; }
Long operator* (const Long&a, const Long&b) { Long c; lmul(a, b, c); return c; }

void lmul(const Long&a, int b, Long&c) { // c = a * b
	int q = 0;
	forn(i, a.l) q += a.n[i]*b, c.n[i] = q%BASE, q/=BASE;
	c.l = a.l;
	while(q) c.n[c.l++] = q%BASE, q/=BASE;
}

Long& operator*= (Long&a, int b) { lmul(a, b, a); return a; }
Long operator* (const Long&a, int b) { Long c = a; c*=b; return c; }

void ldiv(const Long& a, tipo b, Long& c, tipo& rm) { // c = a / b ; rm = a % b
	rm = 0;
	dforn(i, a.l) {
		rm = rm * BASE + a.n[i];
		c.n[i] = rm / b; rm %= b;
	}
	c.l = a.l;
	invar(c);
}

void ldiv(const Long& a, const Long& b, Long& c, Long& rm) { // c = a / b ; rm = a % b
	rm = 0;
	dforn(i, a.l) {
		dforn(j, rm.l) rm.n[j+1] = rm.n[j];
		rm.n[0] = a.n[i]; rm.l++;
		tipo q = rm.n[b.l] * BASE + rm.n[b.l-1];
		tipo u = q / (b.n[b.l-1] + 1);
		tipo v = q /  b.n[b.l-1] + 1;
		while (u < v-1) {
			tipo m = (u+v)/2;
			if (b*m <= rm) u = m; else v = m;
		}
		c.n[i] = u;
		rm -= b*u;
	}
	c.l = a.l;
	invar(c);
}

Long mcd(Long a, Long b)
{
    if(b == Long(0)) return a;
    Long c,rm;
    ldiv(a,b,c,rm);
    return mcd(b,rm);
}

Long numbers[1000];
vector<Long> diff;

int main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int casos;
    cin >> casos;
    string res;
    forn(casito,casos)
    {
        int n;
        cin >> n;
        diff.resize(n*n);
        string st;
        forn(i,n)
        {
            cin >> st;
            numbers[i] = Long(st);
        }
        forn(i,n)
        forn(j,n)
            diff[i*n+j] = (numbers[i]<numbers[j])?numbers[j]-numbers[i]:numbers[i]-numbers[j];
        Long lg = diff[0];
        for(int i=1;i<n*n;i++)
        {
            lg = mcd(lg,diff[i]);
        }
        Long c,rm;
        ldiv(numbers[0],lg,c,rm);
        if(rm==0)
            lg = Long(0);
        else
            lg = lg-rm;
        cout << "Case #" << casito+1 << ": ";
        out(lg);
    }
}
