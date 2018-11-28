#include<stdio.h>
#include<string.h>
#include <ctype.h>


int l,d,n; //com var
int lit[100];
int nr_pos;
int sols;
char dict[5001][100]; //dictionar de termeni
char posib[5001][100];
char st[100];


void cit();

int main() {
	
	//freopen("date.in", "r", stdin);
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	
	cit();

	return 0;
}


int valid () {


	for(int i=1; i<=d; i++) {
		//printf("vv%s - %s \n",st,dict[i]);
		if(strcmp(st,dict[i])==0)
			return 1;
	}
			
	return 0;

}


int isok(int k) {
		for(int i=1; i<=d; i++) {
			if(strncmp(st,dict[i],k)==0)
				return 1;
		}
			
	return 0;
}

void generate(int k) {


	if(k==l+1) { 
		
		
//		printf(" %s ",st);
		if(valid()) {
//			printf("xx%s\n", st);
			sols++;
		}
		

	} else {
		

	for(int i=0; i<strlen(posib[k]); i++) {
		st[k-1]=posib[k][i];
		//st[k]=i;
		//printf("%c",st[k]);
		if(isok(k))
			generate(k+1);
	}
	
	}

}


void go(int caz) {
	
	char tmp[255];
	gets(tmp);
	
	//printf("%s\n",tmp);
	
	nr_pos=0;
	sols=0;
	int in_param=0, begin=0;
	
	/*
  	if(tmp[0]=='(') {
  		in_param=1;
  		begin=1;
  		nr_pos=1;
  	}
  	*/
  	
  	
  	for(begin=0; begin<strlen(tmp); begin++) {
  		
  		if(isalpha(tmp[begin]))  {
  			if(!in_param) 
  				nr_pos++;

  				
  			//strcat(posib[nr_pos],tmp[begin]);
  			int gamma=strlen(posib[nr_pos]);
  			posib[nr_pos][gamma]=tmp[begin];
  			posib[nr_pos][gamma+1]=NULL;	
  			
  		} else {
  		
  			if(tmp[begin]=='(') {
  				in_param=1;
  				//if(strlen(posib[nr_pos])-1)
  				nr_pos++;
  			}
  			else {
  				in_param=0;
  			}
  		}
  	
  	}
  	
  	
  	//printf("pos: %d\n", nr_pos);
  	
  	//for(int i=1; i<=nr_pos; i++)
  	//	printf("%s\n",posib[i]);
  		
  		
  	generate(1);
		
	printf("Case #%d: %d\n", caz, sols);
	//printf("----------------\n");
	memset(posib,NULL,sizeof(posib));
	
}

void cit() {
	
	scanf("%d %d %d", &l, &d, &n);
	

	for(int j=0; j<=d; j++) {
		
		gets(dict[j]);
		
	}
	
	for(int i=1; i<=n; i++) {
		
		go(i);
		
	}
	
}



