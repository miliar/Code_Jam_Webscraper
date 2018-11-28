#include<iostream>
#include<cstdio>
#include<vector>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<string>
#include<algorithm>
//#include<nevertimelimited.h>
//#include<neverwronganswer.h>
//#include<accepted forever.h>
using namespace std;
int rem[30][30];
bool op[30][30];
int main(void){
	FILE * fp1=fopen("in.in","r");
	FILE * fp2=fopen("out.in","w");
	int t,k,n,ep,j;
	char s[5],str[110];
	int vec[120];
	fscanf(fp1,"%d",&t);
	for(k=1;k<=t;k++){
		memset(rem,0,sizeof(rem));
		memset(op,false,sizeof(op));
		fscanf(fp1,"%d",&n);
		for(int i=0;i<n;i++){
			fscanf(fp1,"%s",s);
			rem[s[0]-'A'][s[1]-'A']=s[2]-'A';
			rem[s[1]-'A'][s[0]-'A']=s[2]-'A';
		}
		fscanf(fp1,"%d",&n);
		for(int i=0;i<n;i++){
			fscanf(fp1,"%s",s);
			op[s[0]-'A'][s[1]-'A']=true;
			op[s[1]-'A'][s[0]-'A']=true;
		}
		fscanf(fp1,"%d",&n);
		fscanf(fp1,"%s",str);
		ep=0;
		for(int i=0;i<n;i++){
			if(ep!=0){
				if(rem[vec[ep-1]][str[i]-'A']!=0) vec[ep-1]=rem[vec[ep-1]][str[i]-'A'];
				else{
					for(j=0;j<ep;j++){
						if(op[vec[j]][str[i]-'A']){
							break;
						}
					}
					if(j==ep) vec[ep++]=str[i]-'A';
					else ep=0;
				}
			}
			else vec[ep++]=str[i]-'A';
		}
//		cout<<ep<<endl;   /////////////////////////
		fprintf(fp2,"Case #%d: [",k);
		for(int i=0;i<ep-1;i++){
			fprintf(fp2,"%c, ",char(vec[i]+'A'));
		}
		if(ep!=0) fprintf(fp2,"%c",char(vec[ep-1]+'A'));
		fprintf(fp2,"]\n");
	}
	system("pause");
	return 0;
}