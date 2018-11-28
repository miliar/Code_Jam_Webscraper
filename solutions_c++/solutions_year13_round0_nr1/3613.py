#include<stdio.h>
int notfullvalues = 0;

int convertchar(char c) {
if(c == 'X') return 1;
else if (c == 'O') return 2;
else if (c == '.') { notfullvalues =1; return 0;}
else if (c == 'T')  return 3;
}

char convertint(int val) {

if(val == 1) return 'X';
else if (val == 2) return 'O';
else if (val == 0) { if ( notfullvalues == 1) {  return 'D'; } else return 'E';  }
}

void startTheLogic(FILE *fp, int round) {

    notfullvalues = 0;
    int array[4][4];
    char a, b , c , d, newline;
    int l , m , n ,o;
    bool success = false;
    for(int i =0 ; i< 4 ; i++) {
        fscanf(fp, "%c", &a);
        fscanf(fp, "%c", &b);
        fscanf(fp, "%c", &c);
        fscanf(fp, "%c", &d);
        
        //printf("round %d: chars: %c %c %c %c \n" , round,  a ,b ,c, d );
        

        l = convertchar(a);
        m = convertchar(b);
        n = convertchar(c);
        o = convertchar(d);

        int result = l&m&n&o;
        if(result && !success) {
                printf("Case #%d: %c won\n",round, convertint(result));
                success = true;
        } else {
            array[i][0] = l;
            array[i][1] = m;
            array[i][2] = n;
            array[i][3] = o;
        }
       fscanf(fp, "%c", &newline);
    }
   
  if(!success) { 
   for(int i =0 ; i< 4 ; i++) {
        int result = array[0][i] & array[1][i] & array[2][i] & array[3][i];
        if(result ) { 
              printf("Case #%d: %c won\n",round, convertint(result));
                return; 
                }
        }
     
    int result1 = array[0][0] & array[1][1] & array[2][2] & array[3][3];
    if(result1) {
                printf("Case #%d: %c won\n",round, convertint(result1));
                return;
          }
    
    int result2 = array[0][3]& array[1][2] & array[2][1] & array[3][0];
    if(result2) {
                printf("Case #%d: %c won\n",round, convertint(result2));
                return; 
        }
           
    if(notfullvalues == 0) { 
                printf("Case #%d: Draw\n", round);
                return;
    } else {
                printf("Case #%d: Game has not completed\n", round);
                notfullvalues = 0;
                return;        
        }
   }
}

int main() {

    FILE *fp = fopen("input.txt","r");
    int input;
    char newline;
    fscanf(fp, "%d", &input);
    fscanf(fp, "%c", &newline);
    int i =1;
    while(input > 0) {

        startTheLogic(fp, i++);
        char space;
        fscanf(fp, "%c", &space);
        --input;
    }


}
