#include<fstream>
#define M 20000002
using namespace std;
int tt,cnt,ww[12];
bool c[M];
int is_new(int y);
int main()
{
	FILE *in,*out;
	in=fopen("input.txt","r");
	out=fopen("output.txt","w");
	int st,ed,zz,i,x,y,k,l,qq,m,d,pp;
	fscanf(in,"%d",&tt);
	for(zz=0;zz<tt;zz++){
		fscanf(in,"%d %d",&st,&ed);
		d=0;
		for(x=st;x<=ed;x++) c[x]=0;
		for(x=st;x<=ed;x++){
			c[x]=1;
			k=x; y=x; qq=1;
			while(k>0){
				qq*=10;
				k/=10;
			}
			qq/=10;
			k=x;
			cnt=0;
			while(k>0){
				l=y%10;
				y/=10;
				y+=qq*l;
				if(y>=st && y<=ed){
					if(c[y]==0 && is_new(y)==1){
						ww[cnt++]=y;
						d++;
					}
				}
				k/=10;
			}
		}
		fprintf(out,"Case #%d: %d\n",zz+1,d);
	}
	return 0;
}

int is_new(int y)
{
	int i;
	for(i=0;i<cnt;i++){
		if(ww[i]==y){
			return 0;
		}
	}
	return 1;
}