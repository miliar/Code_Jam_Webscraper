#include <cstdio>
#include <algorithm>

using namespace std;

char map[4][4]={0};
int find(char c,int x, int y,int total,int dirn);

int main(){
FILE* input;
FILE* output;

input =  fopen("A-small-attempt0.in.","r");
output = fopen("output.in","w");

int num=0,sumX=0,sumY=0,finished=0,draw=0; //0 means not finished, 1 means finished, draw=0, means draw, draw = 1 means game not finished
fscanf(input,"%d",&num);

for(int n=1;n<=num;n++){
for(int i=0;i<4;i++){
    for(int j=0;j<4;j++){
        fscanf(input,"%c",&map[i][j]);
        if(map[i][j]!='T'&&map[i][j]!='.'&&map[i][j]!='X'&&map[i][j]!='O'){
            j--;
        }
    }
}

for(int i=0;i<4&&finished!=1;i++){
    for(int j=0;j<4&&finished!=1;j++){
        if(map[i][j]=='X'){
            sumX=find('X',i,j,1,1);
            if(sumX==4){
                finished=1;
                break;
            }
            sumX=find('X',i,j,1,2);
            if(sumX==4){
                finished=1;
                break;
            }
            sumX=find('X',i,j,1,3);
            if(sumX==4){
                finished=1;
                break;
            }
            sumX=find('X',i,j,1,4);
            if(sumX==4){
                finished=1;
                break;
            }
        }
        else if(map[i][j]=='O'){
            sumY=find('O',i,j,1,1);
            if(sumY==4){
                finished=1;
                break;
            }
            sumY=find('O',i,j,1,2);
            if(sumY==4){
                finished=1;
                break;
            }
            sumY=find('O',i,j,1,3);
            if(sumY==4){
                finished=1;
                break;
            }
            sumY=find('O',i,j,1,4);
            if(sumY==4){
                finished=1;
                break;
            }
        }
        else if(map[i][j]=='.'){
            draw=1;
        }

    }
}

if(finished==1){
    if(sumX==4){
        fprintf(output,"Case #%d: X won\n",n);
    }
    else if(sumY==4){
         fprintf(output,"Case #%d: O won\n",n);
    }
}
else{
    if(draw==0){
        fprintf(output,"Case #%d: Draw\n",n);
    }
    else if(draw==1){
        fprintf(output,"Case #%d: Game has not completed\n",n);
    }
}
sumX=0;
sumY=0;
finished=0;
draw=0;
}

fclose(input);
fclose(output);
}

int find(char c,int x, int y,int total,int dirn){
    if((map[x][y+1]==c||map[x][y+1]=='T')&&(dirn==0||dirn==1)&&(x<4&&y<3)){
        find(c,x,y+1,total+1,1);
    }
    else if((map[x+1][y]==c||map[x+1][y]=='T')&&(dirn==0||dirn==2)&&(x<3&&y<4)){
        find(c,x+1,y,total+1,2);
    }
    else if((map[x+1][y+1]==c||map[x+1][y+1]=='T')&&(dirn==0||dirn==3)&&(x<3&&y<3)){
        find(c,x+1,y+1,total+1,3);
    }
     else if((map[x+1][y-1]==c||map[x+1][y-1]=='T')&&(dirn==0||dirn==4)&&(x<3&&y>0)){
        find(c,x+1,y-1,total+1,4);
    }
    else{
        return total;
    }
}
