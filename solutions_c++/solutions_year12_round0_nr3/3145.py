#include<iostream>
#include<cstdio>
using namespace std;
int len(int n){
	int l=0;
	while(n>0){
		n=n/10;
		l++;
	}
	return l;
}

void array(int n,int nl,int* na){
	int d;
	for(int i=0;i<nl;i++){
		d=n%10;
		na[nl-i-1]=d;
		n=n/10;
		//cout<<nl-i-1<<" "<<d<<endl;
	}
}
void recycle(int l,int* ma){
	int ma0=ma[0];
	for (int i=1;i<l;i++){
		ma[i-1]=ma[i];
	}
	ma[l-1]=ma0;
}
int areeq(int l,int* ma,int* na){
	for(int i=0;i<l;i++){
		if(ma[i]!=na[i]){
			return 0;
		}
	}
	return 1;
}

int isrec(int n,int m){
	int nl=len(n);
	//cout<<"nl "<<nl<<endl;
	int ml=len(m);
	//cout<<"ml "<<ml<<endl;	
	if(nl==ml){
		int na[nl],ma[ml];
		array(n,nl,na);
		array(m,ml,ma);
		//for(int j=0;j<ml;j++){
		//	cout<<j<<" "<<na[j]<<" "<<ma[j]<<endl;
		//}
		for(int i=0;i<ml-1;i++){
			recycle(ml,ma);
			if(areeq(ml,ma,na)){
				return 1;
			}
		}
		return 0;
	}
	else{ 
		return 0;
	}
}


int main(){
int t,count,a,b;
FILE* fin;
FILE* fo;
fin=fopen("B.in","r");
fo=fopen("B.out","w");
fscanf(fin,"%d",&t);
for(int i=0;i<t;i++){
	count=0;
	fscanf(fin,"%d %d",&a,&b);
	//printf("%d %d \n",a,b);
	for(int n=a;n<=b;n++){
		for (int m=n+1;m<=b;m++){
			if(isrec(n,m)){
				count=count+1;
			}
		}
	}	
	
	fprintf(fo,"Case #%d: %d\n",i+1,count);

}

//cout<<isrec(12,21)<<endl;
//int na[2];
//array(12,2,na);	
//cout<<na[0]<<" "<<na[1]<<endl;

fclose(fin);
fclose(fo);
return 0;
}
