#include<iostream.h>
#include<fstream.h>
int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("input.txt");
    f2.open("output.txt");


    int t;
    f1>>t;
    int k=1;
    while(t--){
        int r,c;
        f1>>r>>c;

  char arr[51][51];
            char ans[50][50];
                    for(int i=0;i<r;i++){
                        int j;
                        for( j=0;j<c;j++){
                            f1>>arr[i][j];
                        }
                        arr[i][j]='.';

                    }
                    for(int i=0;i<c;i++)
                    {
                        arr[r][i]='.';
                    }

       for(int i=0;i<r;i++){
           for(int j=0;j<c;j++){
               ans[i][j]='*';
           }
       }


            int flag=0;
                for(int i=0;i<r;i++){
                for(int j=0;j<c;j++){
                    if(ans[i][j]=='*'&&(arr[i][j]=='#'&&arr[i][j+1]=='#'&&arr[i+1][j]=='#'&&arr[i+1][j+1]=='#'))
                    {
                        ans[i][j]='/';
                        ans[i][j+1]=(char)92;
                        ans[i+1][j]=(char)92;
                        ans[i+1][j+1]='/';
                    }
                    else if(arr[i][j]!='.'){
                        if(ans[i][j]=='*'&&!(arr[i][j]=='#'&&arr[i][j+1]=='#'&&arr[i+1][j]=='#'&&arr[i+1][j+1]=='#')){
                            flag=1;
                            break;
                        }
                    }
                    else if(arr[i][j]=='.'){
                        ans[i][j]='.';}
                }
                if(flag==1){
                    break;
                }
                }

                if(flag==1){
                    f2<<"Case #"<<k<<":\n";
                    f2<<"Impossible\n";
                }
                else {
                    f2<<"Case #"<<k<<":\n";

                    for(int i=0;i<r;i++){
                        for(int j=0;j<c;j++){
                            f2<<ans[i][j];
                        }
                    f2<<"\n";
                    }
                }
    k++;
    }
}




