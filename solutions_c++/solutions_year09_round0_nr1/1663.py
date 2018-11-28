#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int l, d, n, i, j, k, tn, tot;
char dic[5009][20];
char s[2000], t[20][26];

int main()
{
 	freopen("A-large.in", "r", stdin);
 	freopen("A-large.out", "w", stdout);
 	scanf("%d%d%d", &l, &d, &n);
 	for (i=0;i<d;i++) 
        scanf("%s", dic[i]);
    for (i=0;i<n;i++)
	{
	 	scanf("%s", s);
	 	j = tn = 0;
	 	while (s[j])
		{
		   memset(t[tn], 0, sizeof(t[tn]));
		   if (s[j] == '('){
		       j++;
		       while (s[j]!=')'){
			   	   t[tn][s[j]-'a'] = 1;
			   	   j++;
			   }
			   j++;
	  	   }else{
  	   	   	   t[tn][s[j]-'a'] = 1;
			   j++;
		   }
		   tn++;
	    }
	    tot = 0;
	    for (j=0;j<d;j++){
		   for (k=0;k<l;k++) 	
		      if (!t[k][dic[j][k]-'a']) break;
           if (k>=l) tot++;
        }
        printf("Case #%d: %d\n", i+1, tot);
	}
	//scanf("%d", &i);
	return 0;
}
