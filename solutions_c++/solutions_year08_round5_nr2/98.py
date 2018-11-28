#include <cstdio>

struct state{
	int hx, hy;
	int pax, pay;
	int pad;
	int pbx, pby;
	int pbd;
};

int encode(const state &st){
	return st.hx | (st.hy << 4) | (st.pax << 8) | (st.pay << 12) | (st.pad << 16) | (st.pbx << 17) | (st.pby << 21) | (st.pbd << 25);
}

void decode(state &st, int n){
	st.hx = n & 15;
	st.hy = (n>>4) & 15;
	st.pax = (n>>8) & 15;
	st.pay = (n>>12) & 15;
	st.pad = (n>>16) & 1;
	st.pbx = (n>>17) & 15;
	st.pby = (n>>21) & 15;
	st.pbd = (n>>25) & 1;
}

int row, col;
char map[16][16];

void jump(state &st, int x, int y, int d){
	if (d == 0){
		st.hx = x;
		if (y >= row || map[y][x] == '#')
			st.hy = y-1;
		else
			st.hy = y;
	} else {
		st.hy = y;
		if (x >= col || map[y][x] == '#')
			st.hx = x-1;
		else
			st.hx = x;
	}
}

int main(){
	int n;
	scanf("%d", &n);

	int nst0, nst1;
	int *st0 = new int[67108864];
	int *st1 = new int[67108864];
	int *best = new int[67108864];

	for (int cases = 0; cases < n; cases++){
		scanf("%d%d", &row, &col);

		for (int tmp = 0; tmp < row; tmp++)
			scanf("%s", map[tmp]);

		int hx, hy;
		int dx, dy;
		for (int r = 0; r < row; r++)
			for (int c = 0; c < col; c++){
				if (map[r][c] == 'O'){
					hx = c;
					hy = r;
					map[r][c] = '.';
				}
				if (map[r][c] == 'X'){
					dx = c;
					dy = r;
					map[r][c] = '.';
				}
			}

		state init;
		init.hx = hx;
		init.hy = hy;
		init.pax = init.pbx = hx;
		for (init.pay = hy; init.pay >= 0 && map[init.pay][hx] != '#'; init.pay--);
		init.pby = ++init.pay;
		init.pad = init.pbd = 0;

		for (int tmp = 0; tmp < 67108864; tmp++)
			best[tmp] = 9999999;
		int ans = 0;
		nst0 = 1;
		nst1 = 0;
		best[st0[0] = encode(init)] = 0;

		while(1){
			if (!nst0){
				printf ("Case #%d: THE CAKE IS A LIE\n", cases+1);
				break;
			}

			while(nst0){
				if (best[st0[--nst0]] != ans)
					continue;

				state cur;
				decode(cur, st0[nst0]);

				if (cur.hx == dx && cur.hy == dy){
					printf ("Case #%d: %d\n", cases+1, ans);
					goto deepbreak;
				}

				state next; int enc;

				next=cur;next.pax=next.hx;for(next.pay = next.hy; next.pay >= 0 && map[next.pay][next.hx] != '#'; next.pay--);next.pay++;next.pad=0;
				if (best[enc=encode(next)] > ans){best[enc=encode(next)] = ans; st0[nst0++] = encode(next);}
				next=cur;next.pbx=next.hx;for(next.pby = next.hy; next.pby >= 0 && map[next.pby][next.hx] != '#'; next.pby--);next.pby++;next.pbd=0;
				if (best[enc=encode(next)] > ans){best[enc=encode(next)] = ans; st0[nst0++] = encode(next);}
				next=cur;next.pax=next.hx;for(next.pay = next.hy; next.pay < row && map[next.pay][next.hx] != '#'; next.pay++);next.pad=0;
				if (best[enc=encode(next)] > ans){best[enc=encode(next)] = ans; st0[nst0++] = encode(next);}
				next=cur;next.pbx=next.hx;for(next.pby = next.hy; next.pby < row && map[next.pby][next.hx] != '#'; next.pby++);next.pbd=0;
				if (best[enc=encode(next)] > ans){best[enc=encode(next)] = ans; st0[nst0++] = encode(next);}
				next=cur;next.pay=next.hy;for(next.pax = next.hx; next.pax >= 0 && map[next.hy][next.pax] != '#'; next.pax--);next.pax++;next.pad=1;
				if (best[enc=encode(next)] > ans){best[enc=encode(next)] = ans; st0[nst0++] = encode(next);}
				next=cur;next.pby=next.hy;for(next.pbx = next.hx; next.pbx >= 0 && map[next.hy][next.pbx] != '#'; next.pbx--);next.pbx++;next.pbd=1;
				if (best[enc=encode(next)] > ans){best[enc=encode(next)] = ans; st0[nst0++] = encode(next);}
				next=cur;next.pay=next.hy;for(next.pax = next.hx; next.pax < col && map[next.hy][next.pax] != '#'; next.pax++);next.pad=1;
				if (best[enc=encode(next)] > ans){best[enc=encode(next)] = ans; st0[nst0++] = encode(next);}
				next=cur;next.pby=next.hy;for(next.pbx = next.hx; next.pbx < col && map[next.hy][next.pbx] != '#'; next.pbx++);next.pbd=1;
				if (best[enc=encode(next)] > ans){best[enc=encode(next)] = ans; st0[nst0++] = encode(next);}

				next=cur;next.hx++;
				if (next.hx < col && map[next.hy][next.hx] != '#'){if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				else if(next.pax == next.hx && next.pay == next.hy && next.pad == 1){jump(next, next.pbx, next.pby, next.pbd);if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				else if(next.pbx == next.hx && next.pby == next.hy && next.pbd == 1){jump(next, next.pax, next.pay, next.pad);if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				next=cur;next.hy++;
				if (next.hy < row && map[next.hy][next.hx] != '#'){if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				else if(next.pax == next.hx && next.pay == next.hy && next.pad == 0){jump(next, next.pbx, next.pby, next.pbd);if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				else if(next.pbx == next.hx && next.pby == next.hy && next.pbd == 0){jump(next, next.pax, next.pay, next.pad);if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				next=cur;next.hx--;
				if (next.hx >=0 && map[next.hy][next.hx] != '#'){if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				else if(next.pax == next.hx+1 && next.pay == next.hy && next.pad == 1){jump(next, next.pbx, next.pby, next.pbd);if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				else if(next.pbx == next.hx+1 && next.pby == next.hy && next.pbd == 1){jump(next, next.pax, next.pay, next.pad);if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				next=cur;next.hy--;
				if (next.hy >=0 && map[next.hy][next.hx] != '#'){if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				else if(next.pax == next.hx && next.pay == next.hy+1 && next.pad == 0){jump(next, next.pbx, next.pby, next.pbd);if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
				else if(next.pbx == next.hx && next.pby == next.hy+1 && next.pbd == 0){jump(next, next.pax, next.pay, next.pad);if(best[enc=encode(next)] > ans+1){best[enc=encode(next)] = ans+1; st1[nst1++] = encode(next);}}
			}

			nst0 = nst1;
			nst1 = 0;
			int *foo = st0;
			st0 = st1;
			st1 = foo;
			ans++;
		}
		deepbreak:;
	}
	return 0;
}
