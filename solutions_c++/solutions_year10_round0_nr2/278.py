#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

const int base = 1000000, dig = 6;

typedef long long ll;
typedef vector<int> vi;
vi l[1010];
int n;
char s[100];

void print(vi &a){
	printf("%d", a.back());
	for(int i=(int)a.size()-2; i>=0; --i)
		printf("%0*d", dig, a[i]);
	printf("\n");
}

vi parse(){
	vi ret; ret.clear();
	int j = 0;
	while(s[j] != '\0') ++j;
	--j;
	while(j >= 0){
		int l = 0;
		int p10 = 1;
		for(int i=j; i>j-dig && i>=0; --i){
			l += p10 * (s[i]-'0');
			p10 *= 10;
		}
		ret.push_back(l);
		j -= dig;
	}
	return ret;
}

bool less(vi &a, vi &b){
	if(a.size() != b.size()) return a.size() < b.size();
	for(int i=(int)a.size()-1; i>=0; --i)
		if(a[i] != b[i]) return a[i] < b[i];
	return false;
}

bool lessEq(vi &a, vi &b){
	if(a.size() != b.size()) return a.size() < b.size();
	for(int i=(int)a.size()-1; i>=0; --i)
		if(a[i] != b[i]) return a[i] < b[i];
	return true;
}

vi add(vi &a, vi &b){
	vi ret;
	int r = 0;
	for(int i=0; i<a.size() || i<b.size(); ++i){
		int l = (i<a.size() ? a[i] : 0) + (i<b.size() ? b[i] : 0) + r;
		r = l / base;
		l %= base;
		ret.push_back(l);
	}
	if(r > 0) ret.push_back(r);
	return ret;
}

vi sub(vi &a, vi &b){
	if(less(a,b)) return sub(b,a);
	vi ret;
	int r = 0;
	for(int i=0; i<a.size(); ++i){
		int l = a[i] - (i<b.size() ? b[i] : 0) - r;
		r = 0;
		while(l < 0){ l += base; r++; }
		ret.push_back(l);
	}
	while(!ret.empty() && ret.back() == 0) ret.pop_back();
	if(ret.empty()) ret.push_back(0);
	return ret;
}

static inline bool zero(vi &a){
	return (int)a.size() == 1 && a[0] == 0;
}

static inline bool even(vi &a){
	return a[0] % 2 == 0;
}

void div2(vi &a){
	for(int i=(int)a.size()-1; i>=0; --i){
		if(a[i] % 2 != 0 && i > 0) a[i-1] += base;
		a[i] /= 2;
	}
	while(a.back() == 0) a.pop_back();
}

vi mult(vi &a, vi &b){
	vi ret((int)a.size() + (int)b.size() + 2, 0);
	for(int i=0; i<a.size(); ++i)
		for(int j=0; j<b.size(); ++j){
			ll l = (ll)a[i] * b[j];
			ret[i+j] += l % base;
			ret[i+j+1] += l / base;
		}
	for(int i=0; i+1<ret.size(); ++i){
		ret[i+1] += ret[i] / base;
		ret[i] %= base;
	}
	while(!ret.empty() && ret.back() == 0) ret.pop_back();
	if(ret.empty()) ret.push_back(0);
	return ret;
}

vi div(vi &a, vi &b){
	vi add1(1,1);
	vi left(1,0), right = add(add1,a);
	while(true){
		vi l1 = add(left,add1);
		if(!less(l1,right)) break;
		vi mid = add(left,right);
		div2(mid);
		vi mlt = mult(mid,b);
		if(lessEq(mlt,a)) left = mid;
		else right = mid;
	}
	return left;
}

vi gcd(vi a, vi b){
	vi ret(1,1);
	vi m2(1,2);
	if(less(a,b)) swap(a,b);
	while(!zero(b)){
		if(even(a) && even(b)){
			div2(a);
			div2(b);
			ret = mult(ret, m2);
		}
		else if(even(a)){
			div2(a);
		}
		else if(even(b)){
			div2(b);
		}
		else{
			a = sub(a,b);
		}
		if(less(a,b)) swap(a,b);
	}
	ret = mult(ret, a);
	return ret;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		scanf("%d", &n);
		for(int i=0; i<n; ++i){
			scanf("%s", s);
			l[i] = parse();
		}
		
		vi nwd(1,0);
		for(int i=1; i<n; ++i){
			vi roz = sub(l[0],l[i]);
			nwd = gcd(roz, nwd);
		}
		
		printf("Case #%d: ", iii);
		vi dziel = div(l[0],nwd);
		vi ml = mult(dziel,nwd);
		vi mod = sub(l[0],ml);
		if(zero(mod)){ printf("0\n"); continue; }
		mod = sub(nwd,mod);
		print(mod);
	}
	return 0;
}
