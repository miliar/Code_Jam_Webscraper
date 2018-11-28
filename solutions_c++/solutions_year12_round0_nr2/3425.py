/* 
 * File:   mkdirect.cpp
 * Author: iskumar
 *
 * Created on March 23, 2012, 6:39 PM
 */

#include<fstream>
#include<iostream>
#include <cstdlib>

using namespace std;
int compare(char *with,char *to) {
char *ww,*tw;
int best =0,i=0;
do{ i++;
    if(with[i] == to[i]) {
	if(with[i] == '/') {
	    best ++;
	}
	else if(with[i]== 0) return(-1);
	else continue;
    }
    else if((to[i]==0)&&(with[i]=='/')) return(-1);
    else if((with[i]==0)&&(to[i]=='/')) return(best+1);
    else return best;
}while(1);
}

int create(char *str,int best) {
int i=0,ret=0;
    do{
       if(str[i++]== '/')  {cout <<i<<"once";ret++;}
    }while(str[i]!=0);
return(ret-best);
}

main()
{
int tc,j,total;
int N,p,S,score[100],flag[100];
ifstream f;ofstream f2;
f.open("C:/Turboc3/input.txt");
f2.open("C:/Turboc3/o.txt");
f >> tc;
for(int i=0;i<tc;i++) {
    total=0;
    f >> N >> S >> p;
    for (j=0;j<N;j++) {
        f >> score[j];
        flag[j]=0;
    }
    for(j=0;j<N;j++) {
        if((score[j]>=3*p-2)&&(flag[j]==0)) {
            flag[j]=1;
            total++;
        } else if((score[j]>=3*p-4)&&(flag[j]==0)&&(S>0)) {
            if((p==0)||(score[j]>0)) {
                flag[j]=1;
                total++;
                S--;
            }
        }
    }
    f2 << "Case #"<<i+1<<": "<<total<<"\n";
}
f.close();
f2.close();
return 0;
}
