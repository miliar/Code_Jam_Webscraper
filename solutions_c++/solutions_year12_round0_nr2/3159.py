#include<cstdlib>
#include<stdio.h>

int main(){
	int T, n, s, p, ti, ans;
    scanf("%d", &T);
    for(int i=0; i<T; i++){
	    ans=0;
		scanf("%d%d%d", &n, &s, &p);
	    for(int j=0; j<n; j++){
		    scanf("%d", &ti);
		    ti-=p;
		    if(ti<0)  ;
			else if(ti>=2*(p-1))  ans++;
		    else if(ti>=2*(p-2)&&s>0){
			    ans++;
			    s--;
			}
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
    return 0;
}
