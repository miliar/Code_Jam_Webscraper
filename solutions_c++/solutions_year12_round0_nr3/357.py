#include<cstdio>
#include<algorithm>

using namespace std;

int casos, a, b, ans, x1, x2, q, wv, ten[15], tn[10];

void teste(int p){
	bool flag;
	for(int i=wv-2;i>=0;i--){
		x1 = p%ten[i+1];
		x2 = p/ten[i+1];
		q = (x1*ten[wv-(i+1)]) + x2;
		
		flag = true;
		for(int j=0;j<wv-2-i;j++)
			if(tn[j] == q) flag = false;
		if(!flag) continue;
		tn[(wv-2)-i] = q;

		if(p < q && q <= b) ans++;
	}
}

int main(){
	ten[0]=1; for(int i=1;i<9;i++) ten[i]=10*ten[i-1];
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
	scanf(" %d %d", &a, &b);
	ans = wv = 0;
	for(int i=0;i<9 && !wv;i++) if(ten[i] > a) wv = i;
	for(int i=a;i<b;i++){
		if(i >= ten[wv]) wv++;
		teste(i);
	}
	printf("Case #%d: %d\n", inst, ans);
	}
	return 0;
}

