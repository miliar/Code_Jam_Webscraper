#include <iostream>
#include <string>
#include <numeric>
#include <cmath>
using namespace std;

FILE * pFile;

struct POINT{
	int ah,am, dh,dm;
	void take(){
		char a,b;
char s[12],v[3],v1[3],w1[3],w2[3];
//scanf("%d%c%d%d%c%d", &ah, &a,&am,&dh,&b,&dm);
        fgets (s, 100 , pFile);
int i;
i=0;	
v[0]=s[i++];
if(s[i]==':')
{v[1]='\n';i++;}
else{
v[1]=s[i++];i++;}

v1[0]=s[i++];
if(s[i]==':')
{v1[1]='\n';i++;}
else{
v1[1]=s[i++];i++;
}
w1[0]=s[i++];
if(s[i]==':')
{w1[1]='\n';i++;}
else{
w1[1]=s[i++];i++;
}
w2[0]=s[i++];
if(s[i]==':')
{w2[1]='\n';i++;}
else{
w2[1]=s[i++];
}
v[3]=v1[3]=w1[3]=w2[3]='\n';
ah=atoi(v);
am=atoi(v1);
dh=atoi(w1);
dm=atoi(w2);
//		printf("%s.....\t%d:%d\t%d:%d\n",s, ah,am,dh,dm);
	}
	void set(void){
		ah=25;am=25;dh=25;dm=25;
	}
	void put(){
//		printf("%d:%d\t%d:%d\n", ah,am,dh,dm);

	}
};

void sort (POINT C[],int n){
	int i,j,k,ah,am,dh,dm;
	for(i=0;i<n;++i)
		for(j=i+1;j<n;++j){
			if((C[i].ah >C[j].ah)||((C[i].ah ==C[j].ah)&& (C[i].am >C[j].am))){
				ah=C[i].ah;am=C[i].am;dh=C[i].dh;dm=C[i].dm;
				C[i].ah=C[j].ah;C[i].am=C[j].am;C[i].dh=C[j].dh;C[i].dm=C[j].dm;
				C[j].ah=ah;C[j].am=am;C[j].dh=dh;C[j].dm=dm;
			}
		}
}
POINT A[125],B[125];
int main(){
	int n,na,nb,t,i,j,k,h,m,a,b,c;
	int donea[125],doneb[125],ta,tb,done;                                                                              
char mystring [100],v[10],s[10],s1[10],s2[10];
        pFile = fopen ("input", "r");
        fgets (mystring , 100 , pFile);
n=atoi(mystring);	
//scanf("%d", &n);
	for(i=0;i<n;++i){
		ta=0;tb=0,done=0;
		for(j=0;j<125;++j){
			donea[j]=0;doneb[j]=0;
		}

        fgets (v, 100 , pFile);
t=atoi(v);	
        fgets (s, 100 , pFile);
		for(k=0;k<101;++k){
s1[k]=s[k];
 if (s[k]==' ') break;
}
	s1[k]='\n';	
j=0;
k++;
while(k<strlen(s)){
 if (s[k]==' ') break;
s2[j]=s[k]; 
++k;
++j;
 if (s[k]==' ') break;
}
	s2[k]='\n';	
na=atoi(s1);	
       // fgets (w, 100 , pFile);
nb=atoi(s2);	
//		printf("%d\t%d\t%d\n", t,na,nb);
		for(j=0;j<101;++j)
			A[j].set();
		for(j=0;j<101;++j)
			B[j].set();
		for(j=0;j<na;++j)
			A[j].take();
		for(j=0;j<nb;++j)
			B[j].take();

		sort(A,na);
		sort(B,nb);
		j=0;k=0;
		while(done<1)			{
			if((A[j].ah <B[k].ah)||((A[j].ah ==B[k].ah)&& (A[j].am <B[k].am))){
				ta++;
				donea[j]=1;
				while(k<nb && j<na){
					h=A[j].dh;
					m=A[j].dm+t;
					if(m>59) {
						h++;
						m=m-60;
					}
					while((doneb[k]==1)||((h >B[k].ah)||((h ==B[k].ah)&& (m >B[k].am))))++k;
					if(k<nb){
						doneb[k]=1;
						h=B[k].dh;
						m=B[k].dm+t;
						if(m>59) {
							h++;
							m=m-60;
						}
						while((donea[j]==1)||((h >A[j].ah)||((h ==A[j].ah)&& (m >A[j].am))))++j;
						if(j<na)
							donea[j]=1;
					}
				}

			}
			else{
				tb++;
				doneb[k]=1;
				while(k<nb && j<na){
					h=B[k].dh;
					m=B[k].dm+t;
					if(m>59) {
						h++;
						m=m-60;
					}
					while((donea[j]==1)||((h >A[j].ah)||((h ==A[j].ah)&& (m >A[j].am))))++j;
					if(j<na){
						donea[j]=1;
						h=A[j].dh;
						m=A[j].dm+t;
						if(m>59) {
							h++;
							m=m-60;
						}
						while((doneb[k]==1)||((h >B[k].ah)||((h ==B[k].ah)&& (m >B[k].am))))++k;
						if(k<nb){
							doneb[k]=1;
						}
					}
				}

			}
//		printf("Result..............:%d:%d\n ",ta, tb);
			j=0;k=0;
			while(donea[j]==1&& j<na) ++j;
			while(doneb[k]==1&& k<nb) ++k;

			while (k<nb&&j==na) {
				if(doneb[k]==0){doneb[k]=1;tb++;}
				++k;
			}

			while(j<na&&k==nb)
			{
				if(donea[j]==0){donea[j]=1;ta++;
}
				++j;
			}
			if(k==nb && j==na) {done=1;}
		}
		printf("Case #%d: %d %d\n",i+1,ta, tb);
	}
	return 0;
}
