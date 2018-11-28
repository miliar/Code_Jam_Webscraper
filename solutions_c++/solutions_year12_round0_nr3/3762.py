#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
int main(){
	int t,i,a,b,x[10],j,u,v,w,s,sum;
	FILE *fp1,*fp2;
	fp1=fopen("C-large.in","r");
	fp2=fopen("trying4.txt","w");
	vector <int> z;
	fscanf(fp1,"%d",&t);
	for(i=1;i<=t;i++){
		fscanf(fp1,"%d%d",&a,&b);
		sum=0;
		for(j=a;j<=b;j++){
			v=0;
			for(u=j;u!=0;u=(u/10)){
				x[v]=(u%10);
				v++;
			}
			z.resize(0);
			for(u=(v-1);u>=0;u--){
				s=0;
				for(w=u;w>=0;w--){
					s=s*10+x[w];
				}
				for(w=(v-1);w>u;w--){
					s=s*10+x[w];
				}
				if((s>j)&&((s>=a)&&(s<=b))){
					for(w=0;w<z.size();w++){
						if(z[w]==s)
							break;
					}
					if(w==z.size()){
						z.push_back(s);
						sum=sum+1;
					}	
				}
			}
		}
		fprintf(fp2,"Case #%d: %d\n",i,sum);
	}
	fclose(fp1);
	fclose(fp2);
	return(0);
}	

