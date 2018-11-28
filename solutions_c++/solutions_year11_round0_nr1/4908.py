#include <iostream>
using namespace std;

int main(void){
	int t, i, j, k, num[101]={0} ,n, sum, ro_O[100]={0}, ro_R[100]={0},O, R, chk, chk2;
	char c[101]={0};
	FILE *fp=fopen("output.txt","w");
	cin >>t;
	
	for(k=0;k<t;k++){
		O=R=1;
		chk=chk2=0;
		cin >>n;
		sum=n;
		for(i=0;i<n;i++){
			cin >>c[i] >>num[i];
			if(c[i]=='O')
				ro_O[chk++]=num[i];
			else
				ro_R[chk2++]=num[i];
		}
		chk=chk2=0;
		for(i=0;i<n;i++){
			if(c[i]=='O'){
				while(O!=num[i]){
					if(O<num[i])
						O++;
					else
						O--;
					if(R<ro_R[chk2])
						R++;
					else if(R>ro_R[chk2])
						R--;
					sum++;
				}
				if(R<ro_R[chk2])
					R++;
				else if(R>ro_R[chk2])
					R--;
				chk++;
			}
			else{
				while(R!=num[i]){
					if(R<num[i])
						R++;
					else
						R--;
					if(O<ro_O[chk])
						O++;
					else if(O>ro_O[chk])
						O--;
					sum++;
				}
				if(O<ro_O[chk])
					O++;
				else if(O>ro_O[chk])
					O--;
				chk2++;
			}
		}
		cout <<"Case #" <<k+1 <<": " <<sum <<endl;
		fprintf(fp, "Case #%d: %d\n",k+1, sum);
	}
	fclose(fp);
	return 0;
}