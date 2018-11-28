#include<cstdio>
#include<algorithm>

using namespace std;
const int MAX = 1200;

int n, did, curr, casos, bestn, bestp, vis[MAX], r1[MAX], r2[MAX];
bool flag;

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
	scanf(" %d", &n);
	for(int i=0;i<n;i++){
		scanf(" %d %d", &r1[i], &r2[i]);
		vis[i] = 0;
	}
	did = curr = 0;
	flag = true;
	while(flag){ flag = false;
		for(int i=0;i<n;i++)
			if(vis[i] == 0 && curr >= r2[i]){
				//printf("m2 at %d\n", i);
				flag = true; did++; curr+=2; vis[i] = 2;
			}
		if(flag) continue;
		for(int i=0;i<n && !flag;i++)
			if(vis[i] == 1 && curr >= r2[i]){
				//printf("m2[weak] at %d\n", i);
				flag = true; did++; curr++; vis[i] = 2;
			}
		if(flag) continue;
		bestn = -1;
		for(int i=0;i<n;i++){
			if(vis[i] == 0 && curr >= r1[i]){
				if(r2[i] > bestn){
					bestn = r2[i];
					bestp = i;
					//printf("gothier mit %d $ %d:%d: bn bp %d %d\n", i, curr, did, bestn, bestp);
				}
			}
		}
		if(bestn != -1){ //printf("m1 at %d\n", bestp);
			flag = true; did++; curr++; vis[bestp] = 1; }
	}
	flag = true;
	for(int i=0;i<n;i++) if(vis[i] != 2) flag = false;
	if(flag == false) printf("Case #%d: Too Bad\n", inst);
	else printf("Case #%d: %d\n", inst, did);
	}
	return 0;
}

