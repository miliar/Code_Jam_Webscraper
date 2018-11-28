#include <stdio.h>
#include <stdlib.h>
#include <iostream.h>
#include <conio.h>
int main () {FILE *fp;FILE *fd;char ch[3][4];char c;int i=0;int j=0;int k=0;int q=0;int d=0;int l=0;int n=0;char p[25][10];char e[10][10000];fp = fopen("c:/c++/ex1/A-small-attempt2.in", "r");c = getc(fp);while(c!='\n'){if(c==' '){i++;j=0;}else{ch[i][j]=c;j++;}c=getc(fp);}l=atoi(ch[0]);d=atoi(ch[1]);n=atoi(ch[2]);i=j=0;while(i<d){c=getc(fp);p[i][j]=c;if(c=='\n'){i++;j=0;}else{j++;}}i=j=0;while(i<n){c=getc(fp);e[i][j]=c;if(c==EOF){e[i][j]='\0';i++;}else if(c=='\n'){i++;j=0;}else{j++;}}i=j=0;bool ve=false;int le=0;int t[10];while(i<n){while(j<d){while(k<l){if(e[i][q]=='('){while(e[i][q]!=')'){if(p[j][k]==e[i][q]&&ve==false){ve=true;}q++;}if(ve){ve=false;le++;}}else{if(p[j][k]==e[i][q]){le++;}}q++;k++;}q=0;k=0;if(le==l){t[i]++;}le=0;j++;}i++;j=0;}fd=fopen("c:/c++/ex1/result.txt","w");char a[1];for(i=0;i<10;i++){itoa(t[i],a,10);fprintf(fd,"Case #%d: %-10.10s\n",i+1,a);}fclose(fp);fclose(fd);getch();}
