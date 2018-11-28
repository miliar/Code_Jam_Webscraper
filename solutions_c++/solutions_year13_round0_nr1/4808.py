#include <cstdio>

char s[5];
char b[4][4];

int main(void){

    int t;	
    scanf("%d",&t);

    for(int z=1; z<=t; z++){

	for(int i=0; i<4; i++){
	    scanf("%s",s);
	    for(int j=0; j<4; j++) b[i][j]=s[j];
	}

	bool x_win=false;
	bool o_win=false;
	bool comp=true;

	// check win (h)
	for(int i=0; i<4; i++){
	    bool x_ok=true;
	    bool o_ok=true;
	    for(int j=0; j<4; j++){
		if(b[i][j]!='X' && b[i][j]!='T') x_ok=false;
		if(b[i][j]!='O' && b[i][j]!='T') o_ok=false;
	    }
	    
	    if(x_ok) x_win=true;
	    if(o_ok) o_win=true;
	}
		
	// check win (v)
	for(int j=0; j<4; j++){
	    bool x_ok=true;
	    bool o_ok=true;
	    for(int i=0; i<4; i++){
		if(b[i][j]!='X' && b[i][j]!='T') x_ok=false;
		if(b[i][j]!='O' && b[i][j]!='T') o_ok=false;
	    }    
	    if(x_ok) x_win=true;
	    if(o_ok) o_win=true;
	}
	
	// check win (l_diag)
	bool x_ok=true;
	bool o_ok=true;
	for(int i=0; i<4; i++){
	    if(b[i][i]!='X' && b[i][i]!='T') x_ok=false;
	    if(b[i][i]!='O' && b[i][i]!='T') o_ok=false;
	}
	if(x_ok) x_win=true;
	if(o_ok) o_win=true;

	// check win (r_diag)
	x_ok=true;
	o_ok=true;
	for(int i=0; i<4; i++){
	    if(b[i][3-i]!='X' && b[i][3-i]!='T') x_ok=false;
	    if(b[i][3-i]!='O' && b[i][3-i]!='T') o_ok=false;
	}
	if(x_ok) x_win=true;
	if(o_ok) o_win=true;
	
	for(int i=0; i<4; i++)
	    for(int j=0; j<4; j++) if(b[i][j]=='.') comp=false;

	printf("Case #%d: ", z);
	if(x_win) printf("X won\n");
	if(o_win) printf("O won\n");
	if((!x_win) && (!o_win)){
	    if(comp) printf("Draw\n");
	    else printf("Game has not completed\n");
	}

	gets(s);
    }
    return 0;
}
