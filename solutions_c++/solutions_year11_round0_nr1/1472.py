#include<stdio.h>
#include<string.h>

char s[100];

int main()
{

	freopen("A-large.in", "r", stdin);

     freopen("sample.out", "w", stdout);
	int t,i,j,c;
	int m,n;
	int b,o,bc,oc,c2;
	char last;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%d",&m);
		b=1;
		o=1;
		c=0;
		c2=0;
		last = 'a';
		for(j=0;j<m;j++){
			scanf("%s%d",s,&n);
			if(s[0]=='B'){
				bc = n-b>0?n-b:b-n;
				b=n;
				if(last=='B'||j==0){
					c2+=bc+1;
				}else{
					bc -= c2;
					if(bc<0){
						bc=0;
					}
					c2=bc+1; 
				}
				c+=bc+1;
				last='B';
			}else{
				oc = n-o>0?n-o:o-n;
				o=n;
				if(last=='O'||j==0)
					c2+=oc+1;
				else{
					oc -=c2;
					if(oc<0){
						oc = 0;
					}
					c2=oc+1;
				}
				c+=oc+1;
				last='O';
			}

		}
		printf("Case #%d: %d\n",i+1,c);
	}
	fclose(stdin);
    fclose(stdout);

	return 0;
}