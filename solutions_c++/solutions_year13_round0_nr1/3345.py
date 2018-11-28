#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>

using namespace std;
bool UNLEFT = false;
int has_won(vector<string> str){
  //  printf ("here...");
    int o = 0 , x = 0 ;
    for(int i=0;i<4;i++){
        o = x = 0;
        for(int j=0;j<4;j++){
            if(str[i].at(j) == 'O')
                o++;
            else if(str[i].at(j) == 'X')
                x++;
            else if(str[i].at(j) == 'T'){
                x++; o++;
            } else 
                UNLEFT = true;
        }
        if( o == 4)
            return 1;
        else if(x == 4)
            return 2;
    }
    for(int i=0;i<4;i++){
        o = x = 0;
        for(int j=0;j<4;j++){
            if(str[j].at(i) == 'O')
                o++;
            else if(str[j].at(i) == 'X')
                x++;
            else if(str[j].at(i) == 'T'){
                x++; o++;
            } else 
                UNLEFT = true;
        }
        if( o == 4)
            return 1;
        else if(x == 4)
            return 2;
    }
    o = x = 0;
    for(int i=0;i<4;i++){
            if(str[i].at(i) == 'O')
                o++;
            else if(str[i].at(i) == 'X')
                x++;
            else if(str[i].at(i) == 'T'){
                x++; o++;
            } else 
                UNLEFT = true;
    }
    if( o == 4)
        return 1;
    else if(x == 4)
        return 2;
    o = x  =0;
    for(int i=0;i<4;i++){
            if(str[i].at(3-i) == 'O')
                o++;
            else if(str[i].at(3-i) == 'X')
                x++;
            else if(str[i].at(3-i) == 'T'){
                x++; o++;
            } else 
                UNLEFT = true;
    
    }
    if( o == 4)
        return 1;
    else if(x == 4)
        return 2;
    return 3;


}
int main(){
    int cases;
    int obh;
    scanf("%d",&cases);
    obh = cases;
    string faltu;
    getline(cin, faltu, '\n'); 
    while(cases--){
        UNLEFT = false;
        vector<string> str;
        string tmp;
        for(int i=0;i<4;i++) {
            getline( std::cin, tmp, '\n' );
            str.push_back(tmp);
   //        cout << str[i] << endl;
        }
        getline( std::cin, faltu, '\n' );
        int ret = has_won(str);
        if(ret == 1) 
            printf("Case #%d: O won\n", obh-cases);
        else if(ret == 2)
            printf("Case #%d: X won\n", obh-cases);
        else { 
            if( UNLEFT )
                printf("Case #%d: Game has not completed\n", obh-cases);
            else
                printf("Case #%d: Draw\n", obh-cases);
        }
    }

}
