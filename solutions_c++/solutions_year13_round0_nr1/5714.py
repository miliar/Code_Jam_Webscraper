#include <iostream>
#include <stdio.h>
using namespace std;
char a[4][4];
int main()
{
    int t,iii;
    cin>>t;
    for(iii=1;iii<=t;iii++){
        int nf=1,full=1;
        int i,j;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++){
                cin>>a[i][j];
                if(a[i][j]=='.')
                    full=0;
            }
        //row
        int flag=1;
        for(i=0;i<4&&nf;i++){
            flag=1;
            char aa;
            aa=a[i][0];
            for(j=1;j<4;j++){
                if(aa=='T')
                    aa=a[i][j];
                else{
                    if(a[i][j]!=aa&&a[i][j]!='T'){
                        flag=0;
                        break;
                    }
                }
            }
            if(flag&&aa!='.'){
                nf=0;
                cout<<"Case #"<<iii<<": "<<aa<<" won"<<endl;
                break;
            }
        }
        //cloumn
        for(i=0;i<4&&nf;i++){
            flag=1;
            char aa;
            aa=a[0][i];
            for(j=1;j<4;j++){
                if(aa=='T')
                    aa=a[j][i];
                else{
                    if(a[j][i]!=aa){
                        flag=0;
                        break;
                    }
                }
            }
            if(flag&&aa!='.'){
                nf=0;
                cout<<"Case #"<<iii<<": "<<aa<<" won"<<endl;
                break;
            }
        }
        flag=1;
        char aa;
        aa=a[0][0];
        for(i=1;i<4&&nf;i++){
            if(aa=='T')
                    aa=a[i][i];
                else{
                    if(a[i][i]!=aa){
                        flag=0;
                        break;
                    }
                }
        }
        if(flag&&nf&&aa!='.'){
            nf=0;
                cout<<"Case #"<<iii<<": "<<aa<<" won"<<endl;
            }
        flag=1;
        aa=a[3][0];
        for(i=1;i<4&&nf;i++){
            if(aa=='T')
                    aa=a[3-i][i];
                else{
                    if(a[3-i][i]!=aa){
                        flag=0;
                        break;
                    }
                }
        }
        if(flag&&nf&&aa!='.'){
            nf=0;
                cout<<"Case #"<<iii<<": "<<aa<<" won"<<endl;
            }

        if(nf){
            if(full)
                cout<<"Case #"<<iii<<": "<<"Draw"<<endl;
            else{
                cout<<"Case #"<<iii<<": "<<"Game has not completed"<<endl;
            }
        }
    }
}
