#include <stdio.h>
#include <cstring>

bool ac[110][110];

int main(){
    int testnum, k, x1, x2, y1, y2, cnt, ret;
	int mx, my, ix, iy;

    scanf("%d", &testnum);
    for(int test = 1;test <= testnum;test++){
        memset(ac, false, sizeof(ac));
        scanf("%d", &k);
        cnt = ret = 0;
		mx = my = 1;
		ix = iy = 100;
        for(int i = 0;i < k;i++){
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for(int a = x1;a <= x2;a++){
                for(int b = y1;b <= y2;b++){
                    ac[a][b] = true;
                }
            }
			if(x1 < ix) ix = x1;
			if(y1 < iy) iy = y1;
			if(x2 > mx) mx = x2;
			if(y2 > my) my = y2;
        }
		for(int i = ix;i <= mx;i++){
			for(int j = iy;j <= my;j++){
				if(ac[i][j])
					cnt++;
			}
		}
        while(cnt){
            for(int i = mx;i >= ix;i--){
                for(int j = my;j >= iy;j--){
                    if(ac[i][j]){
                        if((i == 0 || (!ac[i - 1][j])) && (j == 0 || (!ac[i][j - 1]))){
                            ac[i][j] = false;
                            cnt--;
                        }
                    }else{
                        if(i && j && ac[i - 1][j] && ac[i][j - 1]){
                            ac[i][j] = true;
                            cnt++;
                        }
                    }
                }
            }
            ret++;
        }
        printf("Case #%d: %d\n", test, ret);
    }
    return 0;
}
