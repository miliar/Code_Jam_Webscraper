#include <stdio.h>
#include <map>
using namespace std;

string allO[]={"OOOO","TOOO","OTOO","OOTO","OOOT"};
string allX[]={"XXXX","TXXX","XTXX","XXTX","XXXT"};

map<char,int> hash;
enum RESULT{XWON,DRAW,OWON,NOT_COMPLETED};


RESULT JudgeK(char* input){

	int i,j;
	//‰¡‚ð’²‚×‚é
	char oneline_h[5];
	oneline_h[4]='\0';
	for(i=0;i<4;i++){
		memcpy(oneline_h,&input[i*4],4);
		//printf("%s\n",oneline_h);
		for(j=0;j<5;j++){
			if(strcmp(oneline_h,allO[j].c_str())==0 )return OWON;
			int ret=strcmp(oneline_h,allX[j].c_str());
			//printf("”»’è%s‚Æ%s‚Í%d\n",oneline_h,allX[j].c_str(),ret);
			if(ret==0){ return XWON;}
		}
	}
	//c‚ð’²‚×‚é
	for(i=0;i<4;i++){

		char oneline_v[5]={input[0*4+i],input[1*4+i],input[2*4+i],input[3*4+i],'\0'};
		for(j=0;j<5;j++){
			int ret=strcmp(oneline_v,allO[j].c_str());
			//printf("”»’è%s‚Æ%s‚Í%d\n",oneline_v,allO[j].c_str(),ret);
			if(ret==0) return OWON;

			if(strcmp(oneline_v,allX[j].c_str())==0) return XWON;
		}
	}

	//ŽÎ‚ß‚ð’²‚×‚é
	char oneline_d1[5]={input[0],input[5],input[10],input[15],'\0'};
	char oneline_d2[5]={input[3],input[6],input[9],input[12],'\0'};
	for(j=0;j<5;j++){
		if(strcmp(oneline_d1,allO[j].c_str())==0 )return OWON;
		if(strcmp(oneline_d1,allX[j].c_str())==0) return XWON;
	}
	for(j=0;j<5;j++){
		if(strcmp(oneline_d2,allO[j].c_str())==0) return OWON;
		if(strcmp(oneline_d2,allX[j].c_str())==0) return XWON;
	}

	//Ÿ”s‚ª‚È‚¢ê‡
	for(i=0;i<16;i++){
		if (input[i]=='.'){ return NOT_COMPLETED;}
	}

	return DRAW;

}

void main(){
	FILE* fp=fopen("A-large.in","r");
	char firstline[10];
	fgets(firstline,10,fp);
	int test_num=atoi(firstline);
	
	printf("testnum%d\n",test_num);
	FILE* wfp=fopen("output2.txt","w");
	
		for(int i=1;i<=test_num;i++){
			char input[17];
			int count=0;
			while(count<16){
				char c=fgetc(fp);
				if(c!='\n' && c!='\0'){
					input[count]=c;
					count++;
				}
			}
			
			input[16]='\0';
			/*puts("input");
			for(int k=0;k<4;k++){
				printf("%c,%c,%c,%c\n",input[k*4],input[k*4+1],input[k*4+2],input[k*4+3]);
			}
			*/
			fprintf(wfp,"Case #%d: ",i);
			switch(JudgeK(input)){
			case XWON:
				fprintf(wfp,"X won");
				break;
			case OWON:
				fprintf(wfp,"O won");
				break;
			case DRAW:
				fprintf(wfp,"Draw");
				break;
			case NOT_COMPLETED:
				fprintf(wfp,"Game has not completed");
				break;
			}
			fprintf(wfp,"\n");
		}//end test case
	fclose(fp);	
	
}