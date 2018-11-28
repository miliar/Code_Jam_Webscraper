/* 
 * File:   main.cpp
 * Author: pavan
 *
 * Created on May 22, 2010, 6:46 AM
 */

#include <stdlib.h>
#include<iostream>

/*
 * 
 */

using namespace std;


class Table{
    char tab[50][50];
    int n;
    int k;
    
public:
    void init();
    void rotate();
    char calculate();
};



void Table::init(){
    cin>>n;
    cin>>k;
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>tab[i][j];
        }
    }
    
}

void Table::rotate(){
    for(int i=0;i<n;i++){
        for(int j=n-1;j>=0;j--){
            if(tab[i][j]!='.'){
                int x=j;
                while(x+1!=n && tab[i][++x]=='.'){
                    tab[i][x]=tab[i][x-1];
                    tab[i][x-1]='.';
                }
            }
        }
    }
}
      

char Table::calculate(){
    //row
    int r=0,b=0;
    int count;
    
    for(int i=0;i<n;i++){
        count=0;
        for(int j=0;j<n;j++){
            if(tab[i][j]=='B'){
                count++;
                if(count==k)
                    b=1;
            }
            else
                count=0;
        }
    }

    for(int i=0;i<n;i++){
        count=0;
        for(int j=0;j<n;j++){
            if(tab[i][j]=='R'){
                count++;
                if(count==k)
                    r=1;
            }
            else
                count=0;
        }
    }


    //colounn

    for(int i=0;i<n;i++){
        count=0;
        for(int j=0;j<n;j++){
            if(tab[j][i]=='B'){
                count++;
                if(count==k)
                    b=1;
            }
            else
                count=0;
        }
    }


    for(int i=0;i<n;i++){
        count=0;
        for(int j=0;j<n;j++){
            if(tab[j][i]=='R'){
                count++;
                if(count==k)
                    r=1;
            }
            else
                count=0;
        }
    }


    //left diognal

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int x=i;
            int y=j;
            count=0;
            for(int xyz=0;xyz<k;xyz++){
                if(tab[x][y]=='B' && x<n && y<n){
                    count++;
                    x++;
                    y++;
                }
            }
            if(count==k)
                b=1;
        }
    }


    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int x=i;
            int y=j;
            count=0;
            for(int xyz=0;xyz<k;xyz++){
                if(tab[x][y]=='R' && x<n && y<n){
                    count++;
                    x++;
                    y++;
                }
            }
            if(count==k)
                r=1;
        }
    }


    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int x=i;
            int y=j;
            count=0;
            for(int xyz=0;xyz<k;xyz++){
                if(tab[x][y]=='R' && x<n && y>=0){
                    count++;
                    x++;
                    y--;
                }
            }
            if(count==k)
                r=1;
        }
    }


    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int x=i;
            int y=j;
            count=0;
            for(int xyz=0;xyz<k;xyz++){
                if(tab[x][y]=='B' && x<n && y>=0){
                    count++;
                    x++;
                    y--;
                }
            }
            if(count==k)
                b=1;
        }
    }


    if( r==1 && b== 1)
        return('E');
    else if(r==0 && b==0)
        return('N');
    else if(r==1 && b==0)
        return('R');
    else if(r==0 && b==1)
        return('B');


}
        
        
int main(int argc, char** argv) {
    
    int t;
    Table table;
    char ans;

    cin>>t;
    
    for(int i=0;i<t;i++){
        table.init();
        table.rotate();
        ans = table.calculate();
        cout<<"Case #"<<i+1<<": ";
        if(ans=='E')
            cout<<"Both\n";
        else if(ans=='B')
            cout<<"Blue\n";
        else if(ans=='R')
            cout<<"Red\n";
        else if(ans=='N')
            cout<<"Neither\n";
    }

    return (EXIT_SUCCESS);
}

