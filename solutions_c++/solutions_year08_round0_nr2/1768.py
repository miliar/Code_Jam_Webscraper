#include <stdio.h>
#include <string.h>
#define size 100000

int n, t, na, nb;
typedef struct {
	int sta, time[105], num;
}train;
train a[size], b[size];

char s[10], end[10];

int trans (char *s)
{
	return (s[0]-'0')*600  + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
}
int main ()
{
	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);
	int cases = 0;
	scanf ("%d", &n);
	while (n--){
		scanf ("%d", &t);
		scanf ("%d%d", &na, &nb);
		memset (a, 0, sizeof(a));
		memset (b, 0, sizeof(b));
		int i;
		for (i = 0; i < na; i++){
			scanf ("%s%s", &s, &end);
			int ss = trans (s);
			a[ss].time[a[ss].sta++] = trans (end);
		}
		for (i = 0; i < nb; i++){
			scanf ("%s%s", &s, &end);
			int ss = trans (s);
			b[ss].time[b[ss].sta++] = trans (end);
		}
		int tot = na + nb, ansa = 0, ansb = 0;
		int acar = 0, bcar = 0;
		for (i = 0; ; i++){
			if (tot == 0) break;
			acar += a[i].num;
			bcar += b[i].num;
			if (a[i].sta){
				tot -= a[i].sta;
				if (acar < a[i].sta){
					ansa += a[i].sta - acar;
					acar = 0;
				}
				else acar -= a[i].sta;
				for (int k = 0; k < a[i].sta; k++)
					b[a[i].time[k] + t].num++;
			}
			if (b[i].sta){
				tot -= b[i].sta;
				if (bcar < b[i].sta){
					ansb += b[i].sta - bcar;
					bcar = 0;
				}
				else bcar -= b[i].sta;
				for (int k = 0; k < b[i].sta; k++)
					a[b[i].time[k] + t].num++;				
			}			                  
		}
		printf ("Case #%d: %d %d\n", ++cases, ansa, ansb); 
	}
}
