#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fcntl.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;
char arr[51][51];
int row;
int col;
FILE *fp;
void init()
{
    for(int i=0;i<51;i++)
    for(int j=0;j<51;j++)
    arr[i][j]=NULL;

    row=0;
    col=0;
}
void input()
{
    for(int i=0;i<row;i++)
    {char str[52];
        fscanf(fp,"%s",str);
    for(int j=0;j<col;j++)
    arr[i][j]=str[j];
    }
}
int main()
{fp=fopen("//home//karan//Downloads//input.txt","r");
freopen("//home//karan//Desktop//output.txt","w",stdout);
   char str[20];
fscanf(fp,"%s",str);
int n=atoi(str);
for(int l=0;l<n;l++)
    {
        init();
        char str1[20];
fscanf(fp,"%s",str1);
row=atoi(str1);
fscanf(fp,"%s",str1);
col=atoi(str1);


        input();
        for(int i=0;i<row-1;i++)
        {
            for(int j=0;j<col-1;j++)
            {
                if(arr[i][j]=='#'&&arr[i][j+1]=='#'&&arr[i+1][j]=='#'&&arr[i+1][j+1]=='#')
                {
                    arr[i][j]='/';
                    arr[i][j+1]='\\';
                    arr[i+1][j]='\\';
                    arr[i+1][j+1]='/';
                }
            }
        }
        cout<<"Case #"<<l+1<<":"<<endl;
        int flag=0;
        for(int i=0;i<row;i++)
        for(int j=0;j<col;j++)
        {
            if(arr[i][j]=='#')
            {flag=1;
                cout<<"Impossible\n";
                i=row-1;
                j=col-1;

            }
        }

        if(flag==0)
        { for(int i=0;i<row;i++)
            { for(int j=0;j<col;j++)
                {cout<<arr[i][j];
                }
              cout<<endl;
            }
        }
        }
      return 0;
}


