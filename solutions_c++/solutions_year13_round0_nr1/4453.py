#include<cstdio>
#include<iostream>

using namespace std;

char mat[4][4];

bool cXO(char c){

    int i,j,cntx = 0,cntt = 0;

    for( i = 0 ; i < 4; i++){

        cntx = 0;cntt =0;
        for(j = 0 ; j < 4; j++){
            if(mat[i][j] == c)
                cntx++;
            else if(mat[i][j] == 'T')
                cntt++;
        }
        if(cntx == 4 || ( cntx ==3 && cntt == 1))
            return true;
    }
    for( i = 0 ; i < 4; i++){

        cntx = 0;cntt =0;
        for(j = 0 ; j < 4; j++){
            if(mat[j][i] == c)
                cntx++;
            else if(mat[j][i] == 'T')
                cntt++;
        }
        if(cntx == 4 || ( cntx ==3 && cntt == 1))
            return true;
    }
    cntx = 0; cntt = 0;
    for( i = 0 ; i < 4 ; i++){
        if(mat[i][i] == c)
            cntx++;
        else if(mat[i][i] == 'T')
            cntt++;
    }
    if(cntx == 4 || ( cntx ==3 && cntt == 1))
            return true;
    cntx = 0; cntt = 0;
    for( i = 0 ; i < 4 ; i++){
        if(mat[i][3-i] == c)
            cntx++;
        else if(mat[i][3-i] == 'T')
            cntt++;
    }
    if(cntx == 4 || ( cntx ==3 && cntt == 1))
            return true;
    return false;

}

bool chkCmplt(){

    for( int  i = 0 ; i < 4; i ++){
        for( int j = 0 ; j < 4 ; j ++){
            if(mat[i][j] == '.')return false;
        }
    }
    return true;
}
int main(){


    int t,i,j,k;
    char tmp[10],cc;
    scanf("%d",&t);
    //fflush(stdin);
    for( j =1; j<= t ; j++){

        //scanf("%s",tmp);
        i =0;
        while(i<16)
        {
            if((cc = getchar()) != '\n'){
                mat[i/4][i%4] = cc;
                //printf("%c",cc);
                i++;
            }
        }
       /* for( i = 0 ; i < 4; i++)
        {
            for(k = 0 ; k < 4 ; k ++)
            {
                printf("%c",mat[i][k]);
            }

            cout<<endl;

        }*/
        if(cXO('X')){
            printf("Case #%d: X won\n",j);
        }
        else if(cXO('O')){
            printf("Case #%d: O won\n",j);
        }
        else if(chkCmplt()){
            printf("Case #%d: Draw\n",j);
        }
        else
            printf("Case #%d: Game has not completed\n",j);


    }
    return 0;
}
