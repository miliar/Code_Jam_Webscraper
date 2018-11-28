//BISMILLAHHIRRAHMANIRRAHIM


#include <iostream>
#include <cstring>
#include <string>
using namespace std;

char dic[5005][200];
char word[200][500];
bool f[20];

int r,d,l;

bool isin(const char *a,const char *b) {
	int i;
	for(i=0;a[i]&&b[i];i++) if(a[i]!=b[i]) return false;
	return true;
}


void com(char w[][500],char *p,int s) {
	//printf("%d %s %s %d %d\n",s,w[0],p,f[s],d);
	if(!w[0][0] || s==l) {
		for(int i=0;i<d;i++) {
			
			if(!strcmp(p,dic[i])) {//printf("%s %d %s\n",p,i,dic[i]);
				r++;
				return;
			}
		}
		return;
	}
	printf("%d %d\n",f[s],s);
	if(f[s]) for(int i=0;w[0][i];i++) {
		puts(p);
		int l=strlen(p);
		p[l]=w[0][i];
		p[l+1]='\0';
		bool k=0;
		for(int i=0;i<d;i++) {
			if(i==4) printf("%s %s\n",dic[i],p);
			if(isin(p,dic[i])) {
				k=1;
				break;
			}
		}
		if(k) com(&w[1],p,s+1);
		else printf("%s %d %d\n",p,s);
	}
	else {
		strcat(p,w[0]);
		bool k=0;
		for(int i=0;i<d;i++) {
			//if(i==4) printf("%s %s\n",dic[i],p);
			if(isin(p,dic[i])) {
				k=1;
				break;
			}
		}
		if(k) com(&w[1],p,s+1);
	}
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("smallout2.txt","w",stdout);
	int I,n,i,j;
	char c[50];
	scanf("%d %d %d",&l,&d,&n);
	fgetc(stdin);
	for(i=0;i<d;i++) gets(dic[i]);
	for(I=1;I<=4;I++) {
		//printf("%d\n",n);
		memset(f,0,sizeof(f));
		memset(word,0,sizeof(word));
		r=0;
		for(i=0;i<l;i++) {
			word[i][0]=fgetc(stdin);
			if(word[i][0]=='\n') word[i][0]=fgetc(stdin);
			if(word[i][0]=='(') {
				scanf("%[^) \n]",word[i]);
				fgetc(stdin);
				f[i]=1;
			}
			else {
				scanf("%[^( \n]",&word[i][1]);
				puts(word[i]);
				i+=strlen(word[i]);
			}
		}
		if(f[0]) for(j=0;word[0][j];j++) {
			memset(c,0,sizeof(0));
			c[0]=word[0][j];
			c[1]='\0';
			com(&word[1],c,1);
		}
			else {
				memset(c,0,sizeof(0));
				strcat(c,word[0]);
				com(&word[1],c,1);
		}
		//for(i=0;word[i][0];i++) printf("%d %s\n",i,word[i]);
		printf("Case #%d: %d\n",I,r);
		
	}
	return 0;
}
