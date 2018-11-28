#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

char s[100][101];
int comp(char q[],int a){
    int j;
    for(j=0;j<a;j++)
	    if(strcmp(q,s[j])==0)
		  break;
    return j;
}

int main(){
    char temp[255];
    int n;
    ifstream in("A-small.in");
	ofstream out("A-small.out");
    in.getline(temp,255);
    n=atoi(temp);
    for(int j=1;j<=n;j++){
	    int w,a,b,swch=0;
	    char q[100][101],match[101],yes[101],no[101];
	    in.getline(temp,255);
	    a=atoi(temp);
	    for(int i=0;i<a;i++){
		    in.getline(s[i],255);
		    yes[i]='y';
		    no[i]='n';
	    }
	    yes[a]='\0';no[a]='\0';
	    strcpy(match,no);
	    in.getline(temp,255);
	    b=atoi(temp);
	    for(int i=0;i<b;i++)
		    in.getline(q[i],255);

	    for(int k=0;k<b;k++){
		    w=comp(q[k],a);
		    match[w]='y';
		    if(strcmp(match,yes)==0){
			    swch++;
			    strcpy(match,no);
			    match[w]='y';
		    }
	   }
	   out<<"Case #"<<j<<": "<<swch<<'\n';
	   cout<<j;

    }
    in.close();
    out.close();
 }
