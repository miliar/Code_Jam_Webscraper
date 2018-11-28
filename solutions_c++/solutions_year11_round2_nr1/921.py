#include<cstdio>
int t,n,w,a,aa;
char c[105][105];
double wp[105],op[105],oop[105],tt;
int main(){
	scanf("%d",&t);
	for (int z=1; z<=t; z++){
		scanf("%d",&n);
		for (int i=0; i<n; i++)
		    scanf("%s",c[i]);
		for (int i=0; i<n; i++){
			w=a=0;
		    for (int j=0; j<n; j++){
				if (c[i][j]!='.'){
				   ++a;
				   if (c[i][j]=='1') ++w;
				}
			}
			wp[i]=(w*1.0)/(a*1.0);
		}
		for (int i=0; i<n; i++){
			a=0; tt=0;
			for (int j=0; j<n; j++){
				if (c[i][j]!='.'){
				   ++a; aa=0; w=0;
				   for (int k=0; k<n; k++){
					   if (k!=i&&c[j][k]!='.'){
					      ++aa;
					      if (c[j][k]=='1') ++w;
						}
				   }
				   tt+=(w*1.0)/(aa*1.0);
 			    }
			}
			op[i]=tt/(a*1.0);
		}
		for (int i=0; i<n; i++){
			a=0; tt=0;
			for (int j=0; j<n; j++){
				if (c[i][j]!='.'){
				   ++a; tt+=op[j];
				}
			}
			oop[i]=tt/(a*1.0);
		}
		printf("Case #%d:\n",z);
		for (int i=0; i<n; i++)
			printf("%.8lf\n",(0.25*wp[i])+(0.5*op[i])+(0.25*oop[i]));
	}
	return 0;
}
