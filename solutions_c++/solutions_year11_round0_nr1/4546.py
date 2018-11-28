#include <stdio.h>

int main()
{
	int t;
	scanf("%d", &t);
	
	for (int tc = 1; tc <= t; tc++)
	{
		int n;
		scanf("%d ", &n);
		
		int vo[128], vb[128], to = 0, tb = 0, vn[128], tn = 0;
		char vc[128];
		
		for (int i = 0; i < n; i++)
		{
			char c;
			int b;
			
			scanf("%c %d ", &c, &b);
			vn[tn] = b;
			vc[tn++] = c;
			
			if (c == 'O')
			{
				vo[to++] = b;
			}
			else
			{
				vb[tb++] = b;
			}
		}
		
		int tm = 1;
		for (int po = 1, co = 0, pb = 1, cb = 0, cn = 0; 1; tm++)
		{
			bool perto = false;
			if (co < to){
			if (po == vo[co] and vn[cn] == po and vc[cn] == 'O')
			{
				co++;
				cn++;
				perto = true;
			}
			else
			{
			if (po < vo[co])
				po++;
			else
			{
			if (po > vo[co])
				po--;
				}
			}}
			
			//printf("po = %d\n", po);
			
			if (cb < tb){
			if (pb == vb[cb] and vn[cn] == pb and vc[cn] == 'B' and !perto)
			{
				cb++;
				cn++;
			}else{
			
			if (pb < vb[cb])
				pb++;
			else{
			if (pb > vb[cb])
				pb--;}
			}}
			
			//printf("pb = %d\n", pb);
			
			//printf("\n\n");
			
			if (cn == n)
				break;
		}
		
		printf("Case #%d: %d\n", tc, tm);
	}

	return 0;
}
