#include<cstdio>
#include<cstdlib>
#include<cstring>

int main()
{
	int numCases;
	int found=0;
	//char arr[]="XOT.";
	FILE *file;
	file = fopen("qras.out", "w");
	
	scanf("%d", &numCases);	
	for (int k=0; k<numCases; k++, found=0){	
		char state[5][5];
		int cntX=0, cntO=0, cntT=0;
		for (int i=0; i<4; i++){
			fscanf(stdin, "%s", state[i]);
		}
		/*
		for (int i=0; i<4; i++){
			if ((strcmp(state[i], "XXXX")==0)||(strcmp(state[i], "XXXT")==0)||(strcmp(state[i], "XXTX")==0)||(strcmp(state[i], "XTXX")==0)||(strcmp(state[i], "TXXX")==0)){
				fprintf(file, "Case #%d: X won\n", k+1);
				found=1;
				break;
			}else if ((strcmp(state[i], "OOOO")==0)||(strcmp(state[i], "OOOT")==0)||(strcmp(state[i], "OOTO")==0)||(strcmp(state[i], "OTOO")==0)||(strcmp(state[i], "TOOO")==0)){
				      fprintf(file, "Case #%d: O won\n", k+1);
					  found=1;
					  break;
			}
		}
		*/
		
		for (int i=0; i<4; i++){
			cntX=0, cntO=0, cntT=0;
			for (int j=0; j<4; j++){
				switch(state[i][j]){
					case 'X': cntX++;break;
					case 'O': cntO++;break;
					case 'T': cntT++;break;
					case '.': break;
				}
			}
			if ((cntX==4)||((cntX==3)&&(cntT==1))){
				fprintf(file, "Case #%d: X won\n", k+1);
				found=1;
				break;
			}else if ((cntO==4)||((cntO==3)&&(cntT==1))){
				fprintf(file, "Case #%d: O won\n", k+1);
				found=1;
				break;
			}		
		}
		
		if (!found){
			for (int i=0; i<4; i++){
				cntX=0, cntO=0, cntT=0;
				for (int j=0; j<4; j++){
					switch(state[j][i]){
						case 'X': cntX++;break;
						case 'O': cntO++;break;
						case 'T': cntT++;break;
						case '.': break;
					}
				}
				if ((cntX==4)||((cntX==3)&&(cntT==1))){
					fprintf(file, "Case #%d: X won\n", k+1);
					found=1;
					break;
				}else if ((cntO==4)||((cntO==3)&&(cntT==1))){
					fprintf(file, "Case #%d: O won\n", k+1);
					found=1;
					break;
				}		
			}
		}			
		
		if (!found){			
			cntX=0, cntO=0, cntT=0;
			for (int i=0; i<4; i++){
				switch(state[i][i]){
					case 'X': cntX++;break;
					case 'O': cntO++;break;
					case 'T': cntT++;break;
					case '.': break;
				}
			}
			if ((cntX==4)||((cntX==3)&&(cntT==1))){
				fprintf(file, "Case #%d: X won\n", k+1);
				found=1;
			}else if ((cntO==4)||((cntO==3)&&(cntT==1))){
				fprintf(file, "Case #%d: O won\n", k+1);
				found=1;
			}					
		}
		
		if (!found){			
			cntX=0, cntO=0, cntT=0;
			for (int i=0; i<4; i++){
				switch(state[i][3-i]){
					case 'X': cntX++;break;
					case 'O': cntO++;break;
					case 'T': cntT++;break;
					case '.': break;
				}
			}
			if ((cntX==4)||((cntX==3)&&(cntT==1))){
				fprintf(file, "Case #%d: X won\n", k+1);
				found=1;
			}else if ((cntO==4)||((cntO==3)&&(cntT==1))){
				fprintf(file, "Case #%d: O won\n", k+1);
				found=1;
			}					
		}
		
		if (!found){
			cntX=0, cntO=0, cntT=0;			
			for (int i=0; i<4; i++){
				for (int j=0; j<4; j++){
					if (state[i][j]=='.'){
						fprintf(file, "Case #%d: Game has not completed\n", k+1);
						found=1;
						break;
					}
				}
				if (found)
					break;
			}			
		}
		
		if (!found){
			fprintf(file, "Case #%d: Draw\n", k+1);
		}
		
	}	
	
	fclose(file);
	return 0;
}

