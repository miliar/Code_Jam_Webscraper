#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
 
using namespace std;

using namespace std;


#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

int x[1000];
int y[1000];

string str;
int length;
int index;

int read_int_from_char(char in[],int l,int ret[]){
  int i,n,fg,mfg;
  if(l<0) {for(i=0;;i++) if(in[i]<' ') break; l=i;}
  n=0; fg=0; mfg=0; ret[0]=0;
  rep(i,l+1){
    if(in[i]=='-'){mfg=1; continue;}
    if(isdigit(in[i])){ret[n]=ret[n]*10+in[i]-'0'; fg=1; continue;}
    if(!fg) continue;
    fg=0; if(mfg){ret[n]=-ret[n]; mfg=0;}
    ret[++n]=0;
  }
  return n;
}


void parse()
{
    int i;
    length = str.size();
    for(i=0;i<length;i++)
    {
        x[i] = str[i]-'0';
        //y[i] = str[i]-'0';
    }
}

void sorting(int a[],int len)
{
    int i,j,tmp;

    for(i=0;i<len-1;i++)
    {
        for(j=i+1;j<len;j++)
        {
            if(a[i] > a[j])
            {
                tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;

            }
        }
    }
}

int find_next(int t)
{
    int max,j,min,maxx;

    max = x[t];

    
    j = t+1;

    for(;j<length;j++)
    {
        if(max < x[j])
        {
            max = x[j];
        }
    }

    if(max == x[t])
        return max;

    j = t+1;

    min = x[t];

    for(;j<length;j++)
    {
        if(x[j] > min && x[j] <= max)
        {
            max = x[j];
            index = j;
        }
    }

    return max;


}


main()
{
    int cases,t,i,small,j;
    char tmp[10];
    int temp;
    bool flag;

    ifstream fin;
    ofstream fout;


    fin.open ("in.txt", ifstream::in);

    fout.open("output.txt");



    fin >> cases;


    getline(fin, str);
    
    t = 1;

    
    
    while(cases--)
    {

        str.resize(0);

        getline(fin, str);
        parse();
        flag = false;
        for(i=length-2;i>=0;i--)
        {
            small = find_next(i);
            if(small != x[i])
            {
                temp = x[i];
                x[i] = x[index];
                x[index] = temp;
                sorting(&x[i+1],length - (i+1));
                break;
            }
        }

        if(i == -1)
        {
            x[length] = 0;
            length++;
            sorting(x,length);
            temp = x[0];
            x[0] = x[1];
            x[1] = temp;

            if(x[0] == 0)
            {
                for(j=0;j<length;j++)
                {
                    if(x[j] != 0)
                        break;
                }

                x[0] = x[j];
                x[j] = 0;
            }
        }
        

        //printf("Case #%d: ",t++);
        fout << "Case #" << t++ << ": " ;
        for(i=0;i<length;i++)
        {
            //printf("%d",x[i]);
            fout << x[i];
        }
        fout << endl;
    }

}
