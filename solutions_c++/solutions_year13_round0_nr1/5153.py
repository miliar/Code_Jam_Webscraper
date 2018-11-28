#include<iostream>
#include<fstream>
using namespace std;

int det(char C[][5]){
    int i=0,j=0;
    char tmp;
    int ret=0,D=0;
    //1:X won;2:O won;3:Draw 0:not completed
    for(i=0;i<4;i++){
    for(j=0;j<4;j++){
		if(C[i][j]=='.'){ret++;break;}
    }
    }
    if(ret==0)D=1;

    for(i=0;i<4;i++){
    ret=0;
    tmp=C[i][0];
    if(tmp=='X')ret=1;
    else if(tmp=='O')ret=2;
    else if(tmp=='.')continue;
    else if(tmp=='T'){
		tmp=C[i][1];
		if(tmp=='X')ret=1;
        else if(tmp=='O')ret=2;
        else if(tmp=='.')continue;
	}
		

    for(j=1;j<4;j++){
    if((C[i][j]!=tmp)&&(C[i][j]!='T')){
    ret=0;
    break;
    }
    }
    if(ret!=0)return ret;
    }
    for(i=0;i<4;i++){
    ret=0;
    tmp=C[0][i];
    if(tmp=='X')ret=1;
    else if(tmp=='O')ret=2;
    else if(tmp=='.')continue;
    else if(tmp=='T')
	{
		tmp=C[1][i];
		if(tmp=='X')ret=1;
        else if(tmp=='O')ret=2;
        else if(tmp=='.')continue;
	}

    for(j=1;j<4;j++){
    if((C[j][i]!=tmp)&&(C[j][i]!='T')){
    ret=0;
    break;
    }
    }
    if(ret!=0)return ret;
    }

    tmp=C[0][0];
    if(tmp=='X')ret=1;
    else if(tmp=='O')ret=2;
    else if(tmp=='.')ret=0;
    else if(tmp=='T')
	{
		tmp=C[1][1];
		if(tmp=='X')ret=1;
        else if(tmp=='O')ret=2;
        else if(tmp=='.')ret=0;
	}

    for(i=1;i<4;i++){
    if((C[i][i]!=tmp)&&(C[i][i]!='T')){
    ret=0;
    break;
    }
    }
    if(ret!=0)return ret;

    tmp=C[0][3];
    if(tmp=='X')ret=1;
    else if(tmp=='O')ret=2;
    else if(tmp=='.')ret=0;
    else if(tmp=='T')
	{
		tmp=C[1][2];
		if(tmp=='X')ret=1;
        else if(tmp=='O')ret=2;
        else if(tmp=='.')ret=0;
	}

    for(i=1;i<4;i++){
    if((C[i][3-i]!=tmp)&&(C[i][3-i]!='T')){
    ret=0;
    break;
    }
    }
    if(ret!=0)return ret;

    if(D==1)return 3;
    else return 0;
}
      

/*
Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won


*/
void main(){
	fstream infile;
	ofstream outfile;
	infile.open("A-large.in");
	outfile.open("output.txt");
	int T,tmp;
	char test[4][5];
	infile>>T;
	for(int i=1;i<=T;i++){
		infile>>test[0]>>test[1]>>test[2]>>test[3];
	    tmp=det(test);
		if(tmp==1)outfile<<"Case #"<<i<<": "<<"X won"<<endl;
	    else if(tmp==2)outfile<<"Case #"<<i<<": "<<"O won"<<endl;
	    else if(tmp==3)outfile<<"Case #"<<i<<": "<<"Draw"<<endl;
	    else outfile<<"Case #"<<i<<": "<<"Game has not completed"<<endl;
	}
	infile.close();
	outfile.close();
	return;
}
	
    