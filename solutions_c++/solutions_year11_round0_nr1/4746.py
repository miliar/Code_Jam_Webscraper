#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main(){
	//Variable declarations 
	int T,N,opb[100],bpb[100],ost[100],bst[100],o1,o2,o3,b1,b2,b3;
	int op=0,bp=0,no,opn,bpn,st[100],opos=1,bpos=1,time=0,tchk;
	char col;
	FILE* fi;
	FILE* fo;
	
	//Opening files and reading input after variable intialisations
	fi=fopen("A-in.txt","r");
	fo=fopen("A-out.txt","w");
	fscanf(fi,"%d ",&T);
	for(int i=0;i<T;i++){
		op=0;bp=0;
		for(int k=0;k<100;k++){
			opb[k]=0;bpb[k]=0;ost[k]=0;bst[k]=0;st[k]=0;
		}
		fscanf(fi,"%d ",&N);
		for(int j=0;j<N;j++){
			fscanf(fi,"%c %d ",&col,&no);
			if(col=='O'){
				opb[op]=no;ost[op]=j;op++;
			}
			if(col=='B'){
				bpb[bp]=no;bst[bp]=j;bp++;
			}
		}
		
		/*
		for(int l=0;l<N;l++){
			printf("%d %d %d %d %d \n",opb[l],ost[l],bpb[l],bst[l],st[l]);
		}
		cout<<endl;
		*/
		opn=op;//cout<<opn<<endl;
		bpn=bp;//cout<<bpn<<endl;
		op=0;bp=0;time=0;opos=1;bpos=1;
		//The actual algo : Iterate till you do all the buttons
		while(!(op==opn && bp==bpn)){
			tchk=0;o1=0;o2=0;b1=0;b2=0;o3=0;b3=0;
			if(op!=opn){
				if(opb[op]>opos){
					o1++;tchk++;
				}
				if(opb[op]<opos){
					o2++;tchk++;
				}
				if(opb[op]==opos){
					if(ost[op]==0 || st[ost[op]-1]==1){
						//cout<<"chkO"<<endl;
						tchk++;o3++;
					}
				}
			}
			if(bp!=bpn){
				if(bpb[bp]>bpos){
					b1++;tchk++;
				}
				else if(bpb[bp]<bpos){
					b2++;tchk++;
				}
				else if(bpb[bp]==bpos){
					if(bst[bp]==0 || st[bst[bp]-1]==1){
						//cout<<"chkB"<<endl;
						tchk++;b3++;
					}
				}
			}
			if(tchk!=0)time++;
			if(o1!=0)opos++;
			if(o2!=0)opos--;
			if(o3!=0){st[ost[op]]=1;op++;}
			if(b1!=0)bpos++;
			if(b2!=0)bpos--;
			if(b3!=0){st[bst[bp]]=1;bp++;}
			
		//	printf("%d %d %d %d %d\n",opos,op,bpos,bp,time);
		}
		fprintf(fo,"Case #%d: %d \n",i+1,time);
		//cout<<endl;
	}
	
	fclose(fi);
	fclose(fo);
	return 0;
}
