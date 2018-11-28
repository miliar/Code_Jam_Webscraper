#include<stdio.h>
#include<string.h>
inline int abs(int a){
	if(a<0)return -a;
	else return a;
}
#define max(a,b) ((a>b) ? (a) : (b))
//com a[128];
int solve(){
	int n,d,c,i,j,k;
	char cm[36][4];
	char op[28][4];
	char a[128];
	char bf[128],*b=bf+1;
	bf[0]=0;
	
	scanf("%d",&c);
	for(i=0;i<c;i++)
		scanf("%s",cm[i]);

	scanf("%d",&d);
	for(i=0;i<d;i++)
		scanf("%s",op[i]);

	scanf("%d",&n);
	scanf("%s",a);
	n=0;
	bool p;
	for(i=0;a[i];i++){
		b[n]=a[i];
		p=0;
		for(j=0;j<c && !p;j++)
			if(p=(cm[j][0]==b[n] && cm[j][1]==b[n-1] || cm[j][1]==b[n] && cm[j][0]==b[n-1] ))			
				b[n-1]=cm[j][2];

		if(!p){
			for(j=0;j<d && !p;j++)
			{
				if(op[j][0]==b[n])
				{
					for(k=0;k<n && !(p=(op[j][1]==b[k]));k++);
					
				}
				if(op[j][1]==b[n])
				{
					for(k=0;k<n && !(p=(op[j][0]==b[k]));k++);
					
				}

			}
			n++;
			if(p)n=0;
		}
	}

	putchar('[');
	if(n)
	printf("%c",b[0]);
	for(i=1;i<n;i++)
		printf(", %c",b[i]);
	putchar(']');






	return  0;
}
int main(){
	int t;
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	scanf("%d",&t);
	for(int I=1;I<=t;I++){
		printf("Case #%d: ",I);
		solve();
		putchar('\n');
	}
	return 0;
}